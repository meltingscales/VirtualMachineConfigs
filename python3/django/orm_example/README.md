# How do I run this?

1.  Make sure you've made the migrations for the application.

    You can do this by running `python manage.py makemigrations orm_example`.

2.  Apply the migrations by running `python manage.py migrate`.

3.  Then, run `python manage.py runserver`.

    You only need to do step 1 and 2 whenever you change `models.py`.