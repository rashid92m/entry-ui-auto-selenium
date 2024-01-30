from core.data_classes import Logger
import coloredlogs
import logging


def log() -> Logger:
    log = logging.getLogger("My Application")
    level = "info"
    fmt = "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
    datefmt = "%m/%d/%Y %I:%M:%S %p"
    args = {"fmt": fmt, "datefmt": datefmt}
    coloredlogs.install(level, **args)
    return log
