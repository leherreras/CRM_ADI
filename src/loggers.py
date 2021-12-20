import logging
import sys


def initialize_logger(root):
    """
    Initialize logger level logging config
    :return:
    """
    formatter = logging.Formatter('%(asctime)s - %(name)s/%(processName)s - %(levelname)s - %(message)s')

    if root.handlers:
        root_handler = root.handlers[0]
    else:
        root_handler = logging.StreamHandler(sys.stderr)

    log_level = logging.INFO
    root_handler.setLevel(log_level)

    root.setLevel(log_level)
    root_handler.setFormatter(formatter)
    root.info(f"Logger initialized with level {log_level}")
    return root


def initialize_logging():
    """
    Initialize root level logging config
    :return:
    """
    root = logging.getLogger()
    initialize_logger(root)
