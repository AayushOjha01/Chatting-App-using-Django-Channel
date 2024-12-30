# ChatApp

ChatApp is a real-time chat application built with Django and WebSockets. It allows users to send and receive messages instantly, creating an engaging communication platform. This README provides an overview of the project, its features, and instructions for setup and usage.

## Features

- **Real-time Communication:** Messages are sent and received instantly using WebSockets.
- **User Authentication:** Secure login and registration system.
- **Chat Rooms:** Users can create or join chat rooms.
- **Message History:** Persistent message storage for chat history.
- **Responsive Design:** Optimized for both desktop and mobile devices.

## Technology Stack

- **Backend:** Django, Django Channels
- **Frontend:** HTML, CSS, JavaScript
- **Database:** SQLite (default, configurable to PostgreSQL or other databases)
- **WebSocket Protocol:** Enables real-time messaging

## Prerequisites

- Python 3.10 or later
- Django 4.x
- Node.js and npm (for frontend dependencies, if applicable)

## Installation

1. **Clone the Repository**
   ```bash
   git clone https://github.com/your-username/chatapp.git
   cd chatapp
   ```

2. **Create a Virtual Environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Apply Migrations**
   ```bash
   python manage.py migrate
   ```

5. **Run the Development Server**
   ```bash
   python manage.py runserver
   ```

6. **Access the Application**
   Open your browser and navigate to `http://127.0.0.1:8000`.

## Usage

1. **Register an Account:** Create a new user account to start using ChatApp.
2. **Join or Create a Chat Room:** Access available chat rooms or create a new one.
3. **Start Chatting:** Send and receive messages in real-time.

## Configuration

- **Database:** Modify the `DATABASES` setting in `settings.py` to use a different database.
- **WebSocket Settings:** Configure `ASGI_APPLICATION` and `CHANNEL_LAYERS` for WebSocket support.

## Contributing

Contributions are welcome! Please follow these steps:

1. Fork the repository.
2. Create a new branch for your feature or bug fix.
3. Commit your changes and push to your fork.
4. Submit a pull request for review.

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.

## Acknowledgments

- Django and Django Channels documentation
- Open-source libraries and tools used in this project


