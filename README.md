# Django Product Catalog

A Django product catalog with ModelForm CRUD, detail views, and ORM queries backed by SQLite.

## Overview

Products are listed on the home page with links to individual detail pages. New products are created through a ModelForm that provides automatic validation. The `Thing` model stores all product data. Detail views look up products by name via a URL parameter, so each product gets a clean `/item/<name>/` URL.

## Requirements

- Python 3.10+
- Django 5.0

## Project Structure

```
project-2-django-product-catalog/
├── manage.py
├── pyproject.toml
├── poetry.lock
├── .gitignore
├── README.md
├── static/
│   └── styles.css
├── templates/
│   ├── home.html           # Product listing
│   ├── item.html           # Single product detail
│   ├── new_product.html    # Creation form
│   └── success.html        # Post-creation confirmation
└── django_project/
    ├── __init__.py
    ├── asgi.py
    ├── admin.py
    ├── forms.py            # ProductForm (ModelForm)
    ├── models.py           # Thing model
    ├── settings.py
    ├── urls.py
    ├── views.py            # Home, Item, NewProduct, Success CBVs
    ├── wsgi.py
    └── migrations/
        ├── __init__.py
        └── 0001_initial.py
```

## Usage

```bash
poetry install
python manage.py migrate
python manage.py runserver
```

Open `http://127.0.0.1:8000` in a browser.

## Key Files

| File | What it does |
|------|--------------|
| `manage.py` | Django project entry point |
| `django_project/models.py` | `Thing` model — name, manufacturer, cost, weight, image |
| `django_project/forms.py` | `ProductForm` ModelForm for validated product creation |
| `django_project/views.py` | CBVs: listing, detail lookup by name, form handling |
| `django_project/urls.py` | Routes including `/item/<name>/` pattern |
| `templates/` | Four page templates: list, detail, form, confirmation |

## Author

Biswajeet Sahoo

## License

MIT License
