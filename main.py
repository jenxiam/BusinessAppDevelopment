'''
Chase Bradley
BMIS365
10/27/2026
The main program for the Business App Final project. 
The business is a computer repair shop that offers multiple services, including virus removal, repairs, cleaning, and troubleshooting. 
Employees will use the app to log transactions and services that were requested. 
This app solves organizational and historical issues businesses face, such as lost repair records or forgotten service requests.

Business question: Which service (virus removal, repair, cleaning, or troubleshooting) generates the most revenue?
'''

import os
import serviceoperation as so
import servicesimulation as ss

while True:
    print("Computer repair shop terminal")
    print("=" * 29)
    print("1. View Service Log")
    print("2. Add or Remove Service Log")
    print("3. Run Simulation")
    print("4. Generate Graph")
    print("5. Exit")
    print("6. Clear Output")
    print(f'{"=" * 29}\n')

    choice = input("Enter your choice: ")
    if choice == "1":
        so.view_service_log()
    elif choice == "2":
        so.add_or_remove_log()
    elif choice == "3":
        ss.run_simulation()
    elif choice == "4":
        so.generate_graph()
    elif choice == "5":
        break
    elif choice == "6":
        clear = lambda: os.system('cls')
        clear()
    else:
        print("Invalid choice. Please try again.")

    