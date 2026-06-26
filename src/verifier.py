# detector -> embedder -> similarity -> decision

from deepface import DeepFace

from src.config import (
    MODEL_NAME,
    DETECTOR_BACKEND,
    DISTANCE_METRIC,
    ENFORCE_DETECTION,
)

from src.logger import get_logger

logger = get_logger(__name__)


def verify_faces(image1: str, image2: str) -> dict:
    """
    Verifies whether two images belong to the same person.
    """

    logger.info("Face verification started.")

    result = DeepFace.verify(
        img1_path=image1,
        img2_path=image2,
        model_name=MODEL_NAME,
        detector_backend=DETECTOR_BACKEND,
        distance_metric=DISTANCE_METRIC,
        enforce_detection=ENFORCE_DETECTION,
    )

    logger.info("Face verification completed successfully.")

    return result