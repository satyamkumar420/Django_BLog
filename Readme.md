# 📝 Simple Blogging Platform

Welcome to the Simple Blogging Platform! This project allows users to create and manage blog posts, comment on posts, and manage their profiles. The platform includes user authentication, profile management, and a comment system.

## 🚀 Features

- **User Authentication**:

  - User registration with a username, email, and password.
  - Secure login for existing users.
  - Logout feature to sign out of the account.

- **User Profile**:

  - View and update personal information (username, email, bio).
  - Edit profile functionality.

- **Post Management**:

  - Create, edit, and delete blog posts.
  - Authorization checks to ensure users can only edit or delete their own posts.

- **Comment System**:
  - Authenticated users can comment on blog posts.
  - Comments are associated with the respective post and user.

## 🛠️ Installation

1. **Clone the repository**:

   ```bash
   git clone https://github.com/yourusername/simple-blogging-platform.git
   cd simple-blogging-platform
   ```

2. **Create a virtual environment**:

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install dependencies**:

   ```bash
   pip install -r requirements.txt
   ```

4. **Apply migrations**:

   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

5. **Run the development server**:

   ```bash
   python manage.py runserver
   ```

6. **Access the application**:
   Open your web browser and navigate to `http://127.0.0.1:8000`.

## 📂 Project Structure

```
simple-blogging-platform/
├── blog/
│   ├── migrations/
│   ├── templates/
│   │   ├── add_comment.html
│   │   ├── create_post.html
│   │   ├── delete_post.html
│   │   ├── edit_post.html
│   │   ├── home.html
│   │   ├── login.html
│   │   ├── profile.html
│   │   ├── register.html
│   │   ├── post_detail.html
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── forms.py
│   ├── models.py
│   ├── tests.py
│   ├── urls.py
│   ├── views.py
├── myblog/
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py
│   ├── urls.py
│   ├── wsgi.py
├── venv/
├── manage.py
├── requirements.txt
```
