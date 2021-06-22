import logging

def configure_logger(LOGGER):
    """
    Configure custom logger for application
    """
    LOGGER.setLevel(logging.DEBUG)
    ch = logging.StreamHandler()
    ch.setLevel(logging.DEBUG)
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    ch.setFormatter(formatter)
    LOGGER.addHandler(ch)
    return LOGGER

def get_logger(name):
    """
    Return instance of custom logger.
    """
    LOGGER =  logging.getLogger(name)
    configure_logger(LOGGER)
    return LOGGER

