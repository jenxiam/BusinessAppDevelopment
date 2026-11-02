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
    profit = 0
    for day in range(days_tested):
        daily_sales = random.randint(0, 100)
        daily_profit = daily_sales * price_point
        profit += daily_profit
    with open("SimulationHistory.csv", "a", newline="") as f:
        f.seek(0)
        rows = list(csv.DictReader(f))
        simulation_number = max((int(row["SimulationNumber"]) for row in rows)) + 1
        writer = csv.writer(f)
        if not rows:
            writer.writerow(["SimulationNumber", "ProductName", "DayCount", "Profit"])
        writer.writerow([simulation_number, product_name, days_tested, profit])

    plt.bar([product_name], [profit])
    plt.xlabel("Product Name")
    plt.ylabel("Profit")
    plt.title("Simulation Profit Graph")
    plt.show()
    return simulation_number


def fetch_simulation(simulation_number):
    with open("SimulationHistory.csv", "r") as f:
        for row in csv.DictReader(f):
            if row["SimulationNumber"] == str(simulation_number):
                return row
    return None


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
