#!/usr/bin/env python
import os
import sys

if __name__ == '__main__':

    # Check the user has all of the
    errors = 0

    try:
        import crispy_forms
    except ImportError:
        print("Couldn't import `crispy_forms`.")
        print("Run `pip install django-cripsy-forms` to install it.")
        errors += 1

    if errors:
        print("Exited with {} errors.".format(errors))
        exit(1)

    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'orm_example.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)
