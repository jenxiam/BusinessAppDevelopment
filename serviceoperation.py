'''
Service operation will be responsible for managing service logs, such as editing and removing or generating a text report of total revenue, total operations, and revenue per service.
It will also provide functions to view the service log and generate graphs based on the service data.
'''


import csv
import matplotlib.pyplot as plt


def view_service_log():
    with open("ServiceLog.csv", "r") as f:
        reader = csv.reader(f)
        for row in reader:
            print(row)

def generate_report():
    with open("ServiceLog.csv", "r") as f:
        reader = csv.reader(f)
        rows = list(reader)
    total_revenue = sum(float(row[3]) for row in rows[1:])
    total_operations = len(rows) - 1
    revenue_per_service = {}
    for row in rows[1:]:
        service = row[2]
        cost = float(row[3])
        if service in revenue_per_service:
            revenue_per_service[service] += cost
        else:
            revenue_per_service[service] = cost

    print(f"\nReport:")
    print(f"{"=" * 29}")
    print(f"\nTotal Revenue: ${total_revenue:.2f}")
    print(f"Total Operations: {total_operations}")
    print(f"\nRevenue per Service:\n")
    for service, revenue in revenue_per_service.items():
        print(f"{service}: ${revenue:.2f}")
    print(f"\n{"=" * 29}\n")

def add_or_remove_log():
    print(f"\nLog editing options:")
    print(f"{"=" * 29}")
    choice = input(f"1. Add Service Log\n2. Remove Service Log\n3. Return to Main Menu\n{f'{"=" * 29}\n'}\nEnter your choice: ")
    
    if choice == "1":
        with open("ServiceLog.csv", "a", newline="") as f:
            writer = csv.writer(f)
            name = input("Enter name: ")
            employee = input("Enter employee: ")
            service = input("Enter service: ")
            cost = float(input("Enter cost: "))
            writer.writerow([name, employee, service, f"{cost:.2f}"])
    elif choice == "2":
        with open("ServiceLog.csv", "r") as f:
            reader = csv.reader(f)
            rows = list(reader)
        name_to_remove = input("Enter name to remove: ")
        if rows:
            header, data_rows = rows[0], rows[1:]
            filtered = [row for row in data_rows if not row or row[0] != name_to_remove]
            row_write = [header] + filtered
        else:
            row_write = []
        with open("ServiceLog.csv", "w", newline="") as f:
            writer = csv.writer(f)
            writer.writerows(row_write)
    elif choice == "3":
        return
    else:
        print("Invalid choice. Please try again.")

def generate_graph():
    with open("ServiceLog.csv", "r") as f:
        reader = csv.reader(f)
        rows = list(reader)
    services = [row[2] for row in rows[1:]]
    count = {}
    for service in services:
        if service in count:
            count[service] += 1
        else:
            count[service] = 1
    labels = list(count.keys())
    values = list(count.values())
    plt.bar(labels, values)
    plt.xlabel("Service")
    plt.ylabel("Count")
    plt.title("Service Log Graph")
    plt.show()
    plt.savefig("ServiceLogGraph.png")

if __name__ == "__main__":
    pass