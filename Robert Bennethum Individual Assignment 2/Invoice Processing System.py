# Robert Bennethum
# INPUT
def get_invoice_input():
    items = []
    print("Enter items (blank to finish):")
    while True:
        desc = input("Description: ")
        if not desc:
            break
        try:
            qty = int(input("Quantity: "))
            price = float(input("Price: "))
            items.append({"desc": desc, "qty": qty, "price": price})
        except ValueError:
            print("Invalid input")
    return {"items": items}

# VALIDATION
def validate_invoice(invoice):
    if "items" not in invoice or not invoice["items"]:
        print("No items")
        return False
    for item in invoice["items"]:
        if item["qty"] <= 0 or item["price"] < 0:
            print(f"Invalid: {item['desc']}")
            return False
    return True

# PROCESSING
def calculate_invoice(invoice):
    subtotal = sum(item["qty"] * item["price"] for item in invoice["items"])
    tax = subtotal * 0.06  # 6% sales tax
    total = subtotal + tax
    invoice["subtotal"] = subtotal
    invoice["tax"] = tax
    invoice["total"] = total
    return invoice

# OUTPUT
def print_invoice(invoice):
    print("\nINVOICE")
    for item in invoice["items"]:
        print(f"{item['desc']}: {item['qty']} x ${item['price']:.2f}")
    print(f"Subtotal: ${invoice['subtotal']:.2f}")
    print(f"Tax (6%): ${invoice['tax']:.2f}")
    print(f"Total: ${invoice['total']:.2f}")

# Main
invoice = get_invoice_input()
if validate_invoice(invoice):
    invoice = calculate_invoice(invoice)
    print_invoice(invoice)
else:
    print("Validation failed")
