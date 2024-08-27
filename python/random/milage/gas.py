"""
Created to calculate gas efficiency of a road trip. 
"""

from dataclasses import dataclass
import matplotlib.pyplot as plt


@dataclass
class GasRow:
    mile_number: float
    gallons: float
    price: float


rows: list[GasRow] = []

# Extract data
with open("gas.csv", "r") as f:
    headers = f.readline()
    data = f.readlines()

    for row in data:
        split = row.split(",")
        rows.append(
            GasRow(
                float(split[0]),
                float(split[1]),
                float(split[2]),
            )
        )
    rows.sort(key=lambda row: row.mile_number)

mile_numbers: list[float] = []
mpg_values: list[float] = []
gas_prices: list[float] = []

# Interpret Data
for i in range(1, len(rows)):
    curr = rows[i]
    prev = rows[i - 1]

    mile_delta = curr.mile_number - prev.mile_number
    miles_per_gallon = mile_delta / curr.gallons
    price_per_gallon = curr.price / curr.gallons

    mile_numbers.append(curr.mile_number)
    mpg_values.append(miles_per_gallon)
    gas_prices.append(price_per_gallon)


fig: plt.Figure = plt.figure()
ax1: plt.Axes = fig.add_subplot()
ax1.plot(mile_numbers, mpg_values, color="blue", label="Efficiency (MPG)")
ax1.set_xlabel("Mile Number")
ax1.set_ylabel("Miles per Gallon (MPG)")
ax1.set_title("Las Vegas Trip Gas Efficiency")

ax2: plt.Axes = ax1.twinx()
ax2.plot(mile_numbers, gas_prices, color="red", label="Price")
ax2.set_ylabel("Price per Gallon ($)")

# Janky twinx Legend Stuff
lines1, labels1 = ax1.get_legend_handles_labels()
lines2, labels2 = ax2.get_legend_handles_labels()
ax2.legend(lines1 + lines2, labels1 + labels2, loc=0)

plt.savefig(fname="gas-efficiency.png")

print("Max MPG:", max(mpg_values))
print("Min MPG:", min(mpg_values))
print("Max Gas Price:", max(gas_prices))
print("Min Gas Price:", min(gas_prices))

print("Current MPG:", mpg_values[-1])
