import streamlit as st
import time
from transformers import T5Tokenizer, T5ForConditionalGeneration

st.set_page_config(
    page_title="Personalized Story Generator 📖",
    layout="wide"
)

st.title("Personalized Story Generator")
st.markdown("Enter some details and let a powerful language model craft a unique story for you!")

@st.cache_resource
def load_model():
    return T5Tokenizer.from_pretrained("google/flan-t5-large"), T5ForConditionalGeneration.from_pretrained("google/flan-t5-large")

tokenizer, model = load_model()

def clean_story(story):
    lines = story.split('\n')
    cleaned_lines = []
    for line in lines:
        if not line.startswith('—') and not line.startswith('--'):
            cleaned_lines.append(line)
    return '\n'.join(cleaned_lines).strip()

def generate_story(theme, character, location, genre):
    prompt = f"Generate a detailed short story. The story should be at least 30 lines long. The genre is {genre}. Theme: {theme}. Character: {character}. Location: {location}."
    input_ids = tokenizer(prompt, return_tensors="pt").input_ids
    outputs = model.generate(
        input_ids,
        max_length=950,
        min_length=500,
        num_beams=4,
        no_repeat_ngram_size=2
    )
    story = tokenizer.decode(outputs[0], skip_special_tokens=True)
    return clean_story(story)

with st.sidebar:
    st.header("Story Details")
    genre_options = ["Fantasy", "Sci-Fi", "Mystery", "Horror", "Comedy"]
    genre_input = st.selectbox("Genre:", options=genre_options)
    theme_input = st.text_input("Theme:", "adventure")
    character_input = st.text_input("Main Character:", "a brave knight")
    location_input = st.text_input("Location:", "a magical forest")
    generate_button = st.button("Generate Story", type="primary")

story_placeholder = st.empty()

if generate_button:
    if theme_input and character_input and location_input:
        start_time = time.time()
        with st.spinner("Crafting your story... ✍️"):
            patience_message_placeholder = st.empty()
            while time.time() - start_time < 60:
                time.sleep(1)
            if time.time() - start_time >= 60:
                patience_message_placeholder.info("Please be patient! The model is still generating the story. This may take a few moments longer.")
            generated_story = generate_story(theme_input, character_input, location_input, genre_input)
            patience_message_placeholder.empty()
            story_placeholder.success("Story Generated!")
            st.write(generated_story)
    else:
        st.warning("Please fill out all the fields to generate a story.")