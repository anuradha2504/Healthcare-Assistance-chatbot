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

How It Works
Uses OpenAI's gpt-4 or gpt-3.5-turbo model via API.

A system prompt instructs the chatbot to only handle healthcare-related queries.

If users ask non-health questions, it politely declines.

Messages are stored in chat_history.pkl using Python’s pickle module.

Example Interactions
User: What are the symptoms of vitamin D deficiency?
Bot: Common symptoms include fatigue, bone pain, muscle weakness...

User: Who is the president of India?
Bot: I'm sorry, I can only assist with healthcare-related topics.

Disclaimer
This chatbot provides general health-related information and is not a substitute for professional medical advice. Always consult a licensed doctor for personal health concerns.

