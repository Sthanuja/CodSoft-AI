import re

def pattern_match(user_input, pattern, response):
    match = re.search(pattern, user_input)
    return match.group(0) if match else None, response

def simple_chatbot(user_input):
    rules = [
        (r"hello|hi|hey", "Hi there! How can I help you?"),
        (r"what is your name?", "I'm a chatbot. You can call me ChatGPT."),
        (r"how are you?|how's it going?", "I'm just a computer program, but I'm doing well. Thanks for asking!"),
        (r"what's your age?|how old are you?", "I don't have an age. I'm always up-to-date!"),
        (r"what is your purpose?|why are you here?", "I'm here to assist and chat with you!"),
        (r"tell me a joke", "Why don't scientists trust atoms? Because they make up everything!"),
        (r"thanks|thank you", "You're welcome! If you have more questions, feel free to ask."),
        (r"what is your favourite color?", "I don't have one, but I think all colors are great!"),
        (r"bye|goodbye", "Goodbye! Have a great day."),
        (r"(.*)", "I'm sorry, I don't understand that."),
    ]

    for pattern, response in rules:
        match, reply = pattern_match(user_input.lower(), pattern, response)
        if match:
            return reply.format(match)

# Example usage
while True:
    user_input = input("You: ")
    if user_input.lower() in ['exit', 'quit', 'bye']:
        print("Bot: Goodbye!")
        break
    bot_response = simple_chatbot(user_input)
    print("Bot:", bot_response)
