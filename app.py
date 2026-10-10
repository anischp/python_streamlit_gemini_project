import streamlit as st
from api_call import note_generator, audio_transcription, quiz_generator
from PIL import Image


st.title("Note Summary and Quiz Generator")
st.markdown("Upload upto 3 images to generate Note Summary and Quizes")
st.divider()

# Sidebar starts
with st.sidebar:
    # Header
    st.header("Controls")
    # Upload Images
    images = st.file_uploader(
        "Upload the images of your notes",
        type=['jpg', 'jpeg', 'png'],
        accept_multiple_files=True)
    if images:
        if len(images) > 3:
            st.error("Upload at max 3 images")
        else:
            st.subheader("Uploaded Images")
            col = st.columns(len(images))
            for i, img in enumerate(images):
                with col[i]:
                    st.image(Image.open(img))
        
        # Convert image to PIL Image
        pil_images = []
        for img in images:
            pil_img = Image.open(img)
            pil_images.append(pil_img)
    
    # Difficulty
    selected_option = st.selectbox(
        "Select difficulty of your quiz",
        ('Easy', 'Medium', 'Hard'), 
        index=None)
    if selected_option:
        st.write(f"Difficulty Level: {selected_option}")
    
    # Button
    button_clicked = st.button("Inintiate AI", type="primary")
    
# Sidebar ends

# Button Clicked
if button_clicked:
    # Check image uploaded or not
    if not images:
        st.error("You must upload at least 1 image")    
    # Check difficulty seleced or not
    elif not selected_option:
        st.error("You must select Quiz difficulty")
    else:
        # Notes
        with st.container(border=True):
            st.subheader("Your note", anchor=False)
            with st.spinner("AI is writting note for you ..."):
                note = note_generator(pil_images)
                st.markdown(note)
            
            
        # Audio
        with st.container(border=True):
            st.subheader("Audio Transcription", anchor=False)
            with st.spinner("AI is generating audio transcription ..."):
                # Replace '#' * ` from note
                remove_chars = str.maketrans({'#':'', '*':'', '`':''})
                audio_transcript = audio_transcription(note.translate(remove_chars))
                st.audio(audio_transcript)                    
                    
        # Quiz
        with st.container(border=True):
            st.subheader(f"Quiz ({selected_option} Level)", anchor=False)
            with st.spinner("AI is generating quizzes ..."):
                quiz = quiz_generator(pil_images, selected_option)
                st.markdown(quiz)
