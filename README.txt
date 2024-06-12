# Django Web Scraping Project

This project is a Django application that performs web scraping using `requests`, `BeautifulSoup`, and `selenium`, and saves the scraped data into the database.

## Prerequisites

- Python  latest version 
- pip (Python package installer)
- Google Chrome (for Selenium)
- ChromeDriver (ensure it's compatible with your version of Chrome)(ChromeDriver 124.0.6367.91 )


If there is any problem try using virtual environment

##install all dependencies listed in requirements.txt.

bash


pip install -r requirements.txt


If you encounter any errors while installing the dependencies, install them individually:

bash

pip install django
pip install requests
pip install beautifulsoup4
pip install selenium
pip install requests-html
pip install torch
pip install transformers


## Download ChromeDriver
Download the ChromeDriver from here and place it in a directory that is in your system's PATH, or specify its location in the script.
(ChromeDriver 124.0.6367.91 )

## Apply Migrations
Apply the initial migrations to set up your database schema.

bash

python manage.py migrate

If you have defined new models or made changes to existing ones, create new migrations and apply them:

bash

python manage.py makemigrations
python manage.py migrate



## Run the Development Server
Start the Django development server.

bash

python manage.py runserver
Visit http://127.0.0.1:8000/ in your web browser to see the running application.



Useful Commands
Run migrations: python manage.py migrate
Create new migrations: python manage.py makemigrations
Run development server: python manage.py runserver
Create superuser: python manage.py createsuperuser
Check for errors: python manage.py check