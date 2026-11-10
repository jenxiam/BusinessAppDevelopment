'''
This file will be responsible for simulations, allowing for configuration of simulations OR to test a new product given its name, how many days tested, and price point.
This file will also be responsible for graphing and graph configuration.
'''

import random
import csv
import matplotlib.pyplot as plt  # type: ignore[import-not-found]

def configure_simulation():
    product_name = input("Enter the product name: ")
    days_tested = int(input("Enter the number of days tested: "))
    price_point = float(input("Enter the price point: "))
    return product_name, days_tested, price_point

def run_simulation():
    product_name, days_tested, price_point = configure_simulation()
    daily_profits = []
    for day in range(days_tested):
        daily_sales = random.randint(0, 100)
        daily_profit = daily_sales * price_point
        daily_profits.append(daily_profit)
    profit = sum(daily_profits)
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

    plt.bar([product_name], [profit])
    plt.xlabel("Product Name")
    plt.ylabel("Profit")
    plt.title("Simulation Profit Graph")
    plt.show()
    return simulation_number


def fetch_simulation(simulation_number):
    with open("SimulationHistory.csv", "r") as f:
        rows = [
            row
            for row in csv.DictReader(f)
            if row["SimulationNumber"] == str(simulation_number)
        ]
    if not rows:
        return None
    rows[0]["Profit"] = str(sum(float(row["Profit"]) for row in rows))
    return rows[0]


def graph_simulation(simulation_number):
    simulation = fetch_simulation(simulation_number)
    if simulation is None:
        print(f"Simulation {simulation_number} was not found.")
        return

    profit = float(simulation["Profit"])
    plt.bar([simulation["ProductName"]], [profit])
    plt.xlabel("Product Name")
    plt.ylabel("Profit")
    plt.title(f"Simulation {simulation_number} Profit Graph")
    plt.show()


if __name__ == "__main__":
    pass
