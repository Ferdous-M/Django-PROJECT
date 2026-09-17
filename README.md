# Company API

A Django REST Framework API for managing company information.

## Project Structure

```
companyapi/
├── api/                 # Main Django app
│   ├── admin.py         # Admin configuration
│   ├── apps.py          # App configuration
│   ├── migrations/      # Database migrations
│   ├── models.py        # Database models (Company)
│   ├── seriliazers.py   # Serializers (typo: should be serializers)
│   ├── tests.py         # Test cases
│   ├── urls.py          # App URLs
│   └── views.py         # ViewSets (CompanyViewSet)
├── companyapi/          # Project settings
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py      # Django settings
│   ├── urls.py          # Root URL configuration
│   ├── views.py         # Home page view
│   └── wsgi.py
├── manage.py            # Django management script
├── db.sqlite3           # SQLite database
└── README.md            # This file
```

## Features

- RESTful API for Company management
- Company model with fields:
  - id (AutoField)
  - name (CharField)
  - location (CharField)
  - about (TextField)
  - type (CharField with choices: IT, Non IT, Mobiles Phones)
  - added_date (DateTimeField, auto_now=True)
  - active (BooleanField, default=True)
- Django REST Framework ViewSets for full CRUD operations
- Admin interface for easy data management
- Simple home page endpoint returning a JSON response

## Setup Instructions

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd companyapi
   ```

2. **Create a virtual environment (recommended)**
   ```bash
   python -m venv venv
   # On Windows:
   venv\Scripts\activate
   # On Unix/Linux/MacOS:
   source venv/bin/activate
   ```

3. **Install dependencies**
   ```bash
   pip install django djangorestframework
   ```

4. **Apply migrations**
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

5. **Create a superuser (for admin access)**
   ```bash
   python manage.py createsuperuser
   ```

6. **Run the development server**
   ```bash
   python manage.py runserver
   ```

## API Endpoints

- **Admin Interface**: `/admin/`
- **Home Page**: `/home/` - Returns a simple JSON response
- **Company API**: `/api/v1/companies/` - Full CRUD operations for Company model
  - GET: List all companies
  - POST: Create a new company
  - GET/{id}: Retrieve a specific company
  - PUT/{id}: Update a specific company
  - PATCH/{id}: Partially update a specific company
  - DELETE/{id}: Delete a specific company

## Models

### Company
| Field | Type | Description |
|-------|------|-------------|
| company_id | AutoField | Primary key |
| name | CharField(max_length=50) | Company name |
| location | CharField(max_length=50) | Company location |
| about | TextField | Company description |
| type | CharField(max_length=100) | Company type (IT, Non IT, Mobiles Phones) |
| added_date | DateTimeField | Timestamp when record was created |
| active | BooleanField | Whether the company is active |

## Views

### Home Page (`companyapi/views.py`)
- Simple view that returns a JSON response with a list of friends

### CompanyViewSet (`api/views.py`)
- ModelViewSet providing default create, retrieve, update, delete, and list actions
- Uses CompanySerializer for serialization
- Queryset: All Company objects

## Serializers

### CompanySerializer (`api/seriliazers.py`)
- HyperlinkedModelSerializer for Company model
- Includes all fields (`fields = "__all__"`)

## URLs

### Project URLs (`companyapi/urls.py`)
- `/admin/` - Django admin interface
- `/home/` - Home page view
- `/api/v1/` - Includes API URLs from the `api` app

### App URLs (`api/urls.py`)
- Uses Django REST Framework's DefaultRouter
- Registers CompanyViewSet at the root path (`''`)
- Provides standard RESTful endpoints for companies

## Running Tests

```bash
python manage.py test
```

## Notes

- The project uses SQLite3 as the database (configured in settings.py)
- DEBUG is set to True in settings.py (suitable for development only)
- The SECRET_KEY is hardcoded (should be moved to environment variables in production)
- There's a typo in the serializer filename: `seriliazers.py` instead of `serializers.py`

## Future Improvements

1. Fix the typo in `seriliazers.py` → `serializers.py`
2. Add proper validation and constraints to the Company model
3. Implement authentication and permissions for the API
4. Add pagination to API endpoints
5. Include API documentation (using drf-yasg or similar)
6. Add unit and integration tests
7. Use environment variables for sensitive settings
8. Add frontend interface or API client examples