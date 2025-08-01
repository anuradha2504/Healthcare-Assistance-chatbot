# Healthcare-Assistance-chatbot
# 💬 Healthcare Chatbot using OpenAI & Streamlit

A conversational healthcare chatbot built with OpenAI's GPT model and a clean Streamlit UI. This assistant answers **only healthcare-related questions** (symptoms, wellness, diet, mental health, etc.) and refuses unrelated queries. Chat history is saved using Python’s Pickle module.

## Features

-  AI-powered healthcare Q&A
-  Domain-restricted: only responds to health-related queries
-  Saves and loads chat history with `.pkl` file
-  Streamlit-based interactive UI
-  API key secured via `.env` file

## 📁 Project Structure
healthcare_chatbot/
├── .env # Stores OpenAI API Key
├── app.py # Streamlit app UI
├── chatbot.py # Handles OpenAI conversation logic
├── chat_history.pkl # Auto-generated file storing chat history
├── requirements.txt # Python dependencies
└── README.md # This file

