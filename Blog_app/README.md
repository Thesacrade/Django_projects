# Blog_app

A small Django blog application with user registration/login, post creation (with image banners), and a simple public listing and detail pages.

This project was created with Django and uses SQLite for local development. It contains two apps:

- `posts` — models, views and templates for creating and listing blog posts.
- `user` — simple user registration, login and logout views.

Tech stack
- Python (3.11+ recommended)
- Django 5.1.x (this project uses Django 5.1.7)
- SQLite (default DB for this repo)
- Pillow (required for ImageField handling)

Project layout (relevant files)

- `manage.py` — Django CLI entrypoint
- `api/` — project settings, root URLconf, and views
  - `api/settings.py` — main settings (STATIC/MEDIA, INSTALLED_APPS, DEBUG)
  - `api/urls.py` — includes routes for the site and static/media helpers
- `posts/` — blog app (models, forms, views, templates, urls)
- `user/` — user auth views and urls
- `templates/` — top-level templates (`index.html`, `about.html`, `layout.html`)
- `static/`, `media/` — static assets and uploaded images
- `db.sqlite3` — default SQLite database (included in workspace)

Important notes from the code
- DEBUG is set to `False` in `api/settings.py`. For local development set `DEBUG = True` or configure appropriate host entries in `ALLOWED_HOSTS`.
- Image uploads use `MEDIA_ROOT`/`MEDIA_URL` configured in settings; `Pillow` is required to work with `ImageField`.

Routes / endpoints

The main routes available (seen in `api/urls.py`, `posts/urls.py`, and `user/urls.py`):

- `/` — homepage (renders `templates/index.html`)
- `/about/` — about page
- `/admin/` — Django admin
- `/posts/` — posts list (named `posts`)
- `/posts/new-post/` — create a new post (named `new-post`; login required)
- `/posts/<slug>` — post detail (named `post`)
- `/user/register/` — user registration
- `/user/login/` — user login
- `/user/logout/` — user logout

Setup (Windows PowerShell)

Open PowerShell and run the following commands from the repository root (`Blog_app`):

```powershell
# 1) Create and activate a virtual environment
python -m venv .venv
.\.venv\Scripts\Activate.ps1

# 2) Install dependencies (Django + Pillow)
pip install "django==5.1.7" Pillow

# 3) Apply database migrations
python manage.py migrate

# 4) (Optional) Create a superuser to access the admin
python manage.py createsuperuser

# 5) Collect static files (for production or when DEBUG=False)
python manage.py collectstatic --noinput

# 6) Run the development server
python manage.py runserver

```
Local development tips
- The project sets `DEBUG = False` by default. For local development change `api/settings.py` DEBUG to `True` or set up environment-based settings.
- When DEBUG=False, static files are typically served by a web server; during development you can still use `runserver` but you may need to ensure `STATICFILES_DIRS` and `STATIC_ROOT` are configured (they are in `api/settings.py`).
- Media files are served in `api/urls.py` using `django.conf.urls.static.static()` when `DEBUG` is on (and in many dev setups). Uploaded images for posts are stored under the `media/` folder.
- If you see image-related errors when uploading posters/banners, ensure Pillow is installed and that the `media/` directory is writable.

Troubleshooting
- ImportError: Couldn't import Django — ensure your virtualenv is activated and Django is installed.
- OperationalError: unable to open database file — confirm file permissions and path for `db.sqlite3`.
- 403 on POST to new-post — the view `new_post` requires login; log in at `/user/login/` or use the admin site to create posts.

Where to look next in the code
- `posts/models.py` — `Post` model fields (title, body, slug, banner, author)
- `posts/forms.py` — `CreatePost` ModelForm used to create posts
- `posts/views.py` — list, detail, and creation views
- `user/views.py` — registration and authentication views using Django's built-in forms

Status: README created to help new developers run and understand the project locally.
