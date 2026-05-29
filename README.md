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

> See the [Wiki](https://github.com/arseniedev/music-catalogue/wiki) for full admin usage instructions and data model details.

---

## Snapshots

<details>
  <summary>Iteration 1</summary>
  <table>
    <tr align="center">
      <td>Homepage</td>
      <td>Album Home</td>
      <td>Artist Home</td>
    </tr>
    <tr align="center">
      <td><img src="docs/snapshots/iteration-1/home.png" alt="Home page" width="420"/></td>
      <td><img src="docs/snapshots/iteration-1/album-home.png" alt="Home page" width="420"/></td>
      <td><img src="docs/snapshots/iteration-1/artist-home.png" alt="Home page" width="420"/></td>
    </tr>
    <tr>
    <tr align="center">
      <td>Admin Sign In</td>
      <td>Edit Album Details</td>
      <td>Edit Artist Details</td>
    </tr>
    <tr align="center">
      <td>
        <img src="docs/snapshots/iteration-1/admin-signin.png" alt="Home page" width="420"/>
      </td>
      <td>
        <img src="docs/snapshots/iteration-1/edit-album.png" alt="Edit Artist Details" width="420"/>
      </td>
      <td>
        <img src="docs/snapshots/iteration-1/edit-artist.png" alt="Edit Album Details" width="420"/>
      </td>
    </tr>
  </table>
</details>

### Current Iteration
<table>
  <tr align="center">
    <td>Homepage</td>
    <td>Albums</td>
    <td>Artists</td>
  </tr>
  <tr align="center">
    <td><img src="docs/snapshots/iteration-2/01-home.png" alt="Home page" width="420"/></td>
    <td><img src="docs/snapshots/iteration-2/02-albums.png" alt="Albums page" width="420"/></td>
    <td><img src="docs/snapshots/iteration-2/03-artists.png" alt="Artists page" width="420"/></td>
  </tr>
  <tr>
  <tr align="center">
    <td>Admin Sign In</td>
    <td>Add Album</td>
    <td>Add Artist</td>
  </tr>
  <tr align="center">
    <td>
      <img src="docs/snapshots/iteration-2/04-admin.png" alt="Admin Page" width="420"/>
    </td>
    <td>
      <img src="docs/snapshots/iteration-2/05-add-artist.png" alt="Add Artist Details" width="420"/>
    </td>
    <td>
      <img src="docs/snapshots/iteration-2/06-add-album.png" alt="Add Album Details" width="420"/>
    </td>
  </tr>
  <tr align="center">
    <td>View Artist</td>
    <td>Edit Album</td>
    <td>View Album</td>
  </tr>
  <tr align="center">
    <td>
      <img src="docs/snapshots/iteration-2/07-view-artist-details.png" alt="View Artist Details" width="420"/>
    </td>
    <td>
      <img src="docs/snapshots/iteration-2/08-edit-album.png" alt="Edit Album" width="420"/>
    </td>
    <td>
      <img src="docs/snapshots/iteration-2/09-view-album-details.png" alt="View Album Details" width="420"/>
    </td>
  </tr>
  <tr align="center">
    <td>Delete Album</td>
    <td>-</td>
    <td>-</td>
  </tr>
  <tr align="center">
    <td>
      <img src="docs/snapshots/iteration-2/10-delete-album.png" alt="Delete Album" width="420"/>
    </td>
    <td>
      <img src="docs/snapshots/iteration-2/edit-album.png" alt="Empty" width="420"/>
    </td>
    <td>
      <img src="docs/snapshots/iteration-2/edit-artist.png" alt="Empty" width="420"/>
    </td>
  </tr>
</table>


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
