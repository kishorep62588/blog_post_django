## Blogpost website application using Django
    This is an application of creating blogposts by different users who are loggedin to the website.
This blogpost app is designed using Python Django framework in the backend and this is very basic code.

### Requirements
Below are the requirements to run this application on Local computer
- Python 3.6 or above
- Virtual environment which is helpful to install only required libraries to application rather everything
    installed in system level
- Django framework
- Pillow
- Django-crispy-forms

### Installing Python and required libraries in virtual environment

WIP

### Running the Application
- clone the repo using git clone command
- Navigate to project directory by using cd command
- Activate virtual environment and install required libraries
- Change to project directory
- Run "py manage.py makemigrations" or "python3 manage.py makemigrations" depending on your operating system.
- Run "py manage.py migrate" or "python3 manage.py migrate" depending on your operating system.
- This will update the project with all the settings present in the html pages and authentication.
- Run "py manage.py runserver" or "python3 manage.py runserver" depending on your operating system.
- If all the installation process successful, user can see the below page as welcome page.
![starting_screen](/screenshots/homescreen_without_profiles.jpg)
- Please note, since there is no data present in the db. you will get blank page with navigation bar like above.
- User can change the logos by replacing the existing logos and assign then using Django admin panel.

### Updates Todo
- Since this is a sample app, content of blog post is not proper which can be changed.