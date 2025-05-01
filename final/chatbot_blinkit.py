#Develop an elementary chatbot for any suitable customer interaction application. Blink –IT
import re

def chatbot_response(user_input):
    user_input = user_input.lower()

    responses = [
        (r"\b(hello|hi|hey)\b", "Hello! Welcome to Blink-IT. How can I help you today?"),
        (r"\bhow (are|r) (you|u)\b", "I'm a chatbot ready to assist you with your grocery orders."),
        (r"\b(cancel|cancel order|cancellation)\b", "To cancel an order, please provide your order ID."),
        (r"\b(order|buy|purchase)\b", "To place an order, please mention the item you wish to buy."),
        (r"\b(status|track|order status)\b", "Please share your order ID to check the current status."),
        (r"\brefund\b", "Refunds are processed within 3 to 5 business days. Please provide your order ID."),
        (r"\b(payment|payment options|pay)\b", "We accept UPI, credit/debit cards, and cash on delivery."),
        (r"\b(delivery time|delivery|when.*deliver)\b", "Most deliveries are completed within 10 to 30 minutes after placing the order."),
        (r"\b(items available|products|inventory)\b", "We have fresh fruits, vegetables, dairy products, snacks, and daily essentials. What are you looking for?"),
        (r"\b(thank you|thanks|ty)\b", "You're welcome! Let me know if you need anything else."),
        (r"\b(contact|help|support)\b", "You can contact our support team at support@blinkit.com or call 1800-222-5555."),
        (r"\b(offers|discounts|promotions|deals)\b", "We have exciting discounts and cashback offers. Would you like to know today's special offers?"),
        (r"\b(return|replace|exchange)\b", "We offer easy return and replacement for damaged or wrong items. Please share your order ID."),
        (r"\b(membership|blinkit plus|subscribe)\b", "Blink-IT Plus members get free delivery and exclusive offers. Would you like to join?"),
        (r"\b(bye|exit|quit)\b", "Goodbye! Thank you for choosing Blink-IT.")
    ]

    for pattern, response in responses:
        if re.search(pattern, user_input):
            return response

    return "I'm sorry, I didn't quite catch that. Can you rephrase?"

def display_menu():
    print("BLINK-IT CUSTOMER SUPPORT MENU")
    print("You can ask about:")
    print("• Ordering groceries")
    print("• Checking order status")
    print("• Canceling an order")
    print("• Refunds")
    print("• Delivery information")
    print("• Payment options")
    print("• Available products")
    print("• Offers and discounts")
    print("• Return policy")
    print("• Contact support")


print("Welcome to Blink-IT Customer Service!")
print("\n")
print("I'm your virtual assistant, here to help with your grocery needs.")
print("\n")
display_menu()
print("\nType 'exit' anytime to end our conversation.")

while True:
    user_message = input("\nYou: ")
    if re.search(r"\b(bye|exit|quit)\b", user_message.lower()):
        print("Chatbot: Goodbye! Thank you for choosing Blink-IT.")
        break
    elif user_message.lower() == "menu":
        display_menu()
        continue
    response = chatbot_response(user_message)
    print("Chatbot:", response)