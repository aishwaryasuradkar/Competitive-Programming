# list of expenses for each student
expenses = [50.00, 60.00, 45.00, 75.00, 55.00]

# calculate the total expenses
total_expenses = sum(expenses)

# calculate the average expense per student
num_students = len(expenses)
average_expense = total_expenses / num_students

# calculate the amount each student owes or is owed
amounts = [expense - average_expense for expense in expenses]

# group the amounts owed and owed to each student
owed_to = [i for i in range(num_students) if amounts[i] > 0]
owed_by = [i for i in range(num_students) if amounts[i] < 0]

# sort the lists of amounts owed and owed to
owed_to.sort(reverse=True)
owed_by.sort()

# pair students who owe money with students who are owed money
for i in range(min(len(owed_to), len(owed_by))):
    to_student = owed_to[i]
    by_student = owed_by[i]
    amount = min(abs(amounts[to_student]), abs(amounts[by_student]))
    amounts[to_student] -= amount
   
