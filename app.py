import streamlit as st
import google.generativeai as genai
from pathlib import Path

from api_key import api_key

# Configure Gen AI with API key
genai.configure(api_key=api_key)

def upload_to_gemini(path, mime_type=None):
    file = genai.upload_file(path, mime_type=mime_type)
    print(f"Uploaded file '{file.display_name}' as: {file.uri}")
    return file

generation_config = {
    "temperature": 0.4,
    "top_p": 0.95,
    "top_k": 64,
    "max_output_tokens": 8192,
    "response_mime_type": "text/plain",
}

safety_settings = [
    {"category": "HARM_CATEGORY_DANGEROUS", "threshold": "BLOCK_NONE"},
    {"category": "HARM_CATEGORY_HARASSMENT", "threshold": "BLOCK_NONE"},
    {"category": "HARM_CATEGORY_HATE_SPEECH", "threshold": "BLOCK_NONE"},
    {"category": "HARM_CATEGORY_SEXUALLY_EXPLICIT", "threshold": "BLOCK_NONE"},
    {"category": "HARM_CATEGORY_DANGEROUS_CONTENT", "threshold": "BLOCK_NONE"},
]

model = genai.GenerativeModel(
    model_name="gemini-1.5-flash",
    generation_config=generation_config,
    safety_settings=safety_settings
)

chat_session = model.start_chat(history=[])

prompt_parts = [
    "Describe what the people are doing in this image \n",
    "\n what is going on in this image?",
]

response = model.generate_content(prompt_parts)
response = chat_session.send_message("INSERT_INPUT_HERE")

print(response.text)
system_prompt = "Describe this image"

# Design the frontend
st.set_page_config(page_title="Chatbot", page_icon=":robot:")

# Import the Roboto font and apply it
font_css = """
<style>
    @import url('https://fonts.googleapis.com/css2?family=Roboto:wght@400;700&display=swap');

    html, body, [class*="css"]  {
        font-family: 'Roboto', sans-serif;
    }
</style>
"""
st.markdown(font_css, unsafe_allow_html=True)


# Display the Medisense logo in the top-left corner
st.image("MediSenseLogo.png", width=80)

# Set page title with custom font color
st.markdown(
    f"""
    <h1 style='text-align: left; color: #000A8E;'>Hey! I’m Doctor Pulse. How can I help you today?</h1>
    """,
    unsafe_allow_html=True
)

# Set subtitle with custom font color, size, and weight
st.markdown(
    f"""
    <h3 style='text-align: left; color: black; font-size: 18px; font-weight: 400;'>An Application that can help users with medical recommendations and disease detection</h3>
    """,
    unsafe_allow_html=True
)



# Display the image above the file uploader
image_path = "cute-doctor-robot-holding-clipboard-stethoscope-cartoon-vector-icon-illustration-science-techno (1).png"
st.image(image_path, use_column_width=False, width=400)

# Apply gradient background using custom CSS for main content
page_bg_gradient = """
<style>
    .stApp {
        background: linear-gradient(135deg, #FFFFFF, #CEE1F8);
    }
</style>
"""
st.markdown(page_bg_gradient, unsafe_allow_html=True)

# Apply custom CSS for submit button
button_css = """
<style>
    .stButton>button {
        background-color: white; /* White background */
        color: #0661CC; /* Blue text */
        border: 2px solid #0661CC; /* Blue border */
        padding: 10px 20px; /* Some padding */
        text-align: center; /* Centered text */
        text-decoration: none; /* No underline */
        display: inline-block; /* Inline block */
        font-size: 16px; /* Font size */
        margin: 4px 2px; /* Margin */
        cursor: pointer; /* Pointer cursor on hover */
        border-radius: 5px; /* Rounded corners */
    }
    .stButton>button:hover {
        background-color: #0661CC; /* Blue background on hover */
        color: white; /* White text on hover */
    }

    h1, h2, h3, h4, h5, h6 {
        font-family: 'Roboto', sans-serif;
        font-weight: 700;
        letter-spacing: 0.5px;
        margin-bottom: 20px;
        color: #000A8E; /* Deep blue for headings and subheadings */
    }
</style>
"""
st.markdown(button_css, unsafe_allow_html=True)


# Add custom CSS to style the file uploader box
file_uploader_css = """
<style>
    .css-1eq80h2 {
        border: 2px solid #0661CC; /* Border color */
        background-color: #CEE1F8; /* Background color */
        border-radius: 5px; /* Rounded corners */
        padding: 10px; /* Padding */
        color: #000A8E; /* Text color */
        text-align: center; /* Center the text */
        font-size: 16px; /* Font size */
    }
    
    .css-1eq80h2:hover {
        border-color: #000A8E; /* Border color on hover */
        background-color: #FFFFFF; /* Background color on hover */
        color: #000A8E; /* Text color on hover */
    }
</style>
"""
st.markdown(file_uploader_css, unsafe_allow_html=True)

uploaded_file = st.file_uploader("Upload the medical image for analysis", type=["png", "jpg", "jpeg"])

submit_button = st.button("Submit")

if submit_button:
    # Process uploaded image
    image_data = uploaded_file.getvalue()

    # Making our image ready
    image_parts = [
        {
            "mime_type": "image/jpeg",
            "data": image_data
        }
    ]
    prompt_parts = [
        image_parts[0],
        system_prompt,
    ]

    response = model.generate_content(prompt_parts)
    st.write(response.text)
