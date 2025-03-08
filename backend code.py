import azure.cognitiveservices.speech as speechsdk

# Azure Speech API credentials
SPEECH_KEY = "A72lnb1h5F1eek4IGkNJS0nJvgYOdvwosL1dN1oMO3yNj5Ze7zHDJQQJ99BCACYeBjFXJ3w3AAAYACOG1mDi"
SERVICE_REGION = "eastus"

# Function to recognize speech from the microphone
def speech_to_text():
    speech_config = speechsdk.SpeechConfig(subscription="A72lnb1h5F1eek4IGkNJS0nJvgYOdvwosL1dN1oMO3yNj5Ze7zHDJQQJ99BCACYeBjFXJ3w3AAAYACOG1mDi", region="eastus")
    recognizer = speechsdk.SpeechRecognizer(speech_config=speech_config)
    
    print("\n Speak now...")
    result = recognizer.recognize_once()
    
    if result.reason == speechsdk.ResultReason.RecognizedSpeech:
        return result.text
    else:
        return "Sorry, I couldn't understand."

# Function to generate chatbot response (Replace this with your chatbot logic)
def chatbot_respond(user_input):
    response = f"You said: {user_input}. This is a chatbot response."
    return response  # Replace with actual chatbot logic

# Function to convert text to speech
def text_to_speech(text):
    speech_config = speechsdk.SpeechConfig(subscription="A72lnb1h5F1eek4IGkNJS0nJvgYOdvwosL1dN1oMO3yNj5Ze7zHDJQQJ99BCACYeBjFXJ3w3AAAYACOG1mDi", region="eastus")
    speech_config = speechsdk.SpeechConfig(subscription="A72lnb1h5F1eek4IGkNJS0nJvgYOdvwosL1dN1oMO3yNj5Ze7zHDJQQJ99BCACYeBjFXJ3w3AAAYACOG1mDi", region="eastus")
    synthesizer = speechsdk.SpeechSynthesizer(speech_config=speech_config)
    synthesizer.speak_text_async(text).get()

# Main chatbot loop with microphone input
while True:
    print("\nListening for user input...")
    
    # Get voice input from the microphone
    user_input = speech_to_text()
    print(f" You said: {user_input}")

    # Check if the user wants to exit
    if user_input.lower() in ["exit", "quit", "stop"]:
        print(" Chatbot: Goodbye!")
        text_to_speech("Goodbye!")
        break

    # Generate chatbot response
    response = chatbot_respond(user_input)
    print(f"Chatbot: {response}")

    # Speak chatbot response
    text_to_speech(response)