import pdfplumber
from django.core.mail import send_mail
from django.conf import settings


def extract_text_from_resume(resume_file):
    """Extract all text from uploaded PDF resume"""
    text = ''
    try:
        with pdfplumber.open(resume_file) as pdf:
            for page in pdf.pages:
                page_text = page.extract_text()
                if page_text:
                    text += page_text + ' '
    except Exception as e:
        print(f"Error extracting text: {e}")
    return text.lower().strip()


def calculate_match_score(resume_text, required_skills):
    """Compare resume/cover letter skills with job required skills"""

    if not required_skills or not resume_text:
        return 0, [], []

    resume_text = resume_text.lower()

    # Convert to clean word list
    words = [
        word.strip('.,!?;:()[]{}"\'')
        for word in resume_text.split()
    ]

    job_skills = [
        skill.strip().lower()
        for skill in required_skills.split(',')
        if skill.strip()
    ]

    # Skill variations
    variations = {
        'python': ['python', 'py'],
        'django': ['django'],
        'html': ['html', 'html5'],
        'css': ['css', 'css3'],
        'javascript': ['javascript', 'js'],
        'sql': ['sql', 'mysql', 'sqlite', 'postgresql'],
        'git': ['git', 'github'],
        'react': ['react', 'reactjs', 'react.js'],
        'rest api': ['rest', 'api', 'rest api'],
        'bootstrap': ['bootstrap'],
        'java': ['java'],
        'c': ['c', 'c programming'],
        'mongodb': ['mongodb', 'mongo'],
        'nodejs': ['nodejs', 'node.js', 'node'],
        'power bi': ['power bi', 'powerbi'],
        'tableau': ['tableau'],
        'excel': ['excel', 'ms excel'],
        'statistics': ['statistics', 'stats'],
        'flask': ['flask'],
        'machine learning': ['machine learning', 'ml'],
        'deep learning': ['deep learning', 'dl'],
        'data analysis': ['data analysis', 'data analytics'],
        'numpy': ['numpy'],
        'pandas': ['pandas'],
        'matplotlib': ['matplotlib'],
        'aws': ['aws', 'amazon web services'],
        'docker': ['docker'],
        'linux': ['linux', 'ubuntu'],
    }

    matched = []
    missing = []

    for skill in job_skills:
        skill_found = False

        # 1. Exact match
        if skill in words:
            skill_found = True

        # 2. Variation match
        elif skill in variations:
            for variant in variations[skill]:
                if variant in words:
                    skill_found = True
                    break

        if skill_found:
            matched.append(skill.title())
        else:
            missing.append(skill.title())

    # Calculate score safely
    score = int((len(matched) / len(job_skills)) * 100) if job_skills else 0

    return score, matched, missing


def send_application_email(application):
    """Send email notification when someone applies"""

    subject = f'New Application Received — {application.job.title}'
    from_email = settings.DEFAULT_FROM_EMAIL
    to_email = [settings.EMAIL_HOST_USER]

    text_content = f"""
New Job Application Received!!

Job Title   : {application.job.title}
Company     : {application.job.company}
Applicant   : {application.applicant.username}
Applied On  : {application.applied_at.strftime('%B %d, %Y %I:%M %p')}

Cover Letter:
{application.cover_letter}

Match Score    : {application.match_score}%
Matched Skills : {application.matched_skills or 'None'}
Missing Skills : {application.missing_skills or 'None'}

This email was sent from JobPortal!!
    """

    send_mail(
        subject,
        text_content,
        from_email,
        to_email,
        fail_silently=False,
    )