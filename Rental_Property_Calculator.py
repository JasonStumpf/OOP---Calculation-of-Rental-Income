class Rental_property_calculator():

    def __init__(self):
        self.rental_income = 0
        self.property_expenses = 0
        self.current_cash_flow = 0

    def income(self):
        self.rental_income = input("\nWhat is your monthy rental income: ")
        question = input("Do you have any additional related income (Laundry, Storage, etc.): ")
        if question.lower() == 'yes' or question.lower() == 'y':
            extra = input("How much is it: ")
            self.rental_income = int(self.rental_income) + int(extra)
            print(f"Your total income is ${self.rental_income}")
        elif question.lower() == 'no' or question.lower() == 'n':
            print(f"Your total income is ${self.rental_income}")

    def expenses(self):
        self.property_expenses = input("\nWhat is your total monthy expenses: ")
        print(f"Your total expenses is ${self.property_expenses}")

    def cash_flow(self):
        self.current_cash_flow = int(self.rental_income) - int(self.property_expenses)
        print(f"Based on the info, your monthly cash flow is ${self.current_cash_flow}.")

    def return_on_investment(self):
        self.current_cash_flow = int(self.rental_income) - int(self.property_expenses)
        annual = (self.current_cash_flow * 12)
        total = input("\nWhat was the total amount of the investment: ")
        roi = ((int(annual) / int(total)) * 100)
        print(f"Your cash on cash ROI is {roi}%")

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