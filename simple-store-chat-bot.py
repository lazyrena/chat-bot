import random

# Sample product database
products = {
    "iphone": 1000,
    "laptop": 800,
    "headphones": 150,
    "smartwatch": 200,
    "camera": 500
}

# Greetings
def greet():
    print("Hi there! Welcome to our store. How can I assist you today?")
    print("You can ask for prices, list products, or buy something.")
    print("For example, you can ask: 'What is the price of the laptop?'")
    print("Or you can say: 'List all products'")

# Function to handle user queries
def process_query(query):
    query = query.lower()
    if "price of" in query:
        product = query.split("price of")[-1].strip()
        if product in products:
            print(f"The price of {product} is ${products[product]}.")
        else:
            print("Sorry, we don't have that product in our inventory.")
    elif "buy" in query:
        product = query.split("buy")[-1].strip()
        if product in products:
            print(f"You have purchased {product} for ${products[product]}. Thank you for shopping with us!")
        else:
            print("Sorry, we don't have that product in our inventory.")
    elif "list" in query:
        print("Here are the available products:")
        for product, price in products.items():
            print(f"- {product}: ${price}")
    elif any(word in query for word in ["exit", "quit", "goodbye"]):
        print("Thank you for visiting. Have a great day!")
        return True
    else:
        print("I'm sorry, I didn't understand that. You can ask for prices, list products, or buy something.")

    return False

# Main function
def main():
    greet()
    while True:
        query = input("> ")
        if process_query(query):
            break

if __name__ == "__main__":
    main()
