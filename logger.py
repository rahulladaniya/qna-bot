import logging
import os

class Logger:
    def __init__(self):
        pass

    @staticmethod
    def get_logger(name: str):
        logger = logging.getLogger(name)
        if not logger.hasHandlers():
            logger.setLevel(logging.INFO)

            # Ensure the logs directory exists
            os.makedirs('logs', exist_ok=True)

            # Console handler
            ch = logging.StreamHandler()
            ch.setLevel(logging.INFO)

            # File handler
            fh = logging.FileHandler('logs/project.log', encoding='utf-8')
            fh.setLevel(logging.INFO)

            # Formatter with filename, function, and logger name
            formatter = logging.Formatter(
                '[%(asctime)s - %(filename)s - %(name)s - %(funcName)s - %(levelname)s] %(message)s'
            )
            ch.setFormatter(formatter)
            fh.setFormatter(formatter)

            # Add handlers
            logger.addHandler(ch)
            logger.addHandler(fh)

        return logger
