class Machine:
    def __init__(self, products: dict, amount: int) -> None:
        self.products = products

        #setting initial amount
        self.amount = amount
        for i in self.products:
            self.products[i]["amount"] = self.amount

        #options
        self.adminOptions = {"add_product": self.add_product, "exit": self.exit, "withdraw": self.withdraw}
        self.userOptions = {"add_money": self.add_money, "stop": self.exit}
        
        #mode
        self.setMode : bool = False
        self.userMode = False
        self.adminMode = False
        self.modes = {"user": self.set_user, "admin": self.set_admin}

        #Cash
        self.machineCash = 0
        self.userCash = 0

        self.initialStage = True


    #running machine
    def run(self) -> None:
        if self.initialStage:
            self.initialStage = False
            self.display()

        if not self.setMode:
            self.set_mode()
        elif self.userMode:
            self.user_select()
        elif self.adminMode:
            self.admin_select()

        print("\n"*30) #for clearing screen
        self.initialStage = True


    #selections
    def user_select(self) -> None:
        selections = self.products | self.userOptions
        selected = "_".join(input("Select Options or Products [only one is allowed]: ").split())

        err = f"Warning[Invalid Input(Selection not recognized)]: Please try again. \n[Valid Selections]: [{'], ['.join(selections.keys()).replace("_", " ").upper()}]"

        if selected in self.products:
            self.get_product(selected)
        elif selected in self.userOptions:
            self.options(self.userOptions, selected)
        else:
            raise Exception(err)

    def admin_select(self) -> None:
        selected = "_".join(input("Select Options [only one is allowed]: ").split())
        self.options(self.adminOptions, selected)

    def options(self, options: dict, option: str) -> None:
        err = f"Warning[Option not recognized]: Please try again.] \n [Valid Options]: [{'], ['.join(options.keys()).replace("_", " ").upper()}]"

        self.check_input(options, option, err)
        options[option]()


    #get product for user
    def get_product(self, product) -> None:
        err = "Warning[Invalid Input(product name)]: please enter valid product name"
        self.check_input(self.products, "_".join(product.split()).lower(), err)

        if self.products[product]["amount"] == 0:
            raise Exception("Warning[Invalid Product]: Please enter valid product name")
        elif self.products[product]["price"] > self.userCash:
            raise Exception("Warning[Insufficient balance]: Please add more money to complete your purchase.")

        price = self.products[product]["price"]

        #transaction
        self.userCash -= price
        self.machineCash += price

        self.products[product]["amount"] -= 1


    #changing staffs
    def add_product(self) -> None:
        product = input("Enter Product Name: ")

        err = "Warning[Invalid Input]: please enter valid product name"
        self.check_input(self.products, product.replace(" ", "").lower(), err)

        amount = self.input_amount()

        if amount <= 0:
            raise Exception("Warning[Invalid amount]:Amount must be greater than 0")
        self.products[product]["amount"] += amount

    def add_money(self) -> None:
        amount = self.input_amount()

        if amount <= 0:
            raise Exception("Warning[Invalid amount]:Amount must be greater than 0")
        self.userCash += amount

    def withdraw(self) -> None:
        amount = self.input_amount()

        if amount <= 0:
            raise Exception("Warning[Invalid amount]: Amount must be greater than 0")
        if amount > self.machineCash:
            raise Exception("Warning[Not enough money left!]: Amount cannot be greater than the machine's cash")
        self.machineCash -= amount


    #displaying
    def display(self):
        if self.userMode:
            self.user_menu()
        elif self.adminMode:
            self.admin_menu()
        else:
            self.main_menu()
        print()

    def admin_menu(self) -> None:
        print("Admin Menu" + "\n" + "-" * 28)

        for product in self.products:
                print(f"{product.replace("_", " ").upper():<15} {self.products[product]["price"]:>3} TL "
                      f"| Stock: {self.products[product]["amount"] if self.products[product]["amount"] != 0 else "[run out of stock] refill it!!"}")

        print("\n" + "Admin Options" + "\n" + "-" * 28)
        for option in self.adminOptions:
            print(f"{option.replace("_", " ").upper()}")
        print("-" * 28)

        print(f"Cash in Machine: {self.machineCash} TL")
        print("-" * 28)

    def user_menu(self) -> None:
        print("User Menu" + "\n" + "-" * 28)

        out_stock = True

        for product in self.products:
            if self.products[product]["amount"] != 0:
                print(f"{product.replace("_", " ").upper():<15} {self.products[product]["price"]:>3} TL | Stock: {self.products[product]["amount"]}")
                out_stock = False

        if out_stock:
            print("Ops all of the products out of stck!!")

        #options
        print("\n" + "User Options" + "\n" + "-" * 28)
        for option in self.userOptions:
            print(f"{option.replace("_", " ").upper()}")
        print("-" * 28)

        print(f"Your Current Balance: {self.userCash} TL")
        print("-" * 28)

    def main_menu(self) -> None:
        print("Welcome to the Vending Machine!")
        print("-" * 28)
        print("Modes:")
        for mode in self.modes:
            print(" "*6 + f"{mode.replace("_", " ").upper()}")

    #helping static methods
    @staticmethod
    def check_input(opt: dict, inp: str, err: str) -> None:
        if inp not in opt:
            raise Exception(f"{err}")

    @staticmethod
    def input_amount() -> int:
        try:
            amount = int(input("Enter Amount: "))
        except ValueError:
            raise Exception("Warning[Invalid Input]: please enter number only")
        return amount


    # modes
    def set_admin(self) -> None:
        self.userMode = False
        self.adminMode = True

    def set_user(self) -> None:
        self.adminMode = False
        self.userMode = True

    def exit(self) -> None:
        self.adminMode = False
        self.userMode = False
        self.setMode = False

    def set_mode(self) -> None:
        mode = input("Enter Mode: ").replace(" ", "").lower()
        err = f"Warning[Invalid Input]: please enter valid mode\nValid modes are: [Admin] or [User]"
        self.check_input(self.modes, mode, err)
        self.setMode = True
        self.modes[mode]()
