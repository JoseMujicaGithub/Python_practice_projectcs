def validate_input_num(input_description=": "): 
    while True:
        try:
            num=float(input(input_description))
        except:
            print('===Invalid Input===')
            continue
        if type(num)==float:
            break
    return num

def validate_option(message="",max_option=1):
  while True:
    option_=input(message)
    try: 
      if int(option_)<=max_option and int(option_)>0:
        break
    except:
      print("===Input a valid option===")
  return option_

def add_expense(expenses, amount, category):
    expenses.append({'amount': amount, 'category': category})
    
def print_expenses(expenses):
    for expense in expenses:
        print(f'Amount: {expense["amount"]}, Category: {expense["category"]}')
    
def total_expenses(expenses):
    return sum(map(lambda expense: expense['amount'], expenses))
    
def filter_expenses_by_category(expenses, category):
    return filter(lambda expense: expense['category'] == category, expenses)
    

def main():
    expenses = []
    while True:        
        choice=validate_option('\nExpense Tracker\n1. Add an expense\n2. List all expenses\n3. Show total expenses\n4. Filter expenses by category\n5. Exit\n: ',5)

        if choice == '1':
            amount=validate_input_num('Enter amount: ')
            category = input('Enter category: ')
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

if __name__=='__main__':
    main()