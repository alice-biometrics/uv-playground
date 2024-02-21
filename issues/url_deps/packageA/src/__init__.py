import os

from .domain import *  # noqa: F403 F401
from .infrastructure import *  # noqa: F403 F401
from .petisco_v1 import *  # noqa: F403 F401

ROOT_PATH = os.path.abspath(os.path.dirname(__file__))

with open(f"{ROOT_PATH}/VERSION") as f:
    __version__ = f.read().rstrip()
