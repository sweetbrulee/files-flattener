import logging
import colorlog


class Logger:
    def __init__(self, name=__name__):
        self._logger_impl = logging.getLogger(name)
        self._logger_impl.setLevel(logging.DEBUG)

        # Add level SUCCESS
        logging.addLevelName(25, "SUCCESS")

        # Create console handler and set level to debug
        ch = logging.StreamHandler()
        ch.setLevel(logging.DEBUG)

        # Create formatter with colors
        formatter = colorlog.ColoredFormatter(
            "%(log_color)s%(message)s",
            log_colors={
                "DEBUG": "green",
                "INFO": "reset",
                "SUCCESS": "green",
                "WARNING": "yellow",
                "ERROR": "red",
                "CRITICAL": "bold_black,bg_red",
            },
        )

        # Add formatter to ch
        ch.setFormatter(formatter)

        # Add ch to logger
        self._logger_impl.addHandler(ch)

    def debug(self, message, *args, **kwargs):
        self._logger_impl.debug(message, *args, **kwargs)

    def info(self, message, *args, **kwargs):
        self._logger_impl.info(message, *args, **kwargs)

    def success(self, message, *args, **kwargs):
        self._logger_impl.log(25, message, *args, **kwargs)

    def warning(self, message, *args, **kwargs):
        self._logger_impl.warning(message, *args, **kwargs)

    def error(self, message, *args, **kwargs):
        self._logger_impl.error(message, *args, **kwargs)

    def critical(self, message, *args, **kwargs):
        self._logger_impl.critical(message, *args, **kwargs)


logger_instance = Logger()
