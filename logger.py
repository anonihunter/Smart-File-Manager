import logging

# Configure the core logging settings
logging.basicConfig( 
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(funcName)s - %(message)s", 
    datefmt='%Y-%m-%d %H:%M:%S'
    )

# Create a named logger for this module
logger = logging.getLogger(__name__)