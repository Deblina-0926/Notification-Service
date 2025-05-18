from flask import Flask
from api.routes import notification_routes


app = Flask(__name__)
app.register_blueprint(notification_routes)

@app.route("/")
def home():
    return "🚀 Notification Service is running!"

if __name__ == "__main__":
    app.run(debug=True)
