## Installation

Create and activate virtual environment

```
python -m venv venv  
source venv/bin/activate  # Mac/Linux  
venv\Scripts\activate  # Windows
```
Clone this repository

```git clone https://github.com/YuriiBondarCode/djangoProject.git```

Install requirements.txt

```pip install -r requirements.txt```

Run migrations

```python manage.py migrate```

Start server

```python manage.py runserver```

Create superuser

``` python manage.py createsuperuser```

Get the Simple JWT Token

``` 
curl \
  -X POST \
  -H "Content-Type: application/json" \
  -d '{"username": "username", "password": "password"}' \
  http://localhost:8000/api/token/
``` 


Navigate to: 

API (DRF): ```http://127.0.0.1:8000/api/```

Swagger UI: ```http://127.0.0.1:8000/api/schema/swagger-ui/``` ( Authenticate using token from get the token section)

Admin: ```http://127.0.0.1:8000/admin/ ```
