import logging

def setup_logger(name="auto_apply_backend"):
    # Create logger
    logger = logging.getLogger(name)
    # TODO: Setup your log handler here
    return logger

# Create default logger instance
logger = setup_logger()

