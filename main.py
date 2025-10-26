
from pathlib import Path
from tamaos.config import CENTURY_REAL_SEC, BURST_CAP_PER_HOUR, STASIS_FILL_RATE, STASIS_MAX_HOURS, VFS_PATH, LOG_PATH, SKIN_MODE

def ensure_dirs():
    Path(VFS_PATH).mkdir(parents=True, exist_ok=True)
    Path(LOG_PATH).mkdir(parents=True, exist_ok=True)

def banner():
    print("=== TamaOS Boot ===")
    print(f"VFS={VFS_PATH}  LOGS={LOG_PATH}  SKIN={SKIN_MODE}")
    print(f"CENTURY_REAL_SEC={CENTURY_REAL_SEC}, BURST_CAP_PER_HOUR={BURST_CAP_PER_HOUR}")
    print(f"STASIS_FILL_RATE={STASIS_FILL_RATE}, STASIS_MAX_HOURS={STASIS_MAX_HOURS}")
    print("OK.")

def main():
    ensure_dirs()
    banner()
    print("Stub OS ready. Replace with full kernel/devices.")

if __name__ == "__main__":
    main()
