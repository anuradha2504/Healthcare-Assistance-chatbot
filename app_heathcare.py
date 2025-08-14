{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyObpW9zPzU6fCAiZtOCLmfW",
      "include_colab_link": true
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    },
    "language_info": {
      "name": "python"
    }
  },
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "view-in-github",
        "colab_type": "text"
      },
      "source": [
        "<a href=\"https://colab.research.google.com/github/anuradha2504/Healthcare-chatbot/blob/main/app_heathcare.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "id": "di1NOwht5Gw4"
      },
      "outputs": [],
      "source": [
        "!pip install streamlit\n",
        "import streamlit as st\n",
        "import os\n",
        "import pickle\n",
        "from chatbot import get_healthcare_response\n",
        "\n",
        "st.set_page_config(page_title=\"Healthcare Chatbot\", page_icon=\"💬\")\n",
        "st.title(\"💬 Healthcare Assistant Chatbot\")\n",
        "st.markdown(\"Ask health-related questions (e.g., symptoms, wellness, nutrition).\")\n",
        "\n",
        "HISTORY_FILE = \"Healthcare_chatbot.pkl\"\n",
        "\n",
        "# Load saved chat history if exists\n",
        "def load_history():\n",
        "    if os.path.exists(HISTORY_FILE):\n",
        "        with open(HISTORY_FILE, \"rb\") as f:\n",
        "            return pickle.load(f)\n",
        "    return []\n",
        "\n",
        "# Save chat history to file\n",
        "def save_history(history):\n",
        "    with open(HISTORY_FILE, \"wb\") as f:\n",
        "        pickle.dump(history, f)\n",
        "\n",
        "# Initialize session\n",
        "if \"messages\" not in st.session_state:\n",
        "    st.session_state[\"messages\"] = load_history()\n",
        "\n",
        "# Display messages\n",
        "for msg in st.session_state[\"messages\"]:\n",
        "    with st.chat_message(msg[\"role\"]):\n",
        "        st.markdown(msg[\"content\"])\n",
        "\n",
        "# Input\n",
        "user_input = st.chat_input(\"Ask your healthcare question here...\")\n",
        "\n",
        "if user_input:\n",
        "    st.session_state[\"messages\"].append({\"role\": \"user\", \"content\": user_input})\n",
        "    with st.chat_message(\"user\"):\n",
        "        st.markdown(user_input)\n",
        "\n",
        "    response = get_healthcare_response(user_input)\n",
        "\n",
        "    st.session_state[\"messages\"].append({\"role\": \"assistant\", \"content\": response})\n",
        "    with st.chat_message(\"assistant\"):\n",
        "        st.markdown(response)\n",
        "\n",
        "    # Save updated chat history\n",
        "    save_history(st.session_state[\"messages\"])"
      ]
    }
  ]
}