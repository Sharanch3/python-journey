# ☕ Coffee Machine Generator

A Python project demonstrating **generator functions** and **coroutines** through an interactive coffee machine simulation.

---

## 📋 Problem Statement

Traditional functions execute from start to finish in one go. However, many real-world scenarios require:
- **Stateful interactions** - remembering previous states between operations
- **Two-way communication** - sending data back and forth
- **Pause and resume capability** - stopping execution and continuing later
- **Resource management** - proper cleanup when stopping

**Challenge:** Create an interactive system that can:
1. Maintain state across multiple user interactions
2. Accept user input dynamically during execution
3. Process commands continuously without restarting
4. Handle graceful shutdown with cleanup

**Solution:** This project uses Python **generator functions** with the `yield` statement to create a stateful, interactive coffee machine that demonstrates coroutines in action.

---

## 🎯 Features

- ☕ **Interactive Coffee Ordering** - Take continuous coffee orders
- 🔄 **Stateful Execution** - Maintains state between orders
- 📨 **Two-way Communication** - Send orders and receive responses
- 🛡️ **Error Handling** - Graceful shutdown with proper cleanup
- 📝 **Input Validation** - Handles invalid orders with helpful messages
- 🚪 **Multiple Exit Methods** - Normal exit and forced shutdown


## 📦 Requirements

- **Python Version:** 3.x or higher
- **Dependencies:** None (uses only built-in Python features)

---

## 🚀 Installation & Usage

### **1. Clone or Download**
```bash
# Save the code to a file named coffee_machine.py
```

### **2. Run the Program**
```bash
python app.py

### **Generator Lifecycle**

```
┌─────────────────────────────────────────────────┐
│ 1. CREATE: machine = coffee_machine()          │
│    → Prints "Coffee Machine is ON"             │
└─────────────────────────────────────────────────┘
                    ↓
┌─────────────────────────────────────────────────┐
│ 2. START: next(machine)                         │
│    → Runs until first yield                     │
│    → Returns prompt message                     │
└─────────────────────────────────────────────────┘
                    ↓
┌─────────────────────────────────────────────────┐
│ 3. INTERACT: machine.send("espresso")           │
│    → Resumes from yield                         │
│    → Processes order                            │
│    → Loops back to yield                        │
│    → Returns new prompt                         │
└─────────────────────────────────────────────────┘
                    ↓
┌─────────────────────────────────────────────────┐
│ 4. CLOSE: machine.close()                       │
│    → Raises GeneratorExit exception             │
│    → Executes cleanup code                      │
│    → Generator terminates                       │
└─────────────────────────────────────────────────┘

---
### 🎓 Learning Outcomes
This project teaches:

1. ✅ **Generator Functions** — Creating pausable functions  
2. ✅ **Coroutines** — Two-way communication with generators  
3. ✅ **State Management** — Maintaining data between calls  
4. ✅ **Exception Handling** — Managing generator lifecycle  
5. ✅ **Interactive Programming** — Building responsive CLI applications  
6. ✅ **Control Flow** — Using `yield` for program flow control  

---

### 📄 License
This project is open source and available for educational purposes.

---

### 👨‍💻 Author
Created as an educational demonstration of Python generators and coroutines.

---

### 🤝 Contributing
Feel free to fork this project and add your own features:

- More drink options  
- Payment system  
- Inventory management  
- Custom drink builder  
- Save order history to file  

---

### ⭐ Support
If you found this educational project helpful, please give it a star! ⭐

---

**Happy Coding! ☕️🐍**
---

**Happy Coding! ☕️🐍**
