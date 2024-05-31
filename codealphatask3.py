import re

# Define a set of rules for responses
responses = {
    "hello": "Hello! How can I assist you today?",
    "hi": "Hi there! How can I help you?",
    "hey": "Hey! What can I do for you?",
    "how are you": "I'm a bot, so I'm always good. How about you?",
    "what is your name": "I am a chatbot created by you. You can call me Chatbot.",
    "who created you": "I was created by a programmer. How can I assist you?",
    "how old are you": "I am timeless!",
    "quit": "Bye! Take care.",
}

def chatbot():
    print("Hi! I'm a chatbot. How can I help you today? (Type 'quit' to exit)")

    while True:
        user_input = input("You: ").lower()
        if user_input == "quit":
            print("Chatbot: Bye! Take care.")
            break

        response = None

        # Check for exact matches first
        if user_input in responses:
            response = responses[user_input]
        else:
            # Handle more complex input with regular expressions
            if re.match(r"my name is (.*)", user_input):
                name = re.match(r"my name is (.*)", user_input).group(1)
                response = f"Hello {name}, how can I assist you today?"
            elif re.match(r"i'm (.*) doing good", user_input):
                response = "Nice to hear that! Glad to know you're doing good."

        if response:
            print(f"Chatbot: {response}")
        else:
            print("Chatbot: I'm not sure how to respond to that.")

# Run the chatbot
if _name== "main_":
  chatbot()