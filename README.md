# Simple Payment Simulation

This is a simple Python script that simulates core functionalities of a mobile payment application like PhonePe, allowing users to send money and check their balance.

## Features

* **User Authentication:** Basic PIN-based validation for transactions.
* **Send Money:** Allows transferring a specified amount from one user to another, with checks for sufficient balance and correct PIN.
* **Check Balance:** Displays the current balance of a specified user.
* **Simple Transaction Logging:** Records basic transaction details (sender, receiver, amount) in a list.

## Prerequisites

* **Python:** This script requires Python 3.x to run.

## How to Run

1.  Save the code as a Python file (e.g., `phonepe_simulation.py`).
2.  Open your terminal or command prompt.
3.  Navigate to the directory where you saved the file.
4.  Run the script using the Python interpreter:

    ```bash
    python phonepe_simulation.py
    ```

## Usage

When you run the script, you'll be prompted to enter your username and PIN.

### Initial Users & Balances

The simulation starts with two predefined users:

| User | PIN | Initial Balance (₹) |
| :--- | :-- | :------------------ |
| **Madhav** | `1243` | `5000` |
| **Arjun** | `4756` | `3000` |

### Menu Options

After entering your credentials, you will see a menu:

1.  **Send Money**
2.  **Check Balance**

Follow the prompts for the selected choice.

### Example Interaction (Sending Money)

Welcome to PhonePay Simulation

Enter your username:MADHAV Enter your PIN: 1243

Send Money

Check Balance Enter choice: 1 Enter receiver username: ARJUN Enter amount: ₹500 Payment Successful! ₹500 sent from madhav to Arjun


### Example Interaction (Checking Balance)

Welcome to PhonePay Simulation

Enter your username: Madhav Enter your PIN: 4756

Send Money

Check Balance Enter choice: 2 Madhav's current balance: ₹3000


## Code Structure

* `users`: A dictionary storing user data, including their **PIN** and current **balance**.
* `send_money(sender, receiver, amount, pin)`: The main function to handle transfers, performing necessary checks.
* `check_balance(user)`: A function to retrieve and display a user's current balance.
* `transaction_history`: A list that stores a basic log of successful transactions (appended outside the function flow in the current version).

## Future Improvements

* Implement the `check_balance` function properly within the flow and use a **try-except** block for input validation.
* Enhance **error handling** (e.g., non-integer input for choice/amount).
* Improve **transaction logging** by moving the logging logic inside the `send_money` function and including timestamps.
* Add a function to view the `transaction_history`.
* Implement a **user creation/registration** feature.
* Use a more secure method than hardcoded dictionary for user data (e.g., a simple file or database).
