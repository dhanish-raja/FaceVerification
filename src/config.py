from pathlib import Path

# ==========================================================
# Project Paths
# ==========================================================

PROJECT_ROOT = Path(__file__).resolve().parent.parent

LOG_DIR = PROJECT_ROOT / "logs"
LOG_FILE = LOG_DIR / "application.log"

# ==========================================================
# Face Verification Configuration
# ==========================================================

MODEL_NAME = "ArcFace"

DETECTOR_BACKEND = "retinaface"

DISTANCE_METRIC = "cosine"

ENFORCE_DETECTION = True

ANTI_SPOOFING = False

# ==========================================================
# Logger Configuration
# ==========================================================

LOG_LEVEL = "INFO"