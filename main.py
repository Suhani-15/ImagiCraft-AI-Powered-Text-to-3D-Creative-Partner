
from pipeline.llm import expand_prompt
from pipeline.text2image import generate_image
from pipeline.image2model import image_to_3d
from memory.store import save_to_memory

prompt = input("🎨 Enter your idea: ")

creative_prompt = expand_prompt(prompt)
image_path = generate_image(creative_prompt)
model_path = image_to_3d(image_path)
save_to_memory(prompt, model_path)

print(f"✅ Done! 3D model saved at {model_path}")
