# Job-Application-Tracker

## Setup

1. Create and activate a Python virtual environment:

   Windows PowerShell:
   ```powershell
   python -m venv venv
   .\venv\Scripts\Activate.ps1
   ```

2. Install dependencies:

   ```powershell
   pip install -r requirements.txt
   ```

3. Apply migrations:

   ```powershell
   python manage.py migrate
   ```

4. (Optional) Configure OpenAI for follow-up email generation:

   ```powershell
   $env:OPENAI_API_KEY = "your_openai_api_key"
   ```

5. Run the development server:

   ```powershell
   python manage.py runserver
   ```

6. Open the API at: `http://127.0.0.1:8000`

## API Endpoints

Base URL: `http://127.0.0.1:8000/api/applications/`

### 1. List applications

- Method: `GET`
- URL: `/api/applications/`
- Query params: `status` (optional) to filter by `applied`, `interviewing`, `rejected`, or `offered`

Example:
```bash
curl http://127.0.0.1:8000/api/applications/
```

Example filtering by status:
```bash
curl "http://127.0.0.1:8000/api/applications/?status=interviewing"
```

### 2. Create a new application

- Method: `POST`
- URL: `/api/applications/`
- Body: JSON

Example:
```bash
curl -X POST http://127.0.0.1:8000/api/applications/ \
  -H "Content-Type: application/json" \
  -d '{
    "company": "Acme Corp",
    "role": "Software Engineer",
    "status": "applied",
    "notes": "Submitted application via company portal."
  }'
```

### 3. Retrieve application detail

- Method: `GET`
- URL: `/api/applications/<id>/`

Example:
```bash
curl http://127.0.0.1:8000/api/applications/1/
```

### 4. Update an application

- Method: `PATCH`
- URL: `/api/applications/<id>/`
- Body: partial JSON to update fields

Example:
```bash
curl -X PATCH http://127.0.0.1:8000/api/applications/1/ \
  -H "Content-Type: application/json" \
  -d '{
    "status": "interviewing",
    "notes": "Phone screen scheduled for Friday."
  }'
```

### 5. Delete an application

- Method: `DELETE`
- URL: `/api/applications/<id>/`

Example:
```bash
curl -X DELETE http://127.0.0.1:8000/api/applications/1/
```

### 6. Summary counts

- Method: `GET`
- URL: `/api/applications/summary/`

Example:
```bash
curl http://127.0.0.1:8000/api/applications/summary/
```

Response example:
```json
{
  "applied": 3,
  "interviewing": 1,
  "rejected": 0,
  "offered": 1
}
```

### 7. Generate follow-up email

- Method: `POST`
- URL: `/api/applications/<id>/generate-followup/`
- Requires `OPENAI_API_KEY` configured in environment

Example:
```bash
curl -X POST http://127.0.0.1:8000/api/applications/1/generate-followup/
```

Response example:
```json
{
  "email": "Hello [Hiring Manager],\n\nThank you for reviewing my application for the Software Engineer role at Acme Corp..."
}
```

## Model fields

Each job application includes:
- `id`
- `company`
- `role`
- `status`
- `applied_date`
- `notes`

## Notes

- The follow-up generation endpoint uses OpenAI and will return an error if the API key is not configured correctly.
- Status values are normalized to lowercase on create/update.
