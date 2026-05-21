# Job-Application-Tracker

Application Tracker API built using Django REST Framework to manage and track job applications. It supports full CRUD operations, filtering, summary, and AI-powered follow-up email generation.

**Features:**
- Create, Read, Update, Delete job applications
- Filter applications by status
- Summary endpoint (grouped count by status)
- AI-generated follow-up email using OpenAI API

**Tech Stack:**
- Python
- Django
- Django REST Framework
- SQLite (default database)
- OpenAI API (for email generation)

**Project Setup:**
**1. clone the repo** 
-   git clone https://github.com/Sanjay-Gundeboina/Job_Application_Tracker.git
-   cd JobTracker

**2. Create Virtual Environment**
-   python -m venv venv
  
**3. Activate Virtual Environment**
-  venv\Scripts\activate

**4. Install Dependencies**
-   pip install -r requirements.txt
  
**5. Run Migrations**
-   python manage.py makemigrations
-   python manage.py migrate

**6. Run Server**
-   python manage.py runserver

**API Endpoints**
1. Create Job Application -> works only with post method
-   POST /api/applications/

**Request Body:**
{
  "company": "petabytz",
  "role": "Backend developer intern",
  "status": "applied",
  "notes": "Applied through Linked in "
}

**2. Get All Applications (with filter)**
-- GET /api/applications/
-- GET /api/applications/?status=applied

**3. Get Application by ID**
-- GET /api/applications/<id>/

**4. Update Application Status**
-- PATCH /api/applications/<id>/

**Request Body:**

{
  "status": "interviewing"
}

**5. Delete Application**
-- DELETE /api/applications/<id>/

**6. Summary Endpoint**
-- GET /api/applications/summary/

**Response Example:**
{
  "applied": 5,
  "interviewing": 2,
  "rejected": 1,
  "offered": 1
}

**7. AI Follow-up Email Generator**
-- POST /api/applications/<id>/generate-followup/
-- In Setting.py file change your api key OPENAI_API_KEY

**Project Structure**

jobtracker/
│
├── applications/
│   ├── models.py
│   ├── views.py
│   ├── serializers.py
│   ├── urls.py
│   ├── tests.py
│
├── job_tracker/
│   ├── settings.py
│   ├── urls.py
│
├── manage.py
└── requirements.txt


**Notes:**
-- Ensure migrations are applied before running tests
-- OpenAI API key is required only for the follow-up endpoint
-- All endpoints return JSON responses
