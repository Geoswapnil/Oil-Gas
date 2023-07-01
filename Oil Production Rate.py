#!/usr/bin/env python
# coding: utf-8

# In[1]:


import matplotlib.pyplot as plt
import numpy as np
from matplotlib.widgets import Slider
get_ipython().run_line_magic('matplotlib', 'notebook')
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider

# Rest of your code...


# Rest of your code...


def calculate_production_rate(bpd):
    bph = bpd * 24  # Barrels per day to Barrels per hour
    bpy = bpd * 365  # Barrels per day to Barrels per year
    return bph, bpy

# Create a figure and axes for the plot
fig, ax = plt.subplots()
plt.subplots_adjust(bottom=0.25)  # Adjust the bottom margin to make room for the slider

# Set initial values and range for the production rate
initial_rate = 1000  # Initial production rate in barrels per day
min_rate = 0  # Minimum production rate
max_rate = 5000  # Maximum production rate

# Generate x values for the plot
x = np.linspace(0, 10, 100)

# Plot the initial data
bph, bpy = calculate_production_rate(initial_rate)
line, = ax.plot(x, np.sin(x) * bph, label='Oil Production Rate')

# Create a slider widget for the production rate
ax_rate = plt.axes([0.25, 0.1, 0.65, 0.03])
slider_rate = Slider(ax_rate, 'Production Rate (BPD)', min_rate, max_rate, valinit=initial_rate)

# Function to update the plot when the slider value changes
def update(val):
    bpd = slider_rate.val
    bph, bpy = calculate_production_rate(bpd)
    line.set_ydata(np.sin(x) * bph)
    fig.canvas.draw_idle()

# Connect the slider to the update function
slider_rate.on_changed(update)

# Add a legend to the plot
ax.legend()

# Set labels and title for the plot
ax.set_xlabel('Time')
ax.set_ylabel('Oil Production (BPH)')
ax.set_title('Oil Production Rate')

# Show the plot
plt.show()


# In[ ]:




