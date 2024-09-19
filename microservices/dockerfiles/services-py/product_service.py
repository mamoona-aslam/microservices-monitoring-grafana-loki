import logging, sys
from flask import Flask, jsonify
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

@app.route('/products')
def get_products():
    logger.info("Fetching products", service="product_service")
    logging.info("Fetching products")
    # Simulate product list
    products = [{"id": 1, "name": "Product 1"}, {"id": 2, "name": "Product 2"}]
    return jsonify(products)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)