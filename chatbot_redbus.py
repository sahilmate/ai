#Develop an elementary chatbot for any suitable customer interaction application. RED- BUS
import re
def chatbot_response(user_input):
    user_input = user_input.lower()

    responses = [
        (r"\b(hello|hi|hey)\b", "Hello! Welcome to RedBus customer support. How can I assist you today?"),
        (r"\b(book|booking|reserve|ticket)\b", "To book a bus ticket, please provide your source, destination, and travel date."),
        (r"\b(cancel|cancellation)\b", "To cancel your ticket, please provide your booking ID. Note that cancellation charges may apply based on the operator's policy."),
        (r"\b(refund|money back)\b", "Refunds are processed within 5-7 working days to the original payment method. For specific refund status, please provide your booking ID."),
        (r"\b(reschedule|change date|postpone)\b", "To reschedule your journey, please provide your booking ID. Rescheduling charges may apply as per the operator's policy."),
        (r"\b(status|booking status)\b", "To check your booking status, please share your booking ID or the mobile number used for booking."),
        (r"\b(seat|seating|seat selection)\b", "You can select your preferred seat during the booking process, subject to availability. Premium seats may have additional charges."),
        (r"\b(luggage|baggage|bags)\b", "Most bus operators allow 15kg of luggage per passenger. Additional charges may apply for excess baggage."),
        (r"\b(boarding point|pickup|pick up)\b", "Boarding points are listed during the booking process. You can select your preferred boarding point based on availability."),
        (r"\b(dropping|drop|drop-off)\b", "Drop-off points are predetermined by the bus operator. You can view available drop-off points during booking."),
        (r"\b(payment|pay|transaction)\b", "We accept various payment methods including credit/debit cards, net banking, UPI, and wallets. All transactions are secure."),
        (r"\b(discount|offer|coupon|promo|code)\b", "Use code FIRST for 10% off on your first booking. Visit the offers section on our app or website for more current promotions."),
        (r"\b(receipt|invoice|bill)\b", "Your e-ticket serves as an invoice. You can also download the invoice from the 'My Bookings' section on our website or app."),
        (r"\b(bus type|ac|non-ac|sleeper|volvo)\b", "We offer various bus types including AC, Non-AC, Sleeper, Semi-Sleeper, and Volvo buses. You can filter by bus type during search."),
        (r"\b(safety|covid|sanitization|hygiene)\b", "All our partner buses follow safety protocols including regular sanitization, temperature checks, and mandatory masks for staff and passengers."),
        (r"\b(contact|phone|call|reach|support)\b", "You can reach our 24/7 customer support at 1800-123-4567 or email us at support@redbus.in."),
        (r"\b(app|download|mobile|application)\b", "You can download the RedBus app from Google Play Store or Apple App Store for a better booking experience."),
        (r"\b(rating|review|feedback)\b", "You can check bus ratings and reviews from other travelers during the booking process to help you make an informed choice."),
        (r"\b(thank you|thanks|ty)\b", "You're welcome! Is there anything else I can help you with?"),
        (r"\b(bye|goodbye|exit|quit)\b", "Thank you for contacting RedBus support. Have a safe journey!")
    ]

    for pattern, response in responses:
        if re.search(pattern, user_input):
            return response

    return "I'm not sure I understand your query. Could you please rephrase or specify if it's about booking, cancellation, refund, or any other RedBus service?"

def display_menu():
    print("\n")
    print("You can ask about:")
    print("• Bus ticket booking")
    print("• Cancellation and refunds")
    print("• Booking status")
    print("• Rescheduling your journey")
    print("• Seat selection")
    print("• Boarding and drop-off points")
    print("• Payment options")
    print("• Discounts and offers")
    print("• Bus types and facilities")
    print("• Safety measures")

    print("Type 'menu' to see this information again or 'exit' to end chat")

print("Welcome to RedBus Customer Support!")
print("How can we help you with your bus travel needs today?")
display_menu()

while True:
    user_message = input("\nYou: ")
    if re.search(r"\b(bye|exit|quit|goodbye)\b", user_message.lower()):
        print("RedBus: Thank you for contacting RedBus support. Have a safe journey!")
        break
    elif user_message.lower() == "menu":
        display_menu()
        continue
    response = chatbot_response(user_message)
    print("RedBus:", response)
