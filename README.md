# DjangoProjects
Official Documenation: https://docs.djangoproject.com/en/4.2/

## Getting Started

Follow these steps to set up and run the application:

1. Clone the repository:

   https://github.com/tmatin100/DjangoProjects


3. Change directory into any sample project, create a virtual environment and install dependencies:
   ```bash
   cd django_rest_framework
   ```

   ```bash
   python -m venv venv
   ```

   ```bash
   . venv/bin/activate
   ```
   ```bash
   on Windows: venv\Scripts\activate
   ```
   
   ```bash
   pip install -r requirements.txt
   ```

4. Create a Django project and name it config in the current directory:

    ```python
   django-admin startproject config .
   ```

5. Create a Django app named test_app:

   ```bash
   python manage.py startapp
   ```
6. Run the server:

   ```bash
   python manage.py runserver
   ```

5. Usage
     To use the application, navigate to http://127.0.0.1:8000/ in your web browser.

     You can also access the API at http://localhost:8000/api
