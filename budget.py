import json
import os


class Budget:
    def __init__(self, month):
        self.month = month
        self.balance = 0
        self.income = 0
        self.fixed_costs = {}
        self.spending_limits = {}
        self.actual_spending = {}
        self.daily_spending = []

    def setup(self):
        print("Setting up budget for " + self.month)
        self.balance = float(input("Starting balance: "))
        self.income = float(input("Monthly income: "))

        print("\nFixed costs:")
        rent = float(input("Rent: "))
        utilities = float(input("Utilities: "))
        transport = float(input("Transport: "))

        self.fixed_costs = {
            'rent': rent,
            'utilities': utilities,
            'transport': transport
        }

        print("\nSpending limits:")
        grocery_limit = float(input("Grocery limit: "))
        self.spending_limits['grocery'] = grocery_limit

        self.actual_spending['grocery'] = 0
        self.actual_spending['misc'] = 0

    def calculate(self):
        fixed_total = self.fixed_costs['rent'] + self.fixed_costs['utilities'] + self.fixed_costs['transport']
        money_left = self.income - fixed_total
        savings = money_left - self.spending_limits['grocery']
        return money_left, savings

    def add_expense(self, day, what, amount):
        expense = {
            'day': day,
            'what': what,
            'amount': amount
        }
        self.daily_spending.append(expense)

        if what == 'grocery':
            self.actual_spending['grocery'] += amount
        else:
            self.actual_spending['misc'] += amount

    def track(self):
        print("\nTrack spending for " + self.month)
        grocery = float(input("Grocery spent: "))
        misc = float(input("Other spending: "))

        self.actual_spending['grocery'] = grocery
        self.actual_spending['misc'] = misc

        money_left, savings = self.calculate()

        if grocery > self.spending_limits['grocery']:
            over = grocery - self.spending_limits['grocery']
            savings = savings - over
            print("Over grocery limit by " + str(over))

        savings = savings - misc
        self.balance = self.balance + savings

        if savings < 0:
            print("Used " + str(abs(savings)) + " from balance")

        return savings

    def save(self):
        filename = self.month.replace(" ", "_") + ".json"

        data = {
            'month': self.month,
            'balance': self.balance,
            'income': self.income,
            'fixed': self.fixed_costs,
            'limits': self.spending_limits,
            'spent': self.actual_spending,
            'daily': self.daily_spending
        }

        with open(filename, 'w') as f:
            json.dump(data, f)

        print("Saved to " + filename)

    def load(self, filename):
        if os.path.exists(filename):
            with open(filename, 'r') as f:
                data = json.load(f)

            self.month = data['month']
            self.balance = data['balance']
            self.income = data['income']
            self.fixed_costs = data['fixed']
            self.spending_limits = data['limits']
            self.actual_spending = data['spent']
            self.daily_spending = data['daily']

            print("Loaded from " + filename)
            return True
        else:
            print("File not found")
            return False

    def show_report(self):
        money_left, savings = self.calculate()

        report = "\nReport for " + self.month + "\n"
        report += "Balance: " + str(self.balance) + "\n"
        report += "Income: " + str(self.income) + "\n"
        report += "Money left after fixed: " + str(money_left) + "\n"
        report += "Savings: " + str(savings) + "\n"

        report += "\nFixed costs:\n"
        for name, cost in self.fixed_costs.items():
            report += name + ": " + str(cost) + "\n"

        return report