from budget import Budget

print("Personal Finance Manager")
print("Version 1.1")

my_budget = Budget("December")

my_budget.setup()

money_left, savings = my_budget.calculate()

print("\nBudget summary:")
print("Money after fixed costs: " + str(money_left))
print("Expected savings: " + str(savings))

final_savings = my_budget.track()

print("\nFinal results:")
print("Current balance: " + str(my_budget.balance))
print("Money saved: " + str(final_savings))

my_budget.save()

print(my_budget.show_report())

print("\nAll data:")
print("Fixed: " + str(my_budget.fixed_costs))
print("Limits: " + str(my_budget.spending_limits))
print("Spent: " + str(my_budget.actual_spending))