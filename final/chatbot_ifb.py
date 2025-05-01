#Develop an elementary chatbot for any suitable customer interaction application. IFB Washing Machine Service Centre.

import re

def chatbot_response(user_input):
    user_input = user_input.lower()

    responses = [
        (r"\b(hello|hi|hey)\b", "Hello! Welcome to IFB Washing Machine Service Center. How can I assist you today?"),
        (r"\b(service|repair|fix|broken|not working)\b", "We can help with your washing machine repair needs. Please provide your model number and describe the issue."),
        (r"\b(appointment|schedule|book|slot|visit)\b", "To schedule a service appointment, please provide your preferred date and time, along with your address and contact number."),
        (r"\b(cost|price|charges|fee)\b", "Our service charges depend on the issue and model. Basic diagnosis costs 500, which will be adjusted against repair charges if you proceed with the repair."),
        (r"\b(model|model number)\b", "You can find your model number on the back panel of your washing machine or on your purchase invoice."),
        (r"\b(warranty|guarantee)\b", "IFB washing machines typically come with 2-4 years warranty. Please provide your model number and purchase date to check warranty status."),
        (r"\b(spare|parts|replacement)\b", "We use genuine IFB spare parts for all repairs. Parts are covered under warranty for 6 months after replacement."),
        (r"\b(water|leaking|leak)\b", "Water leakage could be due to loose connections, damaged hoses, or worn-out door seals. A technician needs to examine the machine."),
        (r"\b(noise|noisy|sound|loud)\b", "Unusual noise might indicate an unbalanced load, foreign objects in the drum, or issues with the motor or bearings. We recommend a professional check-up."),
        (r"\b(spin|spinning|not spin|won't spin)\b", "Spinning issues could be related to load balancing, drain pump, or motor problems. Our technicians can diagnose and fix it."),
        (r"\b(drain|draining|not drain|won't drain)\b", "Drainage problems are often caused by clogged filters or pumps. Try cleaning the drain filter first, or schedule a service appointment."),
        (r"\b(door|lid|lock|won't open|stuck)\b", "Door lock issues can be related to the locking mechanism or electronic controls. Please avoid forcing the door and contact our service team."),
        (r"\b(error|code|display|showing|flashing)\b", "Please provide the error code showing on the display. This will help us identify the issue more accurately."),
        (r"\b(annual|maintenance|AMC|amc)\b","We offer Annual Maintenance Contracts (AMC) starting from ₹2500 per year, which includes 4 preventive maintenance visits and priority service."),
        (r"\b(contact|phone|number|call|reach)\b", "You can reach our service center at 1800-123-4567 or email us at service@ifbcare.com."),
        (r"\b(address|location|center|centre)\b", "Our service centers are located in most major cities. Please provide your city and area for the nearest center details."),
        (r"\b(status|track|technician arrival)\b", "Please share your service request ID to check the current status."),
        (r"\b(thank you|thanks|ty)\b", "You're welcome! Is there anything else I can help you with?"),
        (r"\b(bye|goodbye|exit|quit)\b", "Thank you for contacting IFB Service Center. Have a great day!")
    ]

    for pattern, response in responses:
        if re.search(pattern, user_input):
            return response

    return "I'm not sure I understand your query. Could you please rephrase or specify if it's about washing machine repair, maintenance, warranty, or booking a service appointment?"

def display_menu():
    print("You can ask about:")
    print("• Booking a service appointment")
    print("• Washing machine repairs and issues")
    print("• Warranty information")
    print("• Service costs and charges")
    print("• Spare parts and replacements")
    print("• Common problems (water leakage, noise, spinning, draining)")
    print("• Annual Maintenance Contract (AMC)")
    print("• Contact information")
    print("\n")
    print("Type 'menu' to see this information again or 'exit' to end chat")

print("Welcome to IFB Washing Machine Service Center!")
print("How can we assist you with your washing machine today?")
display_menu()

while True:
    user_message = input("\nYou: ")
    if re.search(r"\b(bye|exit|quit|goodbye)\b", user_message.lower()):
        print("IFB Service: Thank you for contacting IFB Service Center. Have a great day!")
        break
    elif user_message.lower() == "menu":
        display_menu()
        continue
    response = chatbot_response(user_message)
    print("IFB Service:", response)