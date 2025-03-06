def add_expense(expenses, amount, category):
    """Adiciona uma despesa à lista de despesas."""
    expenses.append({'amount': amount, 'category': category})

def print_expenses(expenses):
    """Exibe todas as despesas."""
    for expense in expenses:
        print(f'Amount: {expense["amount"]}, Category: {expense["category"]}')

def total_expenses(expenses):
    """Calcula o total de despesas."""
    return sum(expense['amount'] for expense in expenses)

def filter_expenses_by_category(expenses, category):
    """Filtra despesas por categoria."""
    return [expense for expense in expenses if expense['category'] == category]

def get_expense_input():
    """Solicita ao usuário o valor e a categoria da despesa."""
    while True:
        try:
            amount = float(input('Enter amount: '))
            if amount < 0:
                print("O valor da despesa deve ser um número positivo.")
                continue
            category = input('Enter category: ')
            return amount, category
        except ValueError:
            print("Entrada inválida. Insira um número válido para o valor.")

def main():
    expenses = []
    while True:
        print('\nExpense Tracker')
        print('1. Add an expense')
        print('2. List all expenses')
        print('3. Show total expenses')
        print('4. Filter expenses by category')
        print('5. Exit')

        choice = input('Enter your choice: ')

        if choice == '1':
            amount, category = get_expense_input()
            add_expense(expenses, amount, category)

        elif choice == '2':
            print('\nAll Expenses:')
            print_expenses(expenses)

        elif choice == '3':
            print('\nTotal Expenses: ', total_expenses(expenses))

        elif choice == '4':
            category = input('Enter category to filter: ')
            print(f'\nExpenses for {category}:')
            expenses_from_category = filter_expenses_by_category(expenses, category)
            print_expenses(expenses_from_category)

        elif choice == '5':
            print('Exiting the program.')
            break
        else:
            print('Invalid choice. Try again.')

if __name__ == "__main__":
    main()
