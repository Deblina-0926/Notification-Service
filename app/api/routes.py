from flask import Blueprint, request, jsonify
from publisher import publish_notification

notification_routes = Blueprint('notification_routes', __name__)

@notification_routes.route('/notifications', methods=['POST'])
def send_notification():
    data = request.json
    
    # Validate required fields:
    required_fields = ['user_id', 'message', 'type']
    if not all(field in data for field in required_fields):
        return jsonify({"error": "Missing required fields"}), 400
    
    # Publish notification to RabbitMQ
    publish_notification(data)
    
    return jsonify({"status": "Notification queued"}), 200
