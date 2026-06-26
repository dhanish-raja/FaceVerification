from src.logger import get_logger
from src.verifier import verify_faces

logger = get_logger(__name__)


def main():

    logger.info("Application started.")

    image1 = "images/input/person1.jpeg"
    image2 = "images/input/person2.jpg"

    result = verify_faces(image1, image2)

    logger.info("Verification successful.")

    print("\n========== RESULT ==========")
    print(f"Verified       : {result['verified']}")
    print(f"Distance       : {result['distance']:.6f}")
    print(f"Threshold      : {result['threshold']:.2f}")
    print(f"Confidence     : {result['confidence']:.2f}%")
    print(f"Model          : {result['model']}")
    print(f"Detector       : {result['detector_backend']}")
    print(f"Metric         : {result['similarity_metric']}")
    print(f"Execution Time : {result['time']:.2f} sec")
    print("============================")

    logger.info("Application finished.")


if __name__ == "__main__":
    main()