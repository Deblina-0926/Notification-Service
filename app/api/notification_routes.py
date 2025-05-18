from flask import Blueprint, request, jsonify
from utils.rabbitmq_publisher import publish_notification

notification_routes = Blueprint('notification_routes', __name__)

# POST /notifications
@notification_routes.route('/notifications', methods=['POST'])
def send_notification():
    data = request.get_json()

    # Simple validation example
    if not data or 'user_id' not in data or 'message' not in data or 'type' not in data:
        return jsonify({'error': 'Missing required fields'}), 400

    # Publish notification to RabbitMQ queue
    publish_notification(data)

    return jsonify({
        "status": "Notification queued",
        "data": data
    }), 200

# GET /users/<id>/notifications (you can add a dummy response or connect to DB here)
@notification_routes.route('/users/<user_id>/notifications', methods=['GET'])
def get_user_notifications(user_id):
    # For now, just a placeholder response
    notifications = [
        {"user_id": user_id, "message": "Test email notification", "type": "email"},
        {"user_id": user_id, "message": "Test SMS notification", "type": "sms"},
        {"user_id": user_id, "message": "Test in-app notification", "type": "in-app"}
    ]
    return jsonify(notifications), 200
