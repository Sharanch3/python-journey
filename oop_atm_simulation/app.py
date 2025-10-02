class BankAccount:
    #class variable (shared by all accounts)
    total_accounts = 0

    def __init__(self, card_number, balance = 1000):
        self.card_number = card_number
        self.balance = balance
        self.__pin = None  #protected attribute
        BankAccount.total_accounts += 1

        print(f"🏦 Bank account created for card {self.card_number}")


    @property
    def pin(self):
        return self.__pin  

    @pin.setter
    def pin(self,new_pin):
        if len(new_pin) == 4 and new_pin.isdigit():
            self.__pin = new_pin
            print("✅ Pin successfully set!")

        else:
            print("❌ Invalid Pin, Pin must be of 4 digit.")


    @classmethod #shows total account 
    def get_total_accounts(cls):
        return f"Total accounts in bank: {cls.total_accounts}"
    
    @staticmethod
    def atm_guidelines():
        return f"💡 Use a 4-digit PIN. Keep it safe! Never share it."
    


class Atm(BankAccount):
    def __init__(self, card_number, balance=1000):
        super().__init__(card_number, balance)
        print("🔌✅ Connected to bank's backend server ")
        print(f" Card {self.card_number} recognized. Account ready!")

        self.menu()
    

    def menu(self):
        user_input = input('''
        How can I help you?
        1. Press 1 to create pin
        2. Press 2 to change pin
        3. Press 3 to check balance
        4. Press 4 to withdraw
        5. Or 'q' to exit
        
        ENTER: ''')

        if user_input =='1':
            self.create_pin()
        
        elif user_input == '2':
            self.change_pin()
            
        elif user_input == '3':
            self.check_balance()

        elif user_input == '4':
            self.withdraw()

        else:
            print("Exitng ATM... Have a nice day!")

    
    def create_pin(self):
        user_pin = input("Enter your pin: ")
        self.pin = user_pin #uses setter

        user_balance = int(input("Enter your balance: "))
        self.balance = user_balance

        print("✅ Pin succesfully created!")

        self.menu()


    def change_pin(self):
        old_pin = input("Enter your existing Pin: ")

        if old_pin == self.pin:
            new_pin = input("Enter your new Pin: ")  
            
            self.pin = new_pin

            print("✅ Pin changed succesfully!")


        else:
            print("Enter your existing Pin in order to change our pin.")
        
        
        self.menu()
          

    def check_balance(self):

        user_pin = input("Enter your Pin: ")
        
        if self.pin == user_pin:
            print(f"Your exising balance is: ${self.balance}")
            
        else:
            print("Incorrect Pin!")
        
        
        self.menu()


    def withdraw(self):
         user_pin = input("Enter your Pin: ")

         if user_pin == self.pin:
            amount = int(input("Enter your amount: "))

            if amount <= self.balance:
                self.balance -= amount
                print(f"✅ Your transaction of ${amount} is sucessfull!")
                print(f"Remaming Balance: ${self.balance}")
                

            else:
                print("Insufficiet Balance:(")

         
         else:
             print("Invalid Pin!")
            
         self.menu()



    



if __name__ == "__main__":
    
    print(BankAccount.atm_guidelines())   # static method
    print(BankAccount.get_total_accounts())  # before creating any account
    obj = Atm(card_number="1234560")
    print(BankAccount.get_total_accounts())  # after creating account
    

