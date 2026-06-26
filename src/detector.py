#detect face, crop face, align face

from deepface import DeepFace

from src.config import DETECTOR_BACKEND
from src.logger import get_logger

logger = get_logger(__name__)


def detect_face(image_path: str):
    """
    Detects and extracts the largest face from an image.

    Parameters
    ----------
    image_path : str

    Returns
    -------
    dict
        DeepFace face dictionary
    """

    logger.info("Detecting face: %s", image_path)

    faces = DeepFace.extract_faces(
        img_path=image_path,
        detector_backend=DETECTOR_BACKEND,
        enforce_detection=True,
        align=True,
    )

    logger.info("%d face(s) detected.", len(faces))

    return faces[0]