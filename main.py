from flask import Flask, request, jsonify
import logging
from flask_cors import CORS

app = Flask(__name__)


logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

# using a GET method
@app.route('/get-user/<user_id>')
def get_user(user_id):
    logging.info(f"Request received for user_id: {user_id}")
    user_data = {
        'user_id': user_id,
        'name': 'john patrick',
        'email': 'johnpatrick@gmail.com'
    }
    return jsonify(user_data)

@app.get("/health")
def health_check():
    logging.info("Health check endpoint called")
    return {"status": "ok", "message": "API is running"}

if __name__ == '__main__':
    app.run(debug=True)
