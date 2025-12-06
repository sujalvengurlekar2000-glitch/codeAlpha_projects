def chatbot():
    print("Chatbot Activated! Type 'bye' to exit.")
    
    while True:
        user_input = input("You: ").lower()

        if user_input == "hello":
            print("Bot: Hi there!")
        elif user_input == "hi":
            print("Bot: Hello!")
        elif user_input == "how are you":
            print("Bot: I'm fine, thanks for asking!")
        elif user_input == "what is your name":
            print("Bot: I'm a simple Python chatbot.")
        elif user_input == "bye":
            print("Bot: Goodbye! Have a nice day.")
            break
        else:
            print("Bot: Sorry, I don’t understand that.")


# Run chatbot
chatbot()