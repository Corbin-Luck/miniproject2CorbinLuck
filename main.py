### INF601 - Advanced Programming in Python
### Corbin Luck
### Mini Project 2

## Imports
import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path

# Creates the charts folder if one does not exist
charts = Path('charts')
if not charts.exists():
    Path(r'charts').mkdir()

## sets df as the data in the healthcare_dataset.csv
df = pd.read_csv("./data/healthcare_dataset.csv", header=None)

## Selects just the condition column from the datasheet
condition = df[4]

## Finds the count of patients with and without Obesity
obesity_count = (condition == "Obesity").value_counts()

## Plots a bar graph to compare the obese vs not obese patients
obesity_count.plot(
    kind="bar",
    color=["#90EE90", "#FA8072"],
    edgecolor="black",
)

plt.title("Obesity Distribution")
plt.ylabel("Number of Patients")
plt.xlabel("Condition")
plt.xticks([0,1], ["Healthy", "Obese"], rotation=0, fontsize="7")
plt.savefig('charts/obesity_graph.png')
print("Saving obesity_graph.png to charts folder")
print("All done")
