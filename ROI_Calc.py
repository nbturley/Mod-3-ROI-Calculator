'''
Create a program that will calculate the Return on Investment(ROI) for a rental property.

Methods:
    - Total Monthly Income
    - Expenses
    - Monthly Cashflow
    - Cash on Cash ROI

'''

class InvestmentProperty():

    def __init__(self):
        self.income = {}
        self.expenses = {}
        self.investments = {}
        self.monthly_income = 1
        self.monthly_expenses = 1

    def totalMonthlyIncome(self):
        self.income['rental income'] = int(input('\nWhat is the monthly rental income? '))
        self.income['laundry income'] = int(input('What is the monthly laundry income? '))
        self.income['storage income'] = int(input('What is the monthly storage income? '))
        self.income['misc. income'] = int(input('What is the monthly misc. income? '))

        self.monthly_income = sum(self.income.values())
        print(self.income)

        while True:
            answer = input('\nWould you like to change any income? yes/no ')
            if answer.lower() == 'yes':
                income = input('What expense would you like to change? ')
                value = input('What is the new value? ')
                self.income[income.lower()] = int(value)
                self.monthly_income = sum(self.income.values())
                print(self.income)
            elif answer.lower() == 'no':
                break
            else:
                print('Invalid response. Please try again.')
        
        f'\nTotal Monthly Income: {self.monthly_income}'

        return self.monthly_income 

    def totalMonthlyExpenses(self):
        self.expenses['taxes'] = int(input('\nWhat is the monthly tax payment? '))
        self.expenses['insurance'] = int(input('What is the monthly insurance payment? '))
        self.expenses['eletric'] = int(input('What is the monthly electric payment? '))
        self.expenses['water'] = int(input('What is the monthly water payment? '))
        self.expenses['sewer'] = int(input('What is the monthly sewer payment? '))
        self.expenses['garbage'] = int(input('What is the monthly garbage payment? '))
        self.expenses['gas'] = int(input('What is the monthly gas payment? '))
        self.expenses['hoa'] = int(input('What is the monthly HOA fee? '))
        self.expenses['lawn'] = int(input('What is the monthly landscaping cost? '))
        self.expenses['vacancy'] = int(input('What is this properties vacancy rate? '))
        self.expenses['repairs'] = int(input('How much will you set aside monthly for repairs? '))
        self.expenses['capex'] = int(input('How much will you set aside monthly for capital expenditures?(roof, HVAC, ets.) '))
        self.expenses['mortgage'] = int(input('What is the monthly mortgage payment? '))
        self.expenses['prop_mgmt'] = int(input('What is the monthly property management cost? '))

        self.monthly_expenses = sum(self.expenses.values())
        print(self.expenses)

        while True:
            answer = input('\nWould you like to change any expenses? yes/no ')
            if answer.lower() == 'yes':
                expense = input('What expense would you like to change? ')
                value = input('What is the new value? ')
                self.expenses[expense.lower()] = int(value)
                self.monthly_expenses = sum(self.expenses.values())
                print(f'\nTotal Monthly Expenses: {self.monthly_expenses}')
            elif answer.lower() == 'no':
                break
            else:
                print('Invalid response. Please try again.')

        f'\nTotal Monthly Expenses: {self.monthly_expenses}'

        return self.monthly_expenses

    def totalMonthlyCashflow(self, monthly_income, monthly_expenses):
        monthly_cashflow = monthly_income - monthly_expenses
        self.annual_cashflow = monthly_cashflow * 12

        return self.annual_cashflow

    def cashROI(self, annual_cashflow):
        self.investments['down payment'] = int(input('\nWhat is your downpayment? '))
        self.investments['closing'] = int(input('What are your closing costs? '))
        self.investments['rehab'] = int(input('What is your rehab budget? '))
        self.investments['misc'] = int(input('What was are you other miscellaneous costs? '))

        total_investment = sum(self.investments.values())
        print(self.investments)

        while True:
            answer = input('\nWould you like to change any investments? yes/no ')
            if answer.lower() == 'yes':
                expense = input('What investment would you like to change? ')
                value = input('What is the new value? ')
                self.expenses[expense.lower()] = int(value)
                total_investment = sum(self.investments.values())
            elif answer.lower() == 'no':
                break
            else:
                print('Invalid response. Please try again.')

        cash_roi = annual_cashflow / total_investment * 100

        print(f'\nCash ROI: {cash_roi}')
        return cash_roi

firstProperty = InvestmentProperty()

def run():
    while True:
        action = input('\nWould you like to calculate a new ROI, display values or close? calculate/display/close ')

        if action.lower() == 'calculate':
            firstProperty.totalMonthlyIncome()
            firstProperty.totalMonthlyExpenses()
            firstProperty.totalMonthlyCashflow(firstProperty.monthly_income, firstProperty.monthly_expenses)
            firstProperty.cashROI(firstProperty.annual_cashflow)

        elif action.lower() == 'display':
            selection = input('Choose what you would like to display from the following: Income/Expenses/Investments ')
            if selection.lower() == 'income':
                print(firstProperty.income)
            elif selection.lower() == 'expenses':
                print(firstProperty.expenses)
            elif selection.lower() == 'investments':
                print(firstProperty.investments)
            else:
                print(f'Sorry {selection} is an invalid repsonse. Please try again.')

        elif action.lower() == 'close':
            print('Thank you. Have a nice day!')
            break

        else:
            print(f'Sorry {action} is not recgonized please try again.')

run()

# print(firstProperty.totalMonthlyIncome())
# print(firstProperty.totalMonthlyExpenses())
# print(firstProperty.totalMonthlyCashflow())
# print(firstProperty.cashROI(firstProperty.totalMonthlyCashflow()))