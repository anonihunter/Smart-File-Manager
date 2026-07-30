from config import config
import logging

log_config = config["logging"]

if log_config["enabled"]:

    level = getattr(logging, log_config["level"].upper(), logging.INFO)

    logging.basicConfig(
        filename=log_config["filename"],
        level=level,
        format="%(asctime)s - %(levelname)s - %(funcName)s - %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S"
    )

logger = logging.getLogger(__name__)