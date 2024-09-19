import logging, sys
from flask import Flask, jsonify, request
import structlog

# Set up file logging
logging.basicConfig(level=logging.INFO,
                    stream=sys.stdout,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')

# Set up structlog to use both console and file logging
structlog.configure(
    processors=[
        structlog.stdlib.add_log_level,
        structlog.stdlib.add_logger_name,
        structlog.processors.TimeStamper(fmt="iso"),
        structlog.stdlib.ProcessorFormatter.wrap_for_formatter,
    ],
    logger_factory=structlog.stdlib.LoggerFactory(),
    wrapper_class=structlog.stdlib.BoundLogger,
    cache_logger_on_first_use=True,
)

logger = structlog.get_logger()

app = Flask(__name__)

@app.route('/login', methods=['POST'])
def login():
    user_data = request.json
    logger.info("User login attempt", service="user_service", username=user_data.get('username'))
    logging.info(f"User login attempt for username: {user_data.get('username')}")
    # Simulate authentication
    return jsonify({"status": "Login successful"})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5003)