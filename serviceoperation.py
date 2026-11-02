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
    choice = input("Do you want to add or remove a log? (add/remove): ")
    if choice == "add":
        with open("ServiceLog.csv", "a", newline="") as f:
            writer = csv.writer(f)
            name = input("Enter name: ")
            service = input("Enter service: ")
            cost = input("Enter cost: ")
            writer.writerow([name, service, cost])
    elif choice == "remove":
        with open("ServiceLog.csv", "r", newline="") as f:
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

def generate_graph():
    with open("ServiceLog.csv", "r") as f:
        reader = csv.reader(f)
        rows = list(reader)
    services = [row[1] for row in rows]
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
    action = input("1: View Service Log\n2: Add or Remove Service Log\n4: Generate Graph\nEnter your choice: ")
    if action == "1":
        view_service_log()
    elif action == "2":
        add_or_remove_log()
    elif action == "4":
        generate_graph()