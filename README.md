# Kolam Design Analyzer 🎨✨

**A Digital Platform for Mathematical & Traditional Art**

## 📖 Overview
The **Kolam Design Analyzer** is an interactive web application that bridges the gap between traditional Indian art (Kolam) and modern technology. It allows users to create, analyze, and explore Kolam patterns using a digital interface. The platform features an AI-powered design assistant, a gallery of traditional patterns, and educational stories about the cultural significance of Kolams.

## ✨ Key Features

### 1. 🎨 Interactive Kolam Creator
- **3-Column Studio Layout**: Intuitive dashboard with controls, canvas, and reference panel.
- **Drawing Tools**: Brush, Eraser, Line, and specialized symmetries (2-fold, 4-fold, 8-fold).
- **Grid System**: Adjustable dot grids (4x4 to 15x15) to guide pattern creation.
- **Background Reference**: Upload reference images with adjustable opacity to trace or take inspiration from.
- **Save & Share**: Save designs locally or upload them to the cloud.

### 2. 🖼️ Pattern Gallery
- Explore a curated collection of traditional patterns (Pulli Kolam, Kambi Kolam, etc.).
- "Try this Design" feature loads gallery patterns directly into the editor.

### 3. 📚 Kolam Tales (Stories)
- Read culturally rich stories about Kolam traditions.
- **Bilingual Support**: Toggle between English and Hindi text.
- **Audio Narration**: Listen to stories using built-in text-to-speech with playback controls.

### 4. 🔐 User Authentication
- Secure Login and Signup via Firebase Authentication.
- User Profiles to manage personal settings and saved designs.

## 🛠️ Tech Stack

- **Frontend**: HTML5, CSS3, JavaScript (ES6+)
- **Backend Framework**: Django (Python)
- **Database/Auth**: Firebase (Authentication, Firestore), SQLite (Django Default)
- **Cloud Storage**: Cloudinary (Image Hosting)
- **Styling**: Vanilla CSS (Linear Gradients, Glassmorphism, Responsive Design)

## 🚀 Setup Instructions

1.  **Clone the Repository**
    ```bash
    git clone <repository-url>
    cd <repository-directory>
    ```

2.  **Create a Virtual Environment**
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows: venv\Scripts\activate
    ```

3.  **Install Dependencies**
    ```bash
    pip install django
    ```

4.  **Run Migrations**
    ```bash
    cd kolam_backend
    python manage.py migrate
    ```

5.  **Start the Server**
    ```bash
    python manage.py runserver
    ```

6.  **Access the App**
    Open your browser and navigate to `http://127.0.0.1:8000/`.

## 📂 Project Structure

project_root/
├── README.md
├── kolam_backend/          # Django Project Root
│   ├── core/               # Django App (Views, URLs)
│   ├── front_end/          # Frontend Assets
│   │   ├── static/         # CSS, JS, Images
│   │   └── templates/      # HTML Templates
│   ├── kolam/              # Project Configuration
│   ├── db.sqlite3          # Database
│   └── manage.py           # Django Management Script

---
*Created with ❤️ for the love of Art & Math.*
