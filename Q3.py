order_amount = float(input("Enter order amount: ₹"))
membership = input("Are you a member? (yes/no): ").strip().lower()

if order_amount < 0 or order_amount > 100000:
    print("Invalid order amount.")
    print("Eligibility Status: Not eligible")
else:
    if order_amount >= 5000:
        discount_percentage = 15
    elif order_amount >= 2000 and membership == "yes":
        discount_percentage = 10
    else:
        discount_percentage = 0

    discount_amount = order_amount * discount_percentage / 100
    final_amount = order_amount - discount_amount

    print(f"Original Amount: ₹{order_amount:.2f}")
    print(f"Discount Percentage: {discount_percentage}%")
    print(f"Discount Amount: ₹{discount_amount:.2f}")
    print(f"Final Payable Amount: ₹{final_amount:.2f}")

    if discount_percentage > 0:
        print("Eligibility Status: Eligible for discount")
    else:
        print("Eligibility Status: Not eligible for discount")
