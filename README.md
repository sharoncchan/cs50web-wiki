# Wiki Project

This project is a web application of a Wikipedia-like online encyclopedia .

This project was built using Django as a backend framework and HTML, CSS and Bootstrap as frontend programming tools. 

All webpages of the project are mobile-responsive.

#### Features of the project 
This project contains the features below where a user can:
- create a new encylopedia entry in markdown format
- edit an existing entry and save the edited entry
- be taken to random entry by clicking “Random Page” in the sidebar
- search for an entry. If the search query matches an entry title, the user will be redirected to the entry page. Otherwise, the results page will display a list of all entries that have the query as a substring. 


#### Running the application
  - Install project dependencies by running `pip install -r requirements.txt`.
  - Make and apply migrations by running `python manage.py makemigrations` and `python manage.py migrate`.
  - Create superuser with `python manage.py createsuperuser`. This will create a user with admin privileges, with permissions to create, read, update and delete data in the Django admin
  - Run the django server using `python manage.py runserver` to enter the homepage of the web application.

#### Files and directories
  - `encyclopedia` - main application directory.
    - `static/network` contains all static content.
        - `styles.css` contains compiled CSS file

    - `templates/encyclopedia` contains all application templates.
        - `layout.html` - Base templates. Other templates extend it.
        - `index.html` -  The homepage of the webpage, displays the titles of all the entries
        - `create.html` - Displays the page to create a new entry
        - `edit.html` - Displays the page to edit an entry and save the edited entry
        - `error.html` - Displays the different error messages
        - `pages.html` - Displays the individual entry page
        - `search.html` - Displays the search results after a search query is submitted
      
    - `urls.py` - contains all application URLs.
    - `views.py`  contains all application views.

My project's video :https://www.youtube.com/watch?v=Uj_kDkJnEyQ
