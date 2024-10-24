#!/usr/bin/env python3.10
"""Django's command-line utility for administrative tasks."""
import os
import sys
import environ

from LocalAdventuresBack.settings.base import BASE_DIR

# Initialize the environment variables
env = environ.Env()
environ.Env.read_env(os.path.join(BASE_DIR, '.env'))


def main():
    """Run administrative tasks."""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', env.str('DJANGO_ENVIRONMENT_FILE', default='LocalAdventuresBack.settings.prod'))
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()
