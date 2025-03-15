import pyttsx3
import tkinter as tk
from tkinter import messagebox
import speech_recognition as sr
import google.generativeai as genai

def log_chat(user_input, response_text):
    with open("chat_log.txt", "a", encoding="utf-8") as log_file:
        log_file.write(f"User: {user_input}\nAI: {response_text}\n{'-'*40}\n")

class ProblemHandler:
    @staticmethod
    def show_error(title, message):
        messagebox.showerror(title, message)

    @staticmethod
    def show_warning(title, message):
        messagebox.showwarning(title, message)

def initialize_genai(api_key):
    try:
        genai.configure(api_key=api_key) 
        return genai.GenerativeModel("gemini-1.5-flash")
    except Exception as e:
        ProblemHandler.show_error("Error", f"Failed to initialize AI model: {e}")
        return None

def initialize_tts():
    try:
        engine = pyttsx3.init()
        engine.setProperty("voice", engine.getProperty("voices")[0].id)
        engine.setProperty("rate", 200)
        engine.setProperty("volume", 1.0)
        return engine
    except Exception as e:
        ProblemHandler.show_error("Error", f"Failed to initialize TTS engine: {e}")
        return None

def recognize_speech():
    recognizer = sr.Recognizer()
    try:
        with sr.Microphone() as source:
            recognizer.adjust_for_ambient_noise(source)
            audio = recognizer.listen(source)
            return recognizer.recognize_google(audio)
    except sr.UnknownValueError:
        ProblemHandler.show_warning("Warning", "Speech not recognized. Please try again.")
    except Exception as e:
        ProblemHandler.show_error("Error", f"Microphone issue: {e}")
    return None

def generate_response(model, text):
    try:
        response = model.generate_content(text)
        return response.text[:100] if response else ""
    except Exception as e:
        ProblemHandler.show_error("Error", f"Failed to generate AI response: {e}")
        return ""

def speak_text(engine, text):
    if text:
        try:
            engine.say(text)
            engine.runAndWait()
        except Exception as e:
            ProblemHandler.show_error("Error", f"Failed to play speech: {e}")

def record_and_speak():
    user_input = recognize_speech()
    if user_input:
        response_text = generate_response(ai_model, user_input)
        chat_history.config(state=tk.NORMAL)
        chat_history.insert(tk.END, f"User: {user_input}\nAI: {response_text}\n\n")
        chat_history.config(state=tk.DISABLED)
        log_chat(user_input, response_text)
        speak_text(tts_engine, response_text)

def clear_history():
    chat_history.config(state=tk.NORMAL)
    chat_history.delete(1.0, tk.END)
    chat_history.config(state=tk.DISABLED)

def create_ui():
    window = tk.Tk()
    window.title("AI Assistant")
    window.geometry("300x250")
    window.configure(bg="#F5F5F5")
    window.resizable(False, False)

    global chat_history
    chat_history = tk.Text(window, height=7, width=35, state=tk.DISABLED, wrap=tk.WORD, bg="white", fg="black")
    chat_history.pack(pady=8, padx=10)

    start_button = tk.Button(window, text="Start", command=record_and_speak, bg="#4CAF50", fg="white", font=("Arial", 10, "bold"), width=20, height=1)
    start_button.pack(pady=5)

    clear_button = tk.Button(window, text="Clear", command=clear_history, bg="#F44336", fg="white", font=("Arial", 10, "bold"), width=20, height=1)
    clear_button.pack(pady=5)

    window.mainloop()

def get_api_key():
    api_key = simpledialog.askstring("API Key", "Enter your API Key:")
    return api_key

if __name__ == "__main__":
    import tkinter.simpledialog as simpledialog

    
    api_key = get_api_key() 

    
    ai_model = initialize_genai(api_key)
    if ai_model is None:
        ProblemHandler.show_error("Error", "Invalid API Key. Exiting program.")
    else:
        tts_engine = initialize_tts()
        if tts_engine:
            create_ui()

print("Program initialized successfully.")

