# Business App Development Final Project

```text
Author: Jenxiam
Date: 11/9/2026
Class: BMIS365
```
## Business Problem
The main purpose of this project is to be an app that a business can use to keep track of service operations such as:

- Recording work performed for customers.
- Graphing data in the form of product launches and potential income.
- Graphing already-existing products to compare performance.

## Business Question

Which service (virus removal, repair, cleaning, or troubleshooting) generates the most revenue?

## Functions & Functions

- view_service_log()
```
This function reads ServiceLog.csv and prints all lines.
```
- add_or_remove_log()
```
This function adds or remove logs at the user's request.
```
- run_simulation()
```
This function runs a custom simulation where the user can pick the product name, how many days it will run for, and the product price point. It will then store that data found in SimulationHistory.csv.
```

- generate_graph()
```
This function generates a graph based off the current product data found in ServiceLog.csv.
```

## How to Run
1. Open the project folder in VS Code
2. Run `main.py`
3. Choose an option from the menu

## Menu Options
1. View Service Log
2. Add or Remove Service Log
3. Run Simulation
4. Generate Graph
5. Exit
6. Clear Output

## Files
- `main.py` - Runs the menu.
- `ServiceLog.csv` - Product log data.
- `serviceoperation.py` - Handles all operations related to data.
- `servicesimulation.py` - Handles simulation inputs and produces simulations.
- `SimulationHistory.csv` - Simulation history log data.

### SUBJECT TO CODE CHANGES AND WILL BE UPDATED
