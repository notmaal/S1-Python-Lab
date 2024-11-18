class bankAcc:
    user_count = 1000
    def __init__(self):
        bankAcc.user_count += 1
        self.name = str()
        self.acc_no = bankAcc.user_count
        self.age = int()
        self.balance = 0.0

    def check_balance(self):
        return self.balance

if __name__ == "__main__":
    is_running = 1  
    print("Welcome to Maal's Bank...")
    user = bankAcc()
    user.name = input("Enter your name: ")
    user.age = input("Enter your age: ")
    while(is_running):
        choice = int(input("\n\nWhat would u like to do?\n1.Deposit Money\n2.Withdraw Money\n3.Check Balance\nPress 0 to exit...\nEnter your choice: "))
        print("\n")
        match(choice):
            case 0:
                is_running = 0
            case 1:
                to_add = float(input("Enter the amount to add: "))
                user.balance += to_add
                print(f"{to_add} has been credited to your acc")
            case 2:
                to_withdraw = float(input("Enter the amount to withdraw: "))
                if user.balance < to_withdraw:
                    print("!! Not Enough Balance !!")
                else:
                    user.balance -= to_withdraw
                    print(f"{to_withdraw} has been credited from your account")
            case 3:
                print(f"Your balance for Acc no: {user.acc_no} is {user.balance}")