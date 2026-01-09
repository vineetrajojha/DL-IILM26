from ultralytics import YOLO

def validate_model():
    model = YOLO('yolov8m.pt')

    print("Start:")
    metrics = model.val(data='coco8.yaml', device='mps')

    print("\nValidation Results:")
    print(f"map50-95: {metrics.box.map}")
    print(f"map50: {metrics.box.map50}")

if __name__ == "__main__":
    validate_model()
