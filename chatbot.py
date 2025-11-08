def chatbot():
    print("Chatbot: Hello! I'm a simple chatbot. Type 'bye' to end our conversation.")
    
    while True:
        user_input = input("You: ").lower().strip()
        
        if user_input in ["hello", "hi", "hey"]:
            print("Chatbot: Hi!")
        elif user_input in ["how are you", "how are you doing"]:
            print("Chatbot: I'm fine, thanks!")
        elif user_input in ["bye", "goodbye", "exit", "quit"]:
            print("Chatbot: Goodbye!")
            break
        elif user_input in ["what's your name", "who are you"]:
            print("Chatbot: I'm a simple rule-based chatbot!")
        elif user_input in ["help", "what can you do"]:
            print("Chatbot: I can respond to greetings like 'hello', 'how are you', and 'bye'.")
        else:
            print("Chatbot: I'm sorry, I don't understand that.")


if __name__ == "__main__":
    chatbot()
