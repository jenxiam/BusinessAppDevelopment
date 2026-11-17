'''
This file will be responsible for simulations, allowing for configuration of simulations OR to test a new product given its name, how many days tested, and price point.
This file will also be responsible for graphing and graph configuration.
'''

import random
import csv
import matplotlib.pyplot as plt  # type: ignore[import-not-found]

def configure_simulation():
    product_name = input("Enter the product name: ")
    try:
        days_tested = int(input("Enter the number of days tested: "))
    except ValueError:
        print("Invalid input. Please enter a valid number.")
        return configure_simulation()
    try:
        price_point = float(input("Enter the price point: "))
    except ValueError:
        print("Invalid input. Please enter a valid number.")
        return configure_simulation()
    return product_name, days_tested, price_point

def run_simulation():
    product_name, days_tested, price_point = configure_simulation()
    daily_profits = []
    for day in range(days_tested):
        daily_sales = random.randint(0, 100)
        daily_profit = daily_sales * price_point
        daily_profits.append(daily_profit)
    with open("SimulationHistory.csv", "a+", newline="") as f:
        f.seek(0)
        rows = list(csv.DictReader(f))
        simulation_number = max((int(row["SimulationNumber"]) for row in rows), default=0) + 1
        f.seek(0, 2)
        writer = csv.writer(f)
        if f.tell() == 0:
            writer.writerow(["SimulationNumber", "ProductName", "DayCount", "Profit"])
        for day_count, daily_profit in enumerate(daily_profits, start=1):
            writer.writerow([simulation_number, product_name, day_count, daily_profit])

    day_counts = list(range(1, days_tested + 1))
    plt.plot(day_counts, daily_profits)
    plt.xlabel("Day")
    plt.ylabel("Daily Profit")
    plt.title(f"Simulation {simulation_number} Profit by Day: {product_name}")
    plt.show()
    return simulation_number

def fetch_simulation(simulation_number):
    with open("SimulationHistory.csv", "r") as f:
        rows = [row for row in csv.DictReader(f) if row["SimulationNumber"] == str(simulation_number)]
    if not rows:
        return None

    day_counts = [int(row["DayCount"]) for row in rows]
    daily_profits = [float(row["Profit"]) for row in rows]
    plt.plot(day_counts, daily_profits)
    plt.xlabel("Day")
    plt.ylabel("Daily Profit")
    plt.title(f"Simulation {simulation_number} Profit by Day: {rows[0]['ProductName']}")
    plt.show()
    plt.savefig(f"Simulation_{simulation_number}_ProfitGraph.png")

def fetch_simulation_numbers():
    with open("SimulationHistory.csv", "r") as f:
        rows = list(csv.DictReader(f))
    simulation_numbers = sorted(set(int(row["SimulationNumber"]) for row in rows))
    print(f"\nAvailable Simulation Numbers:")
    print(f"{"=" * 29}")
    for number in simulation_numbers:
        print(f"\n{number}")
    print(f"\n{"=" * 29}\n")

if __name__ == "__main__":
    pass
