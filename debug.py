from customer import Customer
from coffee import Coffee
from order import Order

if __name__ == "__main__":
    # Example debug/demo usage

    # Create customers
    drake = Customer("drake")
    Emma = Customer("Emma")

    # Create coffees
    latte = Coffee("Latte")
    espresso = Coffee("Espresso")

    # Create orders
    order1 = drake.create_order(latte, 3.5)
    order2 = Emma.create_order(latte, 4.0)
    order3 = drake.create_order(espresso, 2.5)

    # Print all orders for Alice
    print("drake's orders:", drake.orders())

    # Print all coffees Alice has ordered
    print("drake's coffees:", [c.name for c in drake.coffees()])

    # Print all customers who ordered Latte
    print("Latte customers:", [c.name for c in latte.customers()])

    # Print number of orders for Latte
    print("Latte num_orders:", latte.num_orders())

    # Print average price for Latte
    print("Latte average price:", latte.average_price())

    # Print most aficionado for Latte
    print("Most aficionado for Latte:", Customer.most_aficionado(latte).name)