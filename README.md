# Notification Service

## Overview  
A simple notification service that sends Email, SMS, and In-App notifications asynchronously using RabbitMQ as a message broker.

---

## Features
- **POST /notifications**: Send notification requests (Email, SMS, In-App) which get queued to RabbitMQ.
- Worker service listens to RabbitMQ and processes notifications.
- Notifications are processed asynchronously.
- Basic retry can be added in the worker (not implemented by default).

---

## Project Structure

notification_service/
└── app/
├── main.py # Flask app entry point
├── publisher.py # Publishes notification messages to RabbitMQ
├── api/
│ └── routes.py # API endpoints for sending notifications
└── worker.py # Worker script listening and processing notification queue

yaml
## Setup Instructions

### Prerequisites  
- Python 3.7+ installed  
- RabbitMQ installed and running locally  
- pip for package management  

### Installation Steps

1. **Clone the repository**  
   ```bash
   git clone <your-repo-link>
   cd notification_service


2.Create and activate a Python virtual environment
python -m venv venv
# On Windows:
venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate

3.Install dependencies
pip install -r requirements.txt

4.Start RabbitMQ
Ensure RabbitMQ server is running locally on default port 5672.

5.Run the Flask app
Run from project root to allow proper imports:
python -m app.main
The API will be available at http://localhost:5000.

6.Run the worker (in a separate terminal)
python worker.py



Usage
Send a notification (POST)
URL: http://localhost:5000/notifications

Method: POST

Headers: Content-Type: application/json

Body example:
{
  "user_id": "123",
  "message": "Hello! This is a test notification.",
  "type": "email"
}
The notification will be queued and the worker will process it asynchronously.



Assumptions
RabbitMQ runs locally on default settings (localhost:5672).

No persistent database is used; notifications are processed but not stored.

Email, SMS, and in-app notifications are simulated by print statements in the worker.

Retry logic for failed notifications is not implemented but can be added.

No authentication or authorization is implemented for API endpoints.

vbnet
Copy
Edit


