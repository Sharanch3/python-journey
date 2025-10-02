# 🏦 ATM Simulation using OOP in Python

This project simulates a simple **ATM System** while demonstrating **Object-Oriented Programming (OOP)** principles in Python.

---

## 🚀 Features
- 🔑 **PIN Management** – Create and change secure 4-digit PINs  
- 💰 **Balance Handling** – Check and update account balance  
- 💳 **Withdrawals** – Secure money withdrawal with PIN verification  
- 📊 **Account Tracking** – Class method to show total accounts in the bank  
- 📜 **ATM Guidelines** – Static method for safe ATM usage instructions  

---

## 🛠 OOP Concepts Used

1. **Inheritance**  
   - `Atm` inherits from `BankAccount`.

2. **super()**  
   - Used in `Atm.__init__()` to call parent (`BankAccount`) constructor.

3. **Getter & Setter (@property)**  
   - Securely manage **PIN** with validation.

4. **Class Method (@classmethod)**  
   - Tracks and displays total number of accounts created.

5. **Static Method (@staticmethod)**  
   - Provides ATM safety guidelines.

---


