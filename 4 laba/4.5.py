def calculate_units_purchased(n):
    purchases = {}
    for _ in range(n):
        line = input().split()
        customer_id = int(line[0])
        product = line[1]
        quantity = int(line[2])

        if customer_id in purchases:
            purchases[customer_id].append((product, quantity))
        else:
            purchases[customer_id] = [(product, quantity)]

    for customer_id, products in purchases.items():
        print(f"Customer ID: {customer_id}")
        for product, quantity in products:
            print(f"Product: {product}, Quantity: {quantity}")


n = int(input("Enter the number of purchase records: "))


calculate_units_purchased(n)
