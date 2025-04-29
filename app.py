from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# Chatbot logic
class RestaurantBot:
    def __init__(self):
        self.orders = {}  # Dictionary to store customer name as key and their orders as values
        self.reservations = []  # List to store reservations
        self.current_customer = None  # To track the current interacting customer

    def set_customer_name(self, name):
        self.current_customer = name

    def handle_input(self, user_input):
        user_input = user_input.lower()

        if self.current_customer is None:
            return f"Hello! May I know your name please?"

        if "reservation" in user_input:
            return self.make_reservation(user_input)
        elif "order" in user_input:
            return self.place_order(user_input)
        elif "menu" in user_input:
            return self.show_menu()
        else:
            return "I can help with reservations or orders. Type 'menu' to see what we serve."

    def make_reservation(self, user_input):
        # Simple logic to book a reservation
        self.reservations.append(user_input)
        return "Your reservation has been made! Thank you."

    def place_order(self, user_input):
        # Extract item from user input and place order
        menu = self.get_menu()
        for item in menu:
            if item.lower() in userMessage:
                if self.current_customer:
                    if self.current_customer not in self.orders:
                        self.orders[self.current_customer] = []
                    self.orders[self.current_customer].append({"item": item, "price": menu[item]})
                    return f"Your order for {item} has been placed! It will be ready shortly."
                return "Please provide your name first to place an order."
        return "Sorry, that item is not on the menu."

    def show_menu(self):
        menu = self.get_menu()
        return f"Our menu: {menu}"

    def get_menu(self):
        # Menu of the restaurant
        return {
            "Pizza": 250,
            "Burger": 150,
            "Pasta": 200,
            "Salad": 120,
            "Sushi": 350,
            "Dosa": 100,
            "Ice Cream": 90,
            "Chocolate": 80,
            "Coffee": 60
        }

    def get_orders(self):
        return self.orders


# Initialize the chatbot
bot = RestaurantBot()

@app.route('/')
def index():
    return render_template('index.html')


@app.route("/chat", methods=["POST"])
def chat():
    user_input = request.json.get("message")

    # Capture the customer's name if not already set
    if bot.current_customer is None:
        bot.set_customer_name(user_input)
        response = f"Nice to meet you, {user_input}! How can I assist you today?"
    else:
        response = bot.handle_input(user_input)

    return jsonify({"response": response})


# Route for the staff to view orders
@app.route("/chef/orders")
def view_orders():
    return render_template('orders.html', orders=bot.get_orders())


if __name__ == "__main__":
    app.run(debug=True)

