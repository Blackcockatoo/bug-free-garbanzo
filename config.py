
import os
from dotenv import load_dotenv
load_dotenv()

CENTURY_REAL_SEC  = float(os.getenv("CENTURY_REAL_SEC", 2592000))
BURST_CAP_PER_HOUR= float(os.getenv("BURST_CAP_PER_HOUR", 1.0))
STASIS_FILL_RATE  = float(os.getenv("STASIS_FILL_RATE", 0.15))
STASIS_MAX_HOURS  = int(os.getenv("STASIS_MAX_HOURS", 72))

VFS_PATH = os.getenv("VFS_PATH", "./vfs")
LOG_PATH = os.getenv("LOG_PATH", "./logs")
SKIN_MODE = os.getenv("SKIN_MODE", "BSS")
