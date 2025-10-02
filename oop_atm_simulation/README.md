# 🏦 ATM Banking System

A Python-based ATM simulation system demonstrating Object-Oriented Programming (OOP) concepts including inheritance, encapsulation, properties, and method decorators.

---

## 📋 Problem Statement

### Challenge
Design and implement a simple ATM banking system that allows users to:
- Create and manage their PIN securely
- Check their account balance
- Withdraw money from their account
- Track the total number of bank accounts created

### Requirements
1. **Account Management**: Each account should have a unique card number and balance
2. **PIN Security**: Users must create a 4-digit PIN to access their account
3. **PIN Validation**: System should validate PIN format (must be exactly 4 digits)
4. **Authentication**: All sensitive operations require PIN verification
5. **Balance Management**: Users can check balance and withdraw funds
6. **Insufficient Funds Check**: Prevent withdrawals that exceed available balance
7. **Account Tracking**: System should track total number of accounts created
8. **User Interface**: Provide an interactive menu-driven interface

---

## 🎯 Learning Objectives

This project demonstrates:
- **Classes and Objects**: Creating blueprints and instances
- **Inheritance**: `Atm` class inherits from `BankAccount` class
- **Encapsulation**: Protected attributes (e.g., `_pin`)
- **Properties**: Getter and setter methods with validation
- **Class Variables**: Shared data across all instances
- **Class Methods**: Methods that work on class-level data
- **Static Methods**: Utility functions within a class
- **Method Types**: Instance, class, and static methods

---

## 🚀 Features

### Core Functionality
- ✅ **Create PIN**: Set up a new 4-digit PIN with validation
- ✅ **Change PIN**: Update existing PIN with old PIN verification
- ✅ **Check Balance**: View current account balance (PIN required)
- ✅ **Withdraw Money**: Withdraw funds with balance verification (PIN required)
- ✅ **Account Counter**: Track total number of accounts in the system

### Security Features
- 🔒 PIN must be exactly 4 digits
- 🔒 PIN required for all sensitive operations
- 🔒 Old PIN verification required to change PIN
- 🔒 Protected `_pin` attribute (not directly accessible)

---

## 📁 Project Structure

```
atm-banking-system/
│
├── app.py          # Main program file
└── README.md              # Project documentation
```

---

## 🏗️ Code Architecture

### Class Diagram

```
BankAccount (Parent Class)
├── Attributes:
│   ├── total_accounts (class variable)
│   ├── card_number
│   ├── _pin (protected)
│   └── balance
├── Methods:
│   ├── __init__(card_number, balance)
│   ├── pin (property getter)
│   ├── pin.setter (property setter with validation)
│   ├── get_total_accounts() (class method)
│   └── atm_guidelines() (static method)
│
└── Atm (Child Class - Inherits from BankAccount)
    ├── Methods:
    │   ├── __init__(card_number)
    │   ├── menu()
    │   ├── create_pin()
    │   ├── change_pin()
    │   ├── check_balance()
    │   └── withdraw()
```

---

## 🔑 Key OOP Concepts

### 1. **Inheritance**
```python
class Atm(BankAccount):  # Atm inherits from BankAccount
```

### 2. **Encapsulation**
```python
self._pin = None  # Protected attribute (single underscore convention)
```

### 3. **Property Decorators**
```python
@property
def pin(self):
    return self._pin

@pin.setter
def pin(self, new_pin):
    # Validation logic
```

### 4. **Class Variables**
```python
total_accounts = 0  # Shared across all instances
```

### 5. **Class Methods**
```python
@classmethod
def get_total_accounts(cls):
    return f"Total accounts: {cls.total_accounts}"
```

### 6. **Static Methods**
```python
@staticmethod
def atm_guidelines():
    return "Use a 4-digit PIN..."
```
**Happy Coding! 🚀**


