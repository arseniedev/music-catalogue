b# ♯ Music Catalogue

![Python](https://img.shields.io/badge/Python-%23007ACC.svg?style=for-the-badge&logo=python&logoColor=white)
![Django](https://img.shields.io/badge/Django-%23092E20.svg?style=for-the-badge&logo=django&logoColor=white)
![MySQL](https://img.shields.io/badge/MySQL-%234479A1.svg?style=for-the-badge&logo=mysql&logoColor=white)
![Apache](https://img.shields.io/badge/Apache-D22128?style=for-the-badge&logo=apache&logoColor=white)

> BCDE215 - Web Development
>
> Music Catalogue is a web-based catalogue management app built with **Django** and **MySQL**, developed as part of the **BCDE215 - Web Development** course at Ara Institute of Canterbury. It allows users to browse a collection of music albums and songs, while providing administrators with full CRUD control over the catalogue.

🔗 **Live Demo:** https://youtu.be/TuRtaHknz90
&nbsp;·&nbsp;
</br>
📖 **[Wiki — Full Local Setup Documentation](https://github.com/arseniedev/music-catalogue/wiki)**

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

> See the [Wiki](https://github.com/arseniedev/music-catalogue/wiki) for the iteration snapshots, full admin usage instructions, and data model details.

---

## Project Structure
<!-- START_STRUCTURE -->
```text
.
├── README.md
├── app
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── forms.py
│   ├── migrations
│   ├── models.py
│   ├── tests.py
│   ├── urls.py
│   └── views.py
├── docs
│   └── snapshots
├── manage.py
├── music_catalogue
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── requirements.txt
├── structure.txt
└── templates
    ├── albums
    ├── artists
    ├── base.html
    ├── homepage.html
    ├── nav.html
    └── registration

10 directories, 20 files
```
<!-- END_STRUCTURE -->
---

## Local Setup 
[See Wiki](https://github.com/arseniedev/music-catalogue/wiki) ⊿



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
