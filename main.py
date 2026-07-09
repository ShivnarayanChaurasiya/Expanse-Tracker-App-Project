# Expanse Tracker Project 
import csv

expensesList = []
FILE_NAME = "expenses.csv"
try:
    with open(FILE_NAME, mode="r", newline="") as file:
        reader = csv.DictReader(file)

        for row in reader:
            row["amount"] = float(row["amount"])
            expensesList.append(row)

except FileNotFoundError:
    pass     #list  of expenses in form of dictionaries
def saveExpenses():
    with open(FILE_NAME, mode="w", newline="") as file:
        fieldnames = ["date", "category", "description", "amount"]

        writer = csv.DictWriter(file, fieldnames=fieldnames)

        writer.writeheader()
        writer.writerows(expensesList)


print("Welcome to the Expense Tracker  : kharch kam karo , paise bachao ")

while True:
    print("====MENU===")
    print("1. Add Expenses")
    print("2. View All Expenses")
    print("3. View Total kharch ")
    print("4. Delete Expense")
    print("5. Edit Expense")
    print("6. Exit")

    choice = input("Please Enter your  Choice (1-6):")

  #1 ADD Expenses 
    if(choice =="1"):
        date = input("Enter the date of expenses (YYYY-MM-DD): ")
        category =input("Enter the category of expenses (Food , Transport , Shopping, etc) :")
        description = input("Enter the description of expanses: ")

        try:
            amount = float(input("Enter the amount: "))
        except ValueError:
            print("❌ Invalid amount! Please enter a number.")
            continue
       # amount = float(input("Enter the amount : "))

        expense = {
            "date": date,
            "category": category,
            "description": description,
            "amount": amount 
        }
        expensesList.append(expense)
        saveExpenses()
        print(" \n Done Bro. Expense added successfully!")

#2.View All Expanses 

    elif(choice =="2"):
        if( len(expensesList)==0):    
            print("No expenses to display.")
        else:
            print("\n--- All Expenses ---")
        
            for i, expense in enumerate(expensesList, start=1):
               # print(f"{i}. Date: {expense['date']}, Category: {expense['category']}, Description: {expense['description']}, Amount: {expense['amount']}")
                 print(f"{i}. Date: {expense['date']}, Category: {expense['category']}, Description: {expense['description']}, Amount: ₹{expense['amount']}")
 # View Total Expense 

    elif(choice =="3"):
        total = 0
        for eachkharch in expensesList:
            total += eachkharch["amount"] 
        print(f"\nTotal Expense = ₹{total}")

 # Delete Expense 
    elif(choice == "4"):
       if len(expensesList) == 0:
           print("No Expense to Delete.")
       else:
           print("\n ---All Expenses--")
           for i , expense in enumerate(expensesList,start=1):
                print(f"{i}. {expense['category']} - ₹{expense['amount']} ({expense['description']})")
    
           try:
                deleteIndex = int(input("\nEnter the expense number to delete: "))

                if 1 <= deleteIndex <= len(expensesList):
                    deletedExpense = expensesList.pop(deleteIndex - 1)
                    saveExpenses()
                    print(f"✅ Expense '{deletedExpense['description']}' deleted successfully!")
                else:
                    print("❌ Invalid expense number.")

           except ValueError:
                print("❌ Please enter a valid number.")


#Edit Expense 

    elif (choice == "5"):
       if len(expensesList) == 0:
           print("NO Expenses to edit.")

       else:
           print("\n---All Expenses---")

           for i , expense in enumerate(expensesList , start=1):
               print(f"{i}. {expense['category']} - ₹{expense['amount']} ({expense['description']})")
       
           try:
        
              editIndex = int(input("\nEnter the expense number to edit: "))

              if 1 <= editIndex <= len(expensesList):

                expense = expensesList[editIndex - 1]

                print("\nEnter new details")


                expense["date"] = input("Enter new date (YYYY-MM-DD): ")
                expense["category"] = input("Enter new category: ")
                expense["description"] = input("Enter new description: ")
                #expense["amount"] = float(input("Enter new amount: "))
                try:
                  expense["amount"] = float(input("Enter new amount: "))
                except ValueError:
                   print("❌ Invalid amount. Edit cancelled.")
                   continue
                saveExpenses()
                print("✅ Expense updated successfully!")

              else:
                print("❌ Invalid expense number.")

           except ValueError:
                print("❌ Please enter a valid number.")





# Exit 

    # elif (choice == "6"):
    #     print("Thank you for using the Expense Tracker. Goodbye!")
    #     with open(FILE_NAME, mode="w", newline="") as file:
    #      fieldnames = ["date", "category", "description", "amount"]

    #      writer = csv.DictWriter(file, fieldnames=fieldnames)

    #      writer.writeheader()

    #      writer.writerows(expensesList)
    #     break
    elif choice == "6":
        saveExpenses()
        print("Thank you for using the Expense Tracker. Goodbye!")
        break   

    else:
        print("Invalid choice. Try again")
