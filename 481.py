import pandas as pd
import matplotlib.pyplot as plt

# Create a DataFrame
df = pd.DataFrame({
    'store_name': ['Store 1', 'Store 2', 'Store 3', 'Store 4', 'Store 5'],
    'date': ['2023-06-06', '2023-06-07', '2023-06-08', '2023-06-09', '2023-06-10'],
    'weekly_sales': [1000, 1500, 2000, 2500, 3000],
    'holiday_indicator': [0, 1, 0, 1, 0],
    'temperature_in_degrees_fahrenheit': [75, 80, 90, 95, 100],
    'fuel_price_per_gallon': [3.5, 3.0, 2.5, 2.0, 1.5],
    'consumer_price_index': [120, 110, 100, 90, 80],
    'unemployment_rate': [3.5, 4.0, 4.5, 5.0, 5.5]
})

# Calculate the correlation between weekly sales and temperature
correlation = df['weekly_sales'].corr(df['temperature_in_degrees_fahrenheit'])

# Create a scatter plot
plt.figure(figsize=(8, 6))
plt.scatter(df['temperature_in_degrees_fahrenheit'], df['weekly_sales'])
plt.xlabel('Temperature in Degrees Fahrenheit')
plt.ylabel('Weekly Sales')
plt.title('Correlation between Weekly Sales and Temperature')
plt.text(70, 3000, f'Correlation: {correlation:.2f}')
plt.grid(True)
plt.show()