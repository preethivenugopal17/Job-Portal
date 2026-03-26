from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Job, Application
from .forms import ApplicationForm
from .utils import (
    send_application_email,
    extract_text_from_resume,
    calculate_match_score
)


def job_list(request):
    jobs     = Job.objects.all()
    query    = request.GET.get('q', '')
    job_type = request.GET.get('job_type', '')

    if query:
        jobs = jobs.filter(title__icontains=query)   | \
               jobs.filter(company__icontains=query) | \
               jobs.filter(location__icontains=query)

    if job_type:
        jobs = jobs.filter(job_type=job_type)

    return render(request, 'jobs/job_list.html', {
        'jobs':             jobs,
        'query':            query,
        'job_type':         job_type,
        'job_type_choices': Job.JOB_TYPE_CHOICES,
    })


def job_detail(request, pk):
    job             = get_object_or_404(Job, pk=pk)
    already_applied = False
    application     = None

    if request.user.is_authenticated:
        try:
            application     = Application.objects.get(
                job=job, applicant=request.user
            )
            already_applied = True
        except Application.DoesNotExist:
            already_applied = False

    return render(request, 'jobs/job_detail.html', {
        'job':             job,
        'already_applied': already_applied,
        'application':     application,
    })


@login_required
def apply_job(request, pk):
    job = get_object_or_404(Job, pk=pk)

    if Application.objects.filter(job=job, applicant=request.user).exists():
        messages.warning(request, 'You have already applied for this job.')
        return redirect('jobs:job_detail', pk=pk)

    if request.method == 'POST':
        form = ApplicationForm(request.POST, request.FILES)
        if form.is_valid():
            application           = form.save(commit=False)
            application.job       = job
            application.applicant = request.user

            # Start with cover letter text
            combined_text = application.cover_letter.lower()

            # Also extract from resume if uploaded
            if 'resume' in request.FILES:
                resume_text = extract_text_from_resume(
                    request.FILES['resume']
                )
                combined_text          += ' ' + resume_text
                application.resume_text = resume_text

            # Calculate match score from both!!
            if combined_text.strip():
                score, matched, missing = calculate_match_score(
                    combined_text, job.required_skills
                )
                application.match_score    = score
                application.matched_skills = ', '.join(matched)
                application.missing_skills = ', '.join(missing)

            application.save()

            # Send email notification
            try:
                send_application_email(application)
            except Exception as e:
                print(f"Email error: {e}")

            messages.success(request, f'Successfully applied for {job.title}!')
            return redirect('jobs:job_detail', pk=pk)
    else:
        form = ApplicationForm()

    return render(request, 'jobs/apply.html', {
        'form': form,
        'job':  job,
    })