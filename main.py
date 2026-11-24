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
    print("2. Generate Report (Text)")
    print("3. Add or Remove Service Log")
    print("4. Run Simulation")
    print("5. View Current Product Performance (Graph)")
    print("6. Exit")
    print("7. Clear Output")
    print(f'{"=" * 29}\n')

    choice = input("Enter your choice: ")
    if choice == "1":
        so.view_service_log()
    elif choice == "2":
        so.generate_report()
    elif choice == "3":
        so.add_or_remove_log()
    elif choice == "4":
        print(f"\nSimulation options:")
        print("=" * 29)
        choice2 = input(f"1. Run Simulation\n2. Run Product Simulation\n3. Fetch Simulation Numbers\n4. View Previous Simulation\n5. Return to Main Menu\n{f'{"=" * 29}\n'}\nEnter your choice: ")
        if choice2 == "1":
            ss.run_simulation()
            continue
        elif choice2 == "2":
            ss.future_simulation()
            continue
        elif choice2 == "3":
            ss.fetch_simulation_numbers()
            continue        
        elif choice2 == "4":
            ss.fetch_simulation(input("Enter the simulation number to view: "))
            continue
        else:
            continue
    elif choice == "5":
        so.generate_graph()
    elif choice == "6":
        break
    elif choice == "7":
        os.system('cls')
    else:
        print("Invalid choice. Please try again.")
