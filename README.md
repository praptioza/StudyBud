# StudyBuddy

StudyBuddy is a web application designed to help users find study partners, create study rooms, and chat with participants in real-time. Built with Python, Django, and SQLite3, StudyBuddy offers a range of features to enhance the collaborative study experience.

## Features

- **User Registration and Login**: New users can register and existing users can log in to their accounts.
- **User Profile Management**: Users can edit their profiles.
- **Study Rooms**: Users can create, join, and chat in study rooms.
- **Chat Functionality**: Real-time chat within study rooms.
- **Activity Feed**: Displays recent activities of different users.
- **Topics Panel**: Lists topics with the number of rooms under each topic.
- **Search**: Allows users to search for rooms and topics.
- **Admin Panel**: Full-featured admin panel for managing the site.
- **CRUD Operations**: Create, Read, Update, Delete operations for study rooms and messages.
- **Flash Messages**: Feedback to users for actions performed.
- **User Logout**: Users can securely log out of their accounts.
- **Restricted Pages**: Access control for sensitive pages.
- **Static Files Management**: Efficient handling of static files.
- **Theme Installation**: Customizable theme for the application.
- **Mobile Responsiveness**: Ensures usability on mobile devices.
- **Custom User Model**: Integration and customization of the user model.

## Installation

### Prerequisites

- Python 3.8+
- Django 3.0+
- SQLite3

### Steps

1. Clone the repository:

    ```sh
    git clone https://github.com/your-username/studybuddy.git
    cd studybuddy
    ```

2. Create a virtual environment:

    ```sh
    python -m venv env
    source env/bin/activate  # On Windows use `env\Scripts\activate`
    ```

3. Install dependencies:

    ```sh
    pip install -r requirements.txt
    ```

4. Apply migrations:

    ```sh
    python manage.py migrate
    ```

5. Create a superuser:

    ```sh
    python manage.py createsuperuser
    ```

6. Run the development server:

    ```sh
    python manage.py runserver
    ```

7. Access the application at `http://127.0.0.1:8000`

## Usage

### User Registration and Login

- Register a new account or log in with existing credentials.
- Edit your profile information from the profile page.

### Study Rooms

- Create new study rooms and invite participants.
- Join existing study rooms and engage in real-time chat.
- Search for rooms and topics using the search functionality.

### Admin Panel

- Access the admin panel at `http://127.0.0.1:8000/admin`.
- Manage users, rooms, and messages through the admin interface.

## API Endpoints

StudyBuddy uses Django REST Framework to provide API endpoints for various operations. For detailed API documentation, refer to the [API Docs](http://127.0.0.1:8000/api/docs).

## Acknowledgements

- [Django](https://www.djangoproject.com/)
- [Django REST Framework](https://www.django-rest-framework.org/)



