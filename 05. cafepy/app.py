
def coffee_machine():

    print("☕ Coffee Machine is ON. Ready to take orders!")

    try:
        while True:
            order = yield "\n👉 Please place your coffee order..."

            if order.lower() == "espresso":
                print("✅ Brewing Espresso...")
            
            elif order.lower() == "cappuccino":
                print("✅ Brewing Cappuccino with foam...")

            elif order.lower() == "matcha latte":
                print("✅ Brewing Matcha Latte with cream..")

            elif order.lower() == "exit":
                print("👋 Thanks for using the Coffee Machine!")

                break
            
            else:
                print(f"❌ Sorry, we don't have '{order}'. Try Espresso/Cappuccino/Matcha Latte.")

    except GeneratorExit:
        print("🔴 Coffee Machine shutting down... Goodbye!")

       
machine = coffee_machine()

print(next(machine)) #start generator

while True:
    
    order = input("Your order (or type 'exit' to quit): ")

    if order.lower() == "exit":
        machine.close()
        break

    else:
        print(machine.send(order))
