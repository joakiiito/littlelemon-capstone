LITTLE LEMON CAPSTONE - API PATHS FOR REVIEWERS
=================================================

Base URL while running locally: http://127.0.0.1:8000

Pages
-----
  /                       Home page (Django-rendered HTML)
  /admin/                 Django admin

Menu API (public read, authenticated write)
--------------------------------------------
  /api/menu/              GET (list) / POST (create, auth required)
  /api/menu/<id>/         GET / PUT / DELETE (auth required for write)

Booking API (authentication required for all actions)
-------------------------------------------------------
  /api/bookings/          GET (list) / POST (create)
  /api/bookings/<id>/     GET / PUT / DELETE

Authentication
---------------
  /api-token-auth/        POST {"username": "...", "password": "..."} -> {"token": "..."}
  /auth/users/             POST -> register a new user (djoser)
  /auth/token/login/       POST -> obtain an auth token (djoser)
  /auth/token/logout/      POST -> invalidate the current token (djoser)

SUGGESTED TEST FLOW (Insomnia / browsable API)
------------------------------------------------
1. POST /auth/users/ with {"username": "testuser", "password": "testpass123"} to register a user.
2. POST /api-token-auth/ with the same credentials to get a token.
3. Add header "Authorization: Token <token>" to subsequent requests.
4. GET /api/menu/ (works without auth too).
5. POST /api/bookings/ with {"name": "Test", "no_of_guests": 2, "booking_date": "2026-08-01T19:00:00Z"}.
6. GET /api/bookings/ to confirm the booking was created.

SETUP
-----
1. Create the MySQL database (name used in settings.py is "littlelemon"):
       mysql -u root -p
       CREATE DATABASE littlelemon;

2. Open littlelemon/settings.py and set your local MySQL credentials in DATABASES
   (USER / PASSWORD will vary depending on your local machine).

3. Create the virtual environment and install dependencies:
       cd littlelemon
       pipenv shell
       pipenv install

4. Run migrations and start the server:
       python manage.py makemigrations
       python manage.py migrate
       python manage.py runserver

5. Run the unit tests:
       python manage.py test
