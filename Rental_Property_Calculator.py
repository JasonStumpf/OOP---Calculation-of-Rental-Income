class Rental_property_calculator():

    def __init__(self):
        self.rental_income = 0
        self.property_expenses = 0
        self.current_cash_flow = 0

    def income(self):
        self.rental_income = input("\nWhat is your monthy rental income: ")
        question1 = input("Do you have any additional related income (Laundry, Storage, etc.): ")
        if question1.lower() == 'yes' or question1.lower() == 'y':
            extra1 = input("How much is it: ")
            self.rental_income = int(self.rental_income) + int(extra1)
            print(f"Your total monthly income is ${self.rental_income}")
        elif question1.lower() == 'no' or question1.lower() == 'n':
            print(f"Your total monthly income is ${self.rental_income}")

    def expenses(self):
        diary_exp = {}
        print("\nEnter your expenses, than enter how much they cost. Type DONE when finished.")
        while True:
            key = input("What expense do you have: ")
            if key.lower() == 'done':
                break
            value = input("How much does that cost: ")
            diary_exp[key] = value
            
        for x in diary_exp.values():
            self.property_expenses += int(x)
        print(f"\nYour total monthly expenses is ${self.property_expenses}")

    def cash_flow(self):
        self.current_cash_flow = int(self.rental_income) - int(self.property_expenses)
        print(f"Based on the info, your monthly cash flow is ${self.current_cash_flow}.")

    def return_on_investment(self):
        self.current_cash_flow = int(self.rental_income) - int(self.property_expenses)
        annual = (self.current_cash_flow * 12)
        print("\nBefore getting your ROI, you'll need to enter the amount of money that you put down for the property.")
        while True:
            d_p = input("\nHow much was the down payment: ")
            c_c = input("How much was the closing cost: ")
            question2 = input("Where there any additional money spect (Rehbas, etc.): ")
            if question2.lower() == 'yes' or question2.lower() == 'y':
                extra2 = input("How much was it: ")
                total = (int(d_p) + int(c_c) + int(extra2))
                print(f"Your total investment was {total}")
                break
            elif question2.lower() == 'no' or question2.lower() == 'n':
                total = (int(d_p) + int(c_c))
                print(f"Your total investment was {total}")
                break  
        roi = ((int(annual) / int(total)) * 100)
        print(f"\nYOUR CASH ON CASH RETURN ON INVESTMENT IS {roi}%")

landlord = Rental_property_calculator()

def run_calculator():
    print("\nWELCOME TO THE RETURN.ON.INVESTMENT CALCUTAOR - This program will help you determine your ROI based on information you give it.")
    print("\nFirst, you'll need to enter both your Income and Expenses (TYPE Income or Expenses), once both pieces of informations are in you'll be able to calculate your ROI (TYPE ROI).")
    print("At any point you can see your monthly Cash Flow (TYPE Cash Flow), you can also quit the program when you are finished using it (TYPE Quit).")      
          
    while True:
        response = input("\nWhat would you like to do? (Income/Expenses/ROI/Cash Flow/Quit): ")
        if response.lower() == 'income':
            landlord.income()
            continue
        elif response.lower() == 'expenses':
            landlord.expenses()
            continue
        elif response.lower() == 'roi':
            landlord.return_on_investment()
            continue
        elif response.lower() == 'cash flow':
            landlord.cash_flow()
            continue
        elif response.lower() == 'quit':
            break
        else:
            print("That is not a valid response.")
            continue

run_calculator()