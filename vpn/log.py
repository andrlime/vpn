import logging


class ColoredFormatter(logging.Formatter):
    @staticmethod
    def color_of_loglevel(level: int) -> str:
        match level:
            case logging.DEBUG:
                return "\033[2m"
            case logging.INFO:
                return "\033[36m"
            case logging.WARNING:
                return "\033[33m"
            case logging.ERROR:
                return "\033[31m"
            case logging.CRITICAL:
                return "\033[1;31m"
            case _:
                return ""

    @staticmethod
    def reset_color() -> str:
        return "\033[0m"

    def format(self, record: logging.LogRecord) -> str:
        color = self.color_of_loglevel(record.levelno)
        return f"{color}{super().format(record)}{self.reset_color()}"


def get_logger(name: str) -> logging.Logger:
    logger = logging.getLogger(name)
    if not logger.handlers:
        handler = logging.StreamHandler()
        handler.setFormatter(
            ColoredFormatter("%(asctime)s [%(levelname)-8s] %(name)s: %(message)s")
        )
        logger.addHandler(handler)
        logger.setLevel(logging.DEBUG)
    return logger
