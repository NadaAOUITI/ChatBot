import re
import random


patterns = {
    r'hi|hello|hey': [
        "Hello! How can I assist you today?",
        "Hi there! What can I do for you?",
        "Hey! Need any help?"
    ],
    r'how are you': [
        "I'm a bot, but I'm functioning as expected!",
        "All systems operational. How can I help you?"
    ],
    r'what is your name': [
        "I'm ChatBot, your virtual assistant.",
        "They call me ChatBot. I'm here to help!"
    ],
    r'help': [
        "Sure, I'm here to assist. What do you need help with?",
        "I'm ready to help! Please tell me your query."
    ],
    r'bye|exit|quit': [
        "Goodbye! Have a great day!",
        "See you later! If you need anything else, just ask."
    ]
}

def get_response(user_input):
    for pattern, responses in patterns.items():
        if re.search(pattern, user_input, re.IGNORECASE):
            return random.choice(responses)
    return "I'm not sure how to respond to that. Could you please rephrase?"

def main():
    print("ChatBot: Hello! Type 'exit' to end the conversation.")
    while True:
        user_input = input("You: ")
        response = get_response(user_input)
        print(f"ChatBot: {response}")
        if re.search(r'bye|exit|quit', user_input, re.IGNORECASE):
            break

if __name__ == "__main__":
    main()
