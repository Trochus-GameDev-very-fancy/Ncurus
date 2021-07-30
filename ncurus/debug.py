
__all__ = ["debug"]

import logging


logger = logging.getLogger("Ncurus")
logger.setLevel(logging.DEBUG)

formatter = logging.Formatter("%(levelname)s :: %(message)s")
file_handler =  logging.FileHandler("debug.log")

file_handler.setFormatter(formatter)
logger.addHandler(file_handler)

# An alias to facilite import.
debug = logger.debug
