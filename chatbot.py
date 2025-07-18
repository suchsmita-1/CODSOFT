# Simple Rule-Based Chatbot
# Made by Suchismita Padhi for CodSoft Internship (AI)

print("🤖 Welcome to ChatBot! Type 'exit' to end the chat.\n")

while True:
    user = input("You: ").lower()

    if user == "exit":
        print("ChatBot: Goodbye! Have a nice day 🙂")
        break
    elif "hello" in user or "hi" in user:
        print("ChatBot: Hello! How can I help you?")
    elif "your name" in user or "who are you" in user:
        print("ChatBot: I am ChatBot made by Suchismita!")
    elif "how are you" in user:
        print("ChatBot: I'm just a bot, but I'm doing fine! How can I help?")
    elif "bye" in user:
        print("ChatBot: Bye! Take care.")
    elif "help" in user:
        print("ChatBot: You can ask me about my name, how I feel, or just say hi!")
    else:
        print("ChatBot: Sorry, I didn’t understand that.")
