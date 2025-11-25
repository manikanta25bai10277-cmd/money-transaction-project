# Simple Payment Simulation
users = {"madhav": {"pin": "1243", "balance": 5000},
    "arjun": {"pin": "4756", "balance": 3000}}

def send_money(sender, receiver, amount, pin):
    if sender not in users or receiver not in users: .
        return "User not found!"

    if users[sender]["pin"] != pin:
        return "WRONG Wrong PIN!"

    if users[sender]["balance"] < amount:
        return "WRONG Insufficient balance!"
    users[sender]["balance"] -= amount
    users[receiver]["balance"] += amount

    return f" Payment Successful!\n₹{amount} sent from {sender} to {receiver}"
    def check_balance(user):
         if user in users:
           return f"{user}'s current balance: ₹{users[user]['balance']}"            
           

print(" Welcome to Paypal Simulation\n")

sender = input("Enter your username: ")
pin = input("Enter your PIN: ")

print("1. Send Money")
print("2. Check Balance")
choice = int(input("Enter choice: "))
if choice == 1:
    receiver = input("Enter receiver username: ")
    amount = int(input("Enter amount: ₹"))
    print(send_money(sender, receiver, amount, pin))
elif choice == 2:
    print(check_balance (sender))


transaction_history = []
# Inside send_money function, after successful payment:
transaction = {
    "from": sender,
    "to": receiver,
    "amount": amount,}
transaction_history.append(transaction)
