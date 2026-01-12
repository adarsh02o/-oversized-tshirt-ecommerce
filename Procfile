web: gunicorn tshirt_ecommerce.wsgi:application
release: python manage.py migrate
release: python manage.py collectstatic --noinput
