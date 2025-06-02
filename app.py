import streamlit as st
from pipeline.llm import expand_prompt
from pipeline.text2image import generate_image
from pipeline.image2model import image_to_3d
from memory.store import save_to_memory

st.title("🎨 AI Creator: Prompt → Image → 3D Model")

user_prompt = st.text_input("Enter your creative prompt:")

if st.button("Generate"):
    with st.spinner("Expanding your idea..."):
        expanded_prompt = expand_prompt(user_prompt)

    with st.spinner("Generating image..."):
        image_path = generate_image(expanded_prompt)

    with st.spinner("Creating 3D model..."):
        model_path = image_to_3d(image_path)

    save_to_memory(user_prompt, model_path)

    st.success("All done!")
    st.image(image_path, caption="Generated Image")
    st.text(f"3D model saved at: {model_path}")
