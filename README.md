
<div align="center">

# 🍽️ Restaurant Management Website

### A Dynamic Restaurant Website Built with Python & Django

<p>
  <img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python"/>
  <img src="https://img.shields.io/badge/Django-092E20?style=for-the-badge&logo=django&logoColor=white" alt="Django"/>
  <img src="https://img.shields.io/badge/HTML5-E34F26?style=for-the-badge&logo=html5&logoColor=white" alt="HTML5"/>
  <img src="https://img.shields.io/badge/Database-SQLite-003B57?style=for-the-badge&logo=sqlite&logoColor=white" alt="SQLite"/>
</p>

<p>
  A restaurant website designed to display food menus, organize categories,
  collect customer feedback, and handle table reservations.
</p>

</div>

---

## 📌 About the Project

The **Restaurant Management Website** is a web development project built using Python and Django. The main goal of this project is to create a dynamic restaurant website where content can be managed through database models instead of being hardcoded into HTML pages.

This project helped me gain practical experience with Django models, database relationships, views, templates, form handling, and media management.

## ✨ Features

- 🏠 **Dynamic Homepage** — Displays menu items, food categories, and customer reviews.
- 🍕 **Food Menu** — Displays restaurant items and their details.
- 🗂️ **Category Management** — Organizes food items into categories.
- 🖼️ **Food Images** — Supports images for restaurant menu items.
- ℹ️ **About Us Page** — Displays restaurant information.
- ⭐ **Customer Feedback** — Stores customer names, reviews, ratings, and optional images.
- 📅 **Table Reservation** — Accepts customer details and table-booking requests.
- 🗄️ **Database Integration** — Uses Django ORM to retrieve and store application data.

## 🛠️ Technologies Used

| Technology | Purpose |
|---|---|
| Python | Backend programming |
| Django | Web framework |
| Django ORM | Database operations |
| HTML5 | Page structure |
| CSS3 | Styling |
| SQLite | Database, if configured as the default |
| Git & GitHub | Version control and project hosting |

## 📚 What I Learned

### 1. Django Models & ORM
Learned how to define database models for menu items, categories, restaurant information, feedback, and table reservations.

### 2. Foreign Key Relationships
Used Django's `ForeignKey` field to connect food items with their respective categories.

### 3. Views & Templates
Learned how to retrieve records using Django ORM and pass data to HTML templates through context dictionaries.

### 4. Form Handling
Practiced handling HTTP POST requests and saving table reservation information to the database.

### 5. Media Management
Worked with Django's `ImageField` to store image references for menu items and customer feedback.

### 6. Git & GitHub
Learned to organize project files, manage Python dependencies, and prepare a `.gitignore` file before publishing a project.

## 🧩 Challenges & Solutions

| Challenge | What I Learned |
|---|---|
| Managing related data | Connected menu items and categories using foreign keys. |
| Handling booking forms | Practiced reading POST data and checking submitted values. |
| Displaying dynamic content | Used Django ORM queries and template context variables. |
| Organizing project files | Used a structured Django layout and prepared dependency and ignore files. |

## ⚙️ Getting Started

Follow these steps to run the project locally.

### Prerequisites

- Python installed
- pip package manager
- Git (optional)

### 1. Clone the Repository

```bash
git clone YOUR_GITHUB_REPOSITORY_URL
```

### 2. Navigate to the Project Directory

```bash
cd Restaurant_Project
```

### 3. Create a Virtual Environment

```bash
python -m venv venv
```

### 4. Activate the Virtual Environment

**Windows:**

```bash
venv\Scripts\activate
```

**macOS / Linux:**

```bash
source venv/bin/activate
```

### 5. Install Dependencies

If `requirements.txt` is available:

```bash
pip install -r requirements.txt
```

Otherwise, install Django and the image-processing dependency used by `ImageField`:

```bash
pip install django Pillow
```

### 6. Apply Database Migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

### 7. Run the Development Server

```bash
python manage.py runserver
```

Open your browser and visit:

**http://127.0.0.1:8000/**

## 📂 Project Structure

```text
Restaurant_Project/
│
├── Base_App/
│   ├── migrations/
│   ├── models.py
│   ├── views.py
│   ├── admin.py
│   └── apps.py
│
├── Restaurant_Project/
│   ├── settings.py
│   ├── urls.py
│   ├── asgi.py
│   └── wsgi.py
│
├── Static/
├── Template/
├── manage.py
├── requirements.txt
├── .gitignore
└── README.md
```

*Note: The directory structure above is illustrative. Adjust folder names to match your actual project.*

## 🚀 Future Improvements

- [ ] Improve form validation and error messages.
- [ ] Add booking confirmation and cancellation.
- [ ] Prevent duplicate table reservations.
- [ ] Improve responsive design for mobile devices.
- [ ] Add search and filtering for menu items.
- [ ] Improve image upload and media configuration.
- [ ] Add automated tests and stronger input validation.
- [ ] Improve security and prepare for production deployment.

## 🎯 Project Goals

This project is part of my journey toward becoming a **Backend / Full-Stack Developer**. My goal is to build practical web applications, strengthen my problem-solving skills, and apply my knowledge to real-world requirements.

## 👨‍💻 Developer

<div align="center">

### Saachin Kunwar

**Aspiring Backend / Full-Stack Developer**

Passionate about Python, Django, APIs, databases, and building practical software solutions.

<p>
  <a href="https://github.com/Saachin-Kunwar">
    <img src="https://img.shields.io/badge/GitHub-181717?style=for-the-badge&logo=github&logoColor=white" alt="GitHub"/>
  </a>
</p>

</div>

---

<div align="center">

**⭐ If you find this project interesting, consider giving it a star!**

*Learning by building. Improving by solving problems.*

</div>
