
# Account Statement Overview

This document provides a simple, high-level view of account activities based on the transactions recorded in the `transaction_history` list during the simulation run.

## Key Account Holders in Simulation

* **Madhav**
* **Arjun**

## Transaction Summary

This summary reflects all transactions successfully completed during the last execution of the `phonepe_simulation.py` script.

| Type | From | To | Amount (₹) |
| :--- | :--- | :--- | :--- |
| Debit/Sent | (Sender) | (Receiver) | (Amount) |
| Credit/Received | (Receiver) | (Sender) | (Amount) |

***Note:*** *The actual transaction history for this statement will be generated dynamically by the script after a successful transaction. Since the provided Python code appends to `transaction_history` after the main choice block, this file serves as a template for displaying that data.*

### Example Statement Entry (If Madhav sent ₹500 to ARJUN)

If a transaction occurred where  Madhav sent ₹500 to ARJUN, the statement would conceptually show:

* ** Madhav's View:** A **Debit** of ₹500 to ARJUN .
* **ARJUN's View:** A **Credit** of ₹500 from  Madhav.

---

## Technical Details

* **Source of Data:** `transaction_history` list in the Python script.
* **Current Logging Fields:** `from`, `to`, `amount`.
* **Limitations:** This simulation does not currently store historical statements permanently (data is lost upon script termination). It only captures transactions executed in the current session.
