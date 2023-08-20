# Django-eco_machine

## Installation:   

```pip install -r requirements.txt```  
Enter data in .env  
Then run  
```cd eco_m```  
```celery -A mysite worker -l info```  
```python manage.py makemigrations```  
```python manage.py migrate```  
```python manage.py test```  
```python manage.py createsuperuser```  
```python manage.py runserver```  

## Paths :
- `/api/`
  - `get` - All routes.
