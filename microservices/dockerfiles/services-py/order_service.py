import logging, sys
from flask import Flask, jsonify, request
import structlog

# Set up  logging
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

@app.route('/order', methods=['POST'])
def create_order():
    order_data = request.json
    logger.info("Processing order", service="order_service", order_id=order_data.get('id'))
    logging.info(f"Processing order with ID: {order_data.get('id')}")
    # Simulate order processing
    return jsonify({"status": "Order processed successfully"})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5002)