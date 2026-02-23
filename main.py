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
plt.show()
plt.savefig(f'charts/obesity_graph.png')
print("Saving obesity_graph.png to charts folder")
print("All done")




# (10/10 points) Store this information in Pandas dataframe. These should be 2D data as a dataframe, meaning the data is labeled tabular data.
# (10/10 points) Using matplotlib, graph this data in a way that will visually represent the data. Really try to build some fancy charts here as it will greatly help you in future homework assignments and in the final project.
# (10/10 points) Save these graphs in a folder called charts as PNG files. Do not upload these to your project folder, the project should save these when it executes. You may want to add this folder to your .gitignore file.
# (10/10 points) I will be checking out the main branch of your project. Please be sure to include a requirements.txt file which contains all the packages that need installed. You can create this fille with the output of pip freeze at the terminal prompt.
# (20/20 points) There should be a README.md file in your project that explains what your project is, how to install the pip requirements, and how to execute the program. Please use the GitHub flavor of Markdown. Be thorough on the explanations.