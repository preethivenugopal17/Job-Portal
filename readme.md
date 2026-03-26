# 🏢 Job Portal — Django Web Application

A full-stack job portal web application built with Python and Django where users can browse, search, filter and apply for jobs.

## 📸 Screenshots
![Homepage](screenshot.png) ← Add your screenshot here

---

## ✨ Features

- 🔐 User Registration & Login
- 🔍 Search jobs by title, company or location
- 🗂️ Filter jobs by type — Full Time, Part Time, Remote, Internship
- 📋 View detailed job descriptions
- 📝 Apply for jobs with a cover letter
- ✅ Prevents applying to the same job twice
- ⚙️ Admin panel to manage all job listings
- 📱 Responsive design for all screen sizes

---

## 🛠️ Tech Stack

| Technology | Purpose |
|---|---|
| Python 3.12 | Programming language |
| Django 5.x | Web framework |
| SQLite | Database |
| HTML & CSS | Frontend |
| Django Templates | Dynamic pages |
| Django Auth | Login & Registration |

---

## 📁 Project Structure

```
job_portal/
├── core/                   # Project settings & main URLs
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── jobs/                   # Main jobs app
│   ├── templates/jobs/
│   │   ├── base.html       # Common layout
│   │   ├── job_list.html   # Homepage with search
│   │   ├── job_detail.html # Single job page
│   │   └── apply.html      # Application form
│   ├── models.py           # Job & Application models
│   ├── views.py            # Page logic
│   ├── urls.py             # URL routing
│   ├── forms.py            # Application form
│   └── admin.py            # Admin configuration
├── accounts/               # Authentication app
│   ├── templates/accounts/
│   │   ├── login.html
│   │   └── register.html
│   ├── views.py
│   └── urls.py
├── manage.py
└── requirements.txt
```

---

## ⚙️ Installation & Setup

### 1. Clone the repository
```bash
git clone https://github.com/yourusername/job-portal.git
cd job-portal
```

### 2. Create virtual environment
```bash
python -m venv venv

# Activate on Windows:
venv\Scripts\activate

# Activate on Mac/Linux:
source venv/bin/activate
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```

### 4. Run migrations
```bash
python manage.py makemigrations
python manage.py migrate
```

### 5. Create admin account
```bash
python manage.py createsuperuser
```

### 6. Run the server
```bash
python manage.py runserver
```

### 7. Open in browser
```
Homepage  → http://127.0.0.1:8000/
Admin     → http://127.0.0.1:8000/admin/
Register  → http://127.0.0.1:8000/accounts/register/
Login     → http://127.0.0.1:8000/accounts/login/
```

---

## 🗄️ Database Models

### Job Model
| Field | Type | Description |
|---|---|---|
| title | CharField | Job title |
| company | CharField | Company name |
| location | CharField | Job location |
| job_type | CharField | Full Time / Part Time / Remote / Internship |
| description | TextField | Full job description |
| salary | CharField | Salary range (optional) |
| posted_at | DateTimeField | Date posted |

### Application Model
| Field | Type | Description |
|---|---|---|
| job | ForeignKey | Which job applied to |
| applicant | ForeignKey | Which user applied |
| cover_letter | TextField | Applicant's cover letter |
| applied_at | DateTimeField | Date of application |

---

## 🚀 Deployment

This project is deployed on Railway.
- Live URL: [your-app.railway.app](#) ← Add your link

---

## 👩‍💻 Author

**Preethi**
- GitHub: [@yourusername](#)
- LinkedIn: [your linkedin](#)

---

## 📚 What I Learned

- Building a full stack web application with Django
- Implementing user authentication from scratch
- Working with Django ORM and database models
- Creating reusable templates with template inheritance
- Handling forms and user input securely
- Deploying a Django application to production

---

## 🔮 Future Improvements

- [ ] Email notifications when application is received
- [ ] Resume upload feature
- [ ] Job recommendations based on profile
- [ ] Company profiles and dashboards
- [ ] React frontend for better user experience
