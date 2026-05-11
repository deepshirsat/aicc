def chatbot():
    print("Chatbot: Hello! How can I help you today? (type 'exit' to quit)")
    while True:
        user = input("You: ").lower()
        if user == "exit":
            print("Chatbot: Thank you! Have a nice day.")
            break
        elif "hi" in user or "hello" in user:
            print("Chatbot: Hello! How can I assist you?")
        elif "price" in user:
            print("Chatbot: Please tell me the product name to check price.")
        elif "order" in user:
            print("Chatbot: Your order will be delivered in 3-5 days.")
        elif "refund" in user:
            print("Chatbot: Refund will be processed within 5 working days.")
        elif "help" in user:
            print("Chatbot: I can help with orders, price, refund.")
        else:
            print("Chatbot: Sorry, I didn't understand. Please try again.")
# Run
chatbot()

# Output
#PS C:\Users\user> & C:/Users/user/anaconda3/python.exe "e:/AI/P5(chatbot).py"
#Chatbot: Hello! How can I help you today? (type 'exit' to quit)
#Chatbot: Hello! How can I assist you?
#You: order status
#Chatbot: Your order will be delivered in 3-5 days.
#Chatbot: Refund will be processed within 5 working days.
#You: ok
#Chatbot: Sorry, I didn't understand. Please try again.
#You: exit
#Chatbot: Thank you! Have a nice day.
