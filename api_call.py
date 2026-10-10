from google import genai
from dotenv import load_dotenv
from gtts import gTTS
import os, io


# Load environment variable
load_dotenv()

# Get API Key
my_api_key = os.getenv("GEMINI_API_KEY")

# Initializing Client
client = genai.Client(api_key=my_api_key)

# Generate Note
def note_generator(img):    
    request = """generate a note form image in 50 words. 
    make sure to add necessary markdown to this differentiate different section"""    
    response = client.models.generate_content(
        model="gemini-3-flash-preview",
        contents=[img, request]
    )    
    return response.text

# Generate Audio
def audio_transcription(text):
    speech = gTTS(text, lang="en", slow=False)
    audio_buffer = io.BytesIO()
    speech.write_to_fp(audio_buffer)
    return audio_buffer

# Generate Quiz
def quiz_generator(img, difficulty):
    request = f"""generate 3 quizzes based on {difficulty} from uploaded image. add necessary markdown to this differentiate for different quiz. also show correct answers bellow the quizzes."""    
    response = client.models.generate_content(
        model="gemini-3-flash-preview",
        contents=[img, request]
    )    
    return response.text


