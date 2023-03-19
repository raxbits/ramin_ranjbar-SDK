#todo: use this while app runs in prod

import logging

logger = logging.getLogger("lotr-sdk")

console_handler = logging.StreamHandler()
console_handler.setLevel(logging.DEBUG)

logger.addHandler(console_handler)
logger.setLevel(logging.WARNING)

# Logging Lvl handlers
def log_warning():
    logger.setLevel(logging.WARNING)


def log_error():
    logger.setLevel(logging.ERROR)


def log_critical():
    logger.setLevel(logging.CRITICAL)

def log_debug():
    logger.setLevel(logging.DEBUG)


def log_info():
    logger.setLevel(logging.INFO)
