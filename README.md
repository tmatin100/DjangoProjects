# DjangoProjects
https://www.djangoproject.com/

## Getting Started

Follow these steps to set up and run the application:

1. Clone the repository:

   https://github.com/tmatin100/DjangoProjects


3. Cd into any sample project and Create a virtual environment and install dependencies:
   ```bash
   cd django_rest_framework
   ```

   ```bash
   python -m venv venv
   ```

   ```bash
   source venv/bin/activate
   ```


  ```bash
   on Windows: venv\Scripts\activate )
   ```

 ```python
 pip install -r requirements.txt
 ```

4. Create a Django project and name it config in the current directory:

    ```python
   django-admin startproject config .
   ```

5. Create a Django app named test_app

   ```python
  django-admin startapp test_app
   ```
6. Run the server:

   ```bash
   python manage.py runserver
   ```

5. Usage
     To use the application, navigate to http://127.0.0.1:8000/ in your web browser.

     You can also access the API at http://localhost:8000/api
