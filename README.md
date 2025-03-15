AI Assistant

Overview

This is a simple AI-powered voice assistant that listens to user speech, generates a response using Google's Gemini AI model, and provides a text-to-speech (TTS) response. The application is built using Python and utilizes the following libraries:

pyttsx3 for text-to-speech functionality

tkinter for the graphical user interface

speech_recognition for voice input processing

google.generativeai for AI-generated responses

Features

Voice recognition and response generation

Text-to-speech playback

Chat history logging

Simple and intuitive GUI

Installation

Prerequisites

Ensure you have Python installed (>= 3.7). Then, install the required dependencies:

pip install pyttsx3 tkinter speechrecognition google-generativeai

Usage

Run the script:

python script.py

Use the GUI:

Click the Start button to begin voice input.

Click Clear to erase the chat history.

The AI will listen, respond, and speak the response aloud.

File Structure

AI-Assistant/
│-- script.py          # Main application file
│-- chat_log.txt       # Chat history log

Configuration

Replace the API_KEY in the script with your Google Gemini AI API key to enable AI-generated responses.

License

This project is licensed under the MIT License.

Acknowledgments

Google Gemini AI

Python Community

