# AI Chatbot for mental health #

import nltk
from nltk.stem import PorterStemmer
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.pipeline import Pipeline
from sklearn.svm import SVC


def preprocess(text):
    words = nltk.word_tokenize(text)
    stemmer = PorterStemmer()
    words = [stemmer.stem(word) for word in words]
    return words


def chatbot_response(user_input):
    if "hello" in user_input:
        return "Hello! How can I help you today?"
    elif "how are you" in user_input:
        return "I'm doing well, thank you. How are you?"
    elif "thank you" in user_input or "thanks" in user_input:
        return "You're welcome!"
    elif "what is your name" in user_input:
        return "I'm a simple chatbot"
    elif "what can you do" in user_input:
        return "I can answer simple questions, provide basic information, and have a friendly chat."
    elif "I want to ask about my mental health" in user_input:
        return "Yes,sure.Feel free to ask."
    elif "feeling down" in user_input or "sad" in user_input or "depressed" in user_input:
        return "If you're feeling overwhelmed, please reach out to a trusted friend, family member, or a mental health professional."
    elif "anxious" in user_input or "worry" in user_input or "panic" in user_input:
        return "If you're feeling anxious, try some relaxation techniques like deep breathing or mindfulness."
    elif "lonely" in user_input or "isolated" in user_input:
        return "Feeling lonely is common. Try reaching out to friends, family, or joining social groups."
    elif "stress" in user_input:
        return "Try relaxation techniques like deep breathing and mindfulness. Exercise, healthy eating, and sufficient sleep"
    else:
        return "I'm not sure how to help with that. Can you rephrase your question?"


while True:
    user_input = input("You: ")
    if user_input.lower() == "quit":
        break
    response = chatbot_response(user_input)
    print("Bot:", response)
