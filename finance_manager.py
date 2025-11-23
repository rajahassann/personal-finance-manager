def get_monthly_finances():
    finances = {
        'balance': 0,
        'income': 0,
        'fixed_costs': {},
        'spending_limits': {},
        'actual_spending': {}
    }

    print("--- Personal Finance Manager ---")
    print("Let's set up your monthly budget\n")

    finances['balance'] = float(input("Starting balance: "))
    finances['income'] = float(input("Monthly income: "))

    print("\n--- Fixed Monthly Costs ---")
    finances['fixed_costs']['rent'] = float(input("Rent: "))
    finances['fixed_costs']['utilities'] = float(input("Utilities: "))
    finances['fixed_costs']['transport'] = float(input("Transport costs: "))

    print("\n--- Spending Limits ---")
    finances['spending_limits']['grocery'] = float(input("Grocery Limit: "))

    return finances


def calculate_budget(finances):
    # Calculate fixed costs total
    fixed_total = 0
    for cost in finances['fixed_costs'].values():
        fixed_total += cost

    money_left = finances['income'] - fixed_total
    savings = money_left - finances['spending_limits']['grocery']

    return money_left, savings


def track_spending(finances, savings):
    finances['actual_spending']['grocery'] = float(input("\nGrocery expenditure this Month: "))
    finances['actual_spending']['misc'] = float(input("Misc expenses: "))

    # Check grocery budget
    grocery_overspend = finances['actual_spending']['grocery'] - finances['spending_limits']['grocery']
    if grocery_overspend > 0:
        savings -= grocery_overspend
        print(f"⚠️  Over grocery limit by {grocery_overspend}")

    # Subtract misc spending
    savings -= finances['actual_spending']['misc']

    # New Balance
    finances['balance'] += savings

    # Handle negative savings
    if savings < 0:
        print(f"⚠️  Used {abs(savings)} from balance")

    return finances, savings


def main():
    my_finances = get_monthly_finances()
    money_left, current_savings = calculate_budget(my_finances)

    print(f"\n--- Budget Summary ---")
    print(f"Money left after fixed costs: {money_left}")
    print(f"Projected savings: {current_savings:}")

    # Track actual spending
    print("\n--- Actual Spending ---")
    my_finances, final_savings = track_spending(my_finances, current_savings)

    print(f"\n--- Final Results ---")
    print(f"Current balance: {my_finances['balance']}")
    print(f"Money Saved This Month: {final_savings}")

    # Show all data stored in dictionaries
    print(f"\n--- All Data ---")
    print(f"Fixed costs: {my_finances['fixed_costs']}")
    print(f"Spending limits: {my_finances['spending_limits']}")
    print(f"Actual spending: {my_finances['actual_spending']}")


if __name__ == "__main__":
    main()