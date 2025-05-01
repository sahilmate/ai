def ask_question(question):
    return input(question + " ")

def evaluate(trend, fundamentals, indicators):
    return (trend.lower() == "upwards" and
            fundamentals.lower() == "strong" and
            indicators.lower() == "positive")

def print_result(should_buy):
    if should_buy:
        print("Recommendation: Buy the stock!")
    else:
        print("Recommendation: Do not buy the stock.")

def main():
    print("Welcome to the Stock Market Trading System!")
    print("Please answer the following questions:")

    trend = ask_question("What is the current market trend? (Upwards/Downwords):")
    fundamentals = ask_question("How are the fundamentals of the company? (strong/weak):")
    indicators = ask_question("What do the technical indicators suggest? (positive/negative):")

    should_buy = evaluate(trend, fundamentals, indicators)
    print_result(should_buy)

if __name__ == "__main__":
    main()


# Output
# Welcome to the Stock Market Trading System!
# Please answer the following questions:
# What is the current market trend? (Upwards/Downwords): Upwards
# How are the fundamentals of the company? (strong/weak): strong
# What do the technical indicators suggest? (positive/negative): positive
# Recommendation: Buy the stock!