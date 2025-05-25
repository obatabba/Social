# Social Platform (My Twitter)

[![MIT License](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)
[![Deploy on Render](https://img.shields.io/badge/Deployed%20on-Render-46a2f1)](https://social-mhtn.onrender.com)


> A minimalist social media platform built with Django, featuring dynamic interactions using HTMX and AJAX, and styled with Bootstrap.

Deployed Live: [https://social-mhtn.onrender.com](https://social-mhtn.onrender.com)

## Getting Started

To quickly run this project locally, see [Installation & Setup]([#installation--setup](#-installation--setup)) and [Development Setup]([#-development-setup]).

## 📌 Overview

This project serves as a foundational social media application, allowing users to register, authenticate, and interact through posts. It's designed to demonstrate core functionalities of Django in building dynamic web applications, with a clean and responsive UI powered by Bootstrap.

## 🚀 Features

* **User Authentication**: Register, log in, and log out functionalities with form validations and error handling.
* **Profile Management**: Users can create and manage their profiles with personal information.
* **Post Creation**: Ability to create, edit, and delete posts, including image attachments.
* **Dynamic Interactions**: Real-time updates to the user interface using HTMX and AJAX, eliminating full-page reloads.
* **Like System**: Users can like or unlike posts, with immediate feedback on the UI.

## 🛠️ Technologies Used

* **Backend**: Django
* **Frontend**: HTML, CSS, JavaScript, Bootstrap
* **Dynamic Behavior**: HTMX, AJAX
* **Database**: PostgreSQL
* **Media Storage**: Cloudinary (used in production), FileSystemStorage (used in development)
* **Deployment**: Render

## 📂 Project Structure

```
Social/
├── social/             # Main Django application
│   ├── settings/
│   │   ├── common.py   # Main Django configuration settings
│   │   ├── dev.py      # Development-specific settings
│   │   └── prod.py     # Production-specific settings
│   ├── asgi.py
│   ├── urls.py         # Main URLs configuration
│   └── wsgi.py
│
├── twitter/            # Project Core
│   ├── migrations/     # Database migrations
│   ├── static/         # Static files (CSS, JS, images)
│   ├── templates/      # HTML templates
│   ├── admin.py        # Admin configurations
│   ├── apps.py
│   ├── forms.py
│   ├── models.py
│   ├── signals.py
│   ├── urls.py         # Core app URLs configuration
│   └── views.py
│
├── .gitignore
├── manage.py
├── Pipfile             # Python dependencies
├── Pipfile.lock        # Locked dependencies
├── README.md           # Project documentation
└── server.py           # Entry point for production using Waitress

```

## 🧰 Installation & Setup

1. **Clone the Repository**:

   ```bash
   git clone https://github.com/obatabba/Social.git
   cd Social
   ```

2. **Set Up Virtual Environment**:

   ```bash
   pip install pipenv      # Install pipenv tool (if not installed already)
   pipenv install          # Install project dependencies
   ```

## 🖥️ Development Setup

### 1. Apply Migrations

```bash
python manage.py migrate
```

### 2. Create a Superuser (Optional)

```bash
python manage.py createsuperuser
```

### 3. Run the Development Server

```bash
python manage.py runserver
```

Access the app at: [http://127.0.0.1:8000](http://127.0.0.1:8000)

## 🌐 Production Deployment

### 1. Required Environment Variables

Make sure the following environment variables are set:

* `DJANGO_SETTINGS_MODULE` — Settings module to use (set to: `social.settings.prod`. default: `social.settings.dev`)
* `DATABASE_URL` — PostgreSQL connection string (e.g., from Supabase)
* `CLOUDINARY_URL` — Cloudinary credentials for media storage. You must [create a Cloudinary account](https://cloudinary.com/users/register/free) to obtain this.
* `SECRET_KEY` — Django secret key
* `ALLOWED_HOSTS` — Comma-separated list of allowed domains (e.g., `social-mhtn.onrender.com,somedomain.com`)
* `HOST_URL` — Full base URL (with `https://`), used for CSRF, CORS, etc. (e.g., `https://social-mhtn.onrender.com`)
* `PORT_NUMBER` — Port used by `server.py` in production (default: `8000`)

> These can typically be configured in your hosting platform’s dashboard (e.g., Render).

### 2. Apply Migrations

```bash
python manage.py migrate
```

### 3. Collect Static Files

```bash
python manage.py collectstatic --noinput
```

This gathers static assets (CSS, JS, etc.) into the `staticfiles/` directory for serving in production.

### 4. Start the Production Server

```bash
python server.py
```
This project uses Waitress as a production server (cross-platform and Windows-compatible). Feel free to use any production-ready WSGI server like Gunicorn.

## 📄 License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## 🤝 Contributing

Contributions are welcome! Please fork the repository and submit a pull request for any enhancements or bug fixes.

## 📬 Contact

For inquiries or feedback, please contact [obatabba](mailto:obatabba@gmail.com).
