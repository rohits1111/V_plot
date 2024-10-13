import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

file_path = '/root/project/v_plot/output.tsv'
v_plot_data = pd.read_csv(file_path, sep='\t', header='infer') #

#set column names manually
#v_plot_data.columns = ['frequency','position','length']

# Step 2: Extract relevant columns for the scatter plot
x_values = v_plot_data['position']       # X-axis values (position)
y_values = v_plot_data['length']    # Y-axis values (length)
color_values = v_plot_data['frequency'] # Colors of the points (frequency)

# Creating scatter plot
plt.figure(figsize=(8,6))
plt.scatter(x_values, y_values, c=color_values, cmap='twilight', s=10, marker='o') #setting the color map

# Adding labels and title
plt.xlabel('Position')
plt.ylabel('Length')
plt.title('V-plot')

# Step 5: Add color bar and grid
plt.colorbar(label='frequency') #color bar and grading varies according to frequency

# Display the plot
plt.grid(True)
plt.show()

