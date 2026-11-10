'''
Service operation will be responsible for managing service logs, such as editing and removing.
It will also provide functions to view the service log and generate graphs based on the service data.
'''

import csv

try:
    import matplotlib.pyplot as plt  # type: ignore[import-not-found]
except ImportError:
    plt = None

def view_service_log():
    with open("ServiceLog.csv", "r") as f:
        reader = csv.reader(f)
        for row in reader:
            print(row)

def add_or_remove_log():
    print(f"\nLog editing options:")
    print(f"{"=" * 29}")
    choice = input(f"1. Add Service Log\n2. Remove Service Log\n3. Exit\n{f'{"=" * 29}\n'}\nEnter your choice: ")
    
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
            filtered_rows = [row for row in data_rows if not row or row[0] != name_to_remove]
            rows_to_write = [header] + filtered_rows
        else:
            rows_to_write = []
        with open("ServiceLog.csv", "w", newline="") as f:
            writer = csv.writer(f)
            writer.writerows(rows_to_write)
    elif choice == "3":
        return
    else:
        print("Invalid choice. Please try again.")

def generate_graph():
    with open("ServiceLog.csv", "r") as f:
        reader = csv.reader(f)
        rows = list(reader)
    services = [row[2] for row in rows]
    service_counts = {}
    for service in services:
        if service in service_counts:
            service_counts[service] += 1
        else:
            service_counts[service] = 1
    labels = list(service_counts.keys())
    values = list(service_counts.values())
    plt.bar(labels, values)
    plt.xlabel("Service")
    plt.ylabel("Count")
    plt.title("Service Log Graph")
    plt.show()

if __name__ == "__main__":
    pass