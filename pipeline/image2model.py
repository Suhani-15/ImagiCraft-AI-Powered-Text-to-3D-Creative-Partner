import os
import uuid

def image_to_3d(image_path: str) -> str:
    os.makedirs("assets/models", exist_ok=True)
    filename = f"assets/models/{uuid.uuid4()}.glb"
    with open(filename, "wb") as f:
        f.write(b"This is a mock 3D model file.")
    return filename
