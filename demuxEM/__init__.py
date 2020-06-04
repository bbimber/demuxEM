import sys
import logging

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
ch = logging.StreamHandler(sys.stdout)
ch.setLevel(logging.INFO)
formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
ch.setFormatter(formatter)
logger.addHandler(ch)

from .tools import *

from importlib_metadata import version, PackageNotFoundError

try:
    __version__ = version(__name__)
    del version
except PackagteNotFoundError:
    pass
