# ♯ Music Catalogue

![Python](https://img.shields.io/badge/Python-%23007ACC.svg?style=for-the-badge&logo=python&logoColor=white)
![Django](https://img.shields.io/badge/Django-%23092E20.svg?style=for-the-badge&logo=django&logoColor=white)
![MySQL](https://img.shields.io/badge/MySQL-%234479A1.svg?style=for-the-badge&logo=mysql&logoColor=white)
![Apache](https://img.shields.io/badge/Apache-D22128?style=for-the-badge&logo=apache&logoColor=white)

> BCDE215 - Web Development
>
> Music Catalogue is a web-based catalogue management app built with **Django** and **MySQL**, developed as part of the **BCDE215 - Web Development** course at Ara Institute of Canterbury. It allows users to browse a collection of music albums and songs, while providing administrators with full CRUD control over the catalogue.

🔗 **Live Demo:** *(link to be added)*
&nbsp;·&nbsp;
📖 **[Wiki — Full Documentation](../../wiki)**

---

## ✨ Core Features

**Public browsing**
- View all albums and their associated songs
- Browse by artist, genre, or release year

**Admin Panel (login required)**
- Secure admin login via Django's built-in authentication
- **Create** new albums and songs
- **Read** — browse and search the full catalogue
- **Update** existing album and song details (title, artist, year, cover art, track listing, etc.)
- **Delete** albums or individual songs from the catalogue
- Manage collections — group albums into curated sets

> See the [Wiki](../../wiki) for full admin usage instructions and data model details.

---

## Snapshots

<table>
  <tr>
    <td align="center"><strong>Home — Album Catalogue</strong></td>
    <td align="center"><strong>Album Detail & Track Listing</strong></td>
  </tr>
  <tr>
    <td><img src="docs/snapshots/home.png" alt="Home page" width="420"/></td>
    <td><img src="docs/snapshots/album-detail.png" alt="Album detail" width="420"/></td>
  </tr>
  <tr>
    <td align="center"><strong>Admin — Manage Albums</strong></td>
    <td align="center"><strong>Admin — Edit Song</strong></td>
  </tr>
  <tr>
    <td><img src="docs/snapshots/admin-albums.png" alt="Admin albums" width="420"/></td>
    <td><img src="docs/snapshots/admin-edit-song.png" alt="Admin edit song" width="420"/></td>
  </tr>
</table>

> Add your screenshots to `docs/snapshots/` and update the filenames above.

---

## Project Structure

```
music-catalogue/
├── catalogue/              # Main Django app
│   ├── migrations/         # Database migrations
│   ├── templates/          # HTML templates
│   ├── static/             # CSS, JS, images
│   ├── models.py           # Album & Song data models
│   ├── views.py            # Page logic and CRUD handlers
│   ├── urls.py             # App URL routing
│   └── admin.py            # Admin panel config
├── music_catalogue/        # Django project config
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── docs/
│   └── snapshots/          # README screenshots
├── requirements.txt
└── manage.py
```

---

## Getting Started

### Prerequisites

- Python 3.10+
- MySQL 8.0+
- pip
- (Optional) virtualenv or venv

### Installation

```bash
# 1. Clone the repository
git clone https://github.com/arseniedev/music-catalogue.git
cd music-catalogue

# 2. Create and activate a virtual environment
python -m venv venv
source venv/bin/activate        # macOS / Linux
venv\Scripts\activate           # Windows

# 3. Install dependencies
pip install -r requirements.txt
```

### Database Setup

```sql
-- Run in your MySQL client
CREATE DATABASE music_catalogue CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
CREATE USER 'catalogue_user'@'localhost' IDENTIFIED BY 'your_password';
GRANT ALL PRIVILEGES ON music_catalogue.* TO 'catalogue_user'@'localhost';
FLUSH PRIVILEGES;
```

Then update `music_catalogue/settings.py` with your database credentials:

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'music_catalogue',
        'USER': 'catalogue_user',
        'PASSWORD': 'your_password',
        'HOST': 'localhost',
        'PORT': '3306',
    }
}
```

### Run Migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

### Create an Admin Account

```bash
python manage.py createsuperuser
# Follow the prompts to set your own username, email, and password.
# These credentials are yours — do not share or commit them.
```

### Run the App

```bash
python manage.py runserver
```

Then open **[http://127.0.0.1:8000](http://127.0.0.1:8000)** in your browser.
Admin panel is at **[http://127.0.0.1:8000/admin](http://127.0.0.1:8000/admin)**.

---

## 🔮 Future Improvements

- Search and filter by genre, artist, or year
- User accounts with personalised playlists
- Album cover image uploads
- REST API endpoint for external integrations
- Spotify / MusicBrainz metadata auto-fill

</br>

---

</br>

> ![IMPORTANT_NOTICE-_Academic_Integrity](https://img.shields.io/badge/IMPORTANT_NOTICE-_Academic_Integrity-%23800000.svg?style=for-the-badge&logoColor=white)
>
> #### **BCDE215 - Web Development**
>
> This portfolio contains original work completed as part of my BCDE215 - Web Development course at Ara Institute of Canterbury. I do not condone plagiarism or academic misconduct in any form. This project is for academic purposes only and is not intended to be copied or used without proper authorisation.
> The university has a <span style="color:brown;">**STRICT**</span> policy on academic misconduct, and I fully support this policy. Any attempt to plagiarize, copy, or use this work as your own will result in serious consequences. Please respect academic integrity and do not attempt to pass off this work as your own.
>
> #### **Disclaimer**
>
> All the content presented here is the result of my own individual work, and any resemblance to other works is purely coincidental. If you are a student, please refrain from using or copying this work in any way that violates the principles of academic honesty and integrity.

---

Created by Arsenie — 2024