"""
Demonstrate logging from modules
"""
import logging
logger = logging.getLogger(__name__)
# logger.setLevel(logging.DEBUG)

def banana():
    logger.warning("bravo")
    logger.info("Barbarella")
    logger.error("broccoli")
    logger.debug("banana()")
