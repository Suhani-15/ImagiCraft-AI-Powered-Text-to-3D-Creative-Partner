import torch
from diffusers import StableDiffusionPipeline
import uuid
import os

model_id = "runwayml/stable-diffusion-v1-5"
pipe = StableDiffusionPipeline.from_pretrained(model_id)
pipe.to("cuda" if torch.cuda.is_available() else "cpu")

def generate_image(prompt: str) -> str:
    image = pipe(prompt).images[0]
    os.makedirs("assets/images", exist_ok=True)
    filename = f"assets/images/{uuid.uuid4()}.png"
    image.save(filename)
    return filename
