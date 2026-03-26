from django.db import models


class Job(models.Model):
    JOB_TYPE_CHOICES = [
        ('full_time',  'Full Time'),
        ('part_time',  'Part Time'),
        ('remote',     'Remote'),
        ('internship', 'Internship'),
    ]

    title           = models.CharField(max_length=200)
    company         = models.CharField(max_length=200)
    location        = models.CharField(max_length=200)
    job_type        = models.CharField(max_length=20, choices=JOB_TYPE_CHOICES, default='full_time')
    description     = models.TextField()
    salary          = models.CharField(max_length=100, blank=True, null=True)
    required_skills = models.CharField(
        max_length=500, blank=True, null=True,
        help_text='Enter comma separated skills e.g. Python, Django, SQL'
    )
    posted_at       = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.title} at {self.company}"

    class Meta:
        ordering = ['-posted_at']


class Application(models.Model):
    job              = models.ForeignKey(Job, on_delete=models.CASCADE, related_name='applications')
    applicant        = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    cover_letter     = models.TextField()
    resume           = models.FileField(upload_to='resumes/', blank=True, null=True)
    resume_text      = models.TextField(blank=True, null=True)
    match_score      = models.IntegerField(default=0)
    matched_skills   = models.CharField(max_length=500, blank=True, null=True)
    missing_skills   = models.CharField(max_length=500, blank=True, null=True)
    applied_at       = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('job', 'applicant')

    def __str__(self):
        return f"{self.applicant.username} applied to {self.job.title}"