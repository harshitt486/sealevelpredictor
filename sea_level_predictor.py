import pandas as pd  
import matplotlib.pyplot as plt  
from scipy.stats import linregress  
import numpy as np  

def draw_plot():  
    # Read data  
    df = pd.read_csv('epa-sea-level.csv')  
    
    # Create scatter plot  
    plt.figure(figsize=(10, 6))  
    plt.scatter(df['Year'], df['CSIRO Adjusted Sea Level'], label='Data')  
    
    # Line of best fit for entire dataset  
    slope, intercept, _, _, _ = linregress(df['Year'], df['CSIRO Adjusted Sea Level'])  
    years = np.arange(1880, 2051)  
    plt.plot(years, slope * years + intercept, 'r', label='Best fit line (1880-2050)')  
    
    # Line of best fit for data from 2000 onwards  
    recent_data = df[df['Year'] >= 2000]  
    slope_recent, intercept_recent, _, _, _ = linregress(recent_data['Year'], recent_data['CSIRO Adjusted Sea Level'])  
    recent_years = np.arange(2000, 2051)  
    plt.plot(recent_years, slope_recent * recent_years + intercept_recent, 'green', label='Best fit line (2000-2050)')  
    
    # Add labels and title  
    plt.xlabel('Year')  
    plt.ylabel('Sea Level (inches)')  
    plt.title('Rise in Sea Level')  
    
    # Add legend  
    plt.legend()  
    
    # Save plot  
    plt.savefig('sea_level_plot.png')  
    return plt.gca()  

# For testing  
if __name__ == "__main__":  
    draw_plot()  
