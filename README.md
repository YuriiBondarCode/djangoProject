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

Get the Token

``` 
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token 
user = User.objects.get(username="username") 
token, created = Token.objects.get_or_create(user=user)
print(token.key)
``` 


Navigate to: 

API (DRF): ```http://127.0.0.1:8000/api/```

Swagger UI: ```http://127.0.0.1:8000/api/schema/swagger-ui/``` ( Authenticate using: "Token + {token}" from get the token section)

Admin: ```http://127.0.0.1:8000/admin/ ```
