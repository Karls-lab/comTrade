import pandas as pd
import numpy as np 
import matplotlib.pyplot as plt
import locale
import logging
import os

# Read in the data
data_path = os.path.join(os.path.dirname(__file__), 'worldExports2022.csv') 
df = pd.read_csv(data_path, encoding='latin-1')

# Print data frame info
logging.info(df.info())

"""Creating a pie chart displaying countries and their exports
   x = df['ReporterISO'], y = df['PrimaryValue']"""

# Calculate total exports and format it into human readable
total_exports = sum(df['PrimaryValue'])
locale.setlocale(locale.LC_ALL, 'en_US.UTF-8')
formated_total_exports = locale.currency(total_exports, grouping=True)
print(f"Total exports: {formated_total_exports}")

# Only account for largest 10 exoprters
df.nlargest(10, 'PrimaryValue', keep='first')
largestExporters = df.nlargest(10, 'PrimaryValue', keep='first')

# Create a list of countries and their exports
countries = largestExporters['ReporterISO']
exports = largestExporters['PrimaryValue']
exports_10_largest = exports.sum() 

# Configure the canvas and chart labels
plt .figure(figsize=(7, 7))
plt.title("Top 10 Exporters")

# Create a pie chart
pie_chart, lables, dictionary= plt.pie(
   exports,
   labels=countries, 
   autopct='%1.1f%%',
   shadow=True,
   wedgeprops={"edgecolor": "black", "linewidth": 1},
   radius=1.2,
    )

# Create custom colors for the pie chart labels 
country_colors = {"CHN": "#DD0004", "USA": "#0055A4", "DEU": "gray", "NLD": "#FFA500", "JPN": "white", 
                  "ITA": "green", "KOR": "purple", "FRA": "#2552CA", "HKG": "#DE2910", "CAN": "pink"}
for wedge in pie_chart :
   print(wedge.get_label())
   wedge.set_facecolor(country_colors[wedge.get_label()])

# Display the pie chart
plt.show()