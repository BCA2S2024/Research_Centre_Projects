Source Code: -
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

data = {
    'Time': pd.date_range(start='08:00', periods=12, freq='H'),  
    'Location': ['Entrance', 'Exit', 'Parking', 'Main Road'] * 3, 
    'Vehicle_Count': np.random.randint(20, 200, 12),  
    'Pedestrian_Count': np.random.randint(5, 50, 12)  
}

traffic_df = pd.DataFrame(data)

traffic_df.replace([np.inf, -np.inf], np.nan, inplace=True)

average_traffic = traffic_df.groupby('Location').mean()

print("Average Traffic Data:")
print(average_traffic)

peak_hours = traffic_df.loc[traffic_df['Vehicle_Count'] == traffic_df['Vehicle_Count'].max()]
print("\nPeak Traffic Hours:")
print(peak_hours)

plt.figure(figsize=(10, 6))
sns.lineplot(data=traffic_df, x='Time', y='Vehicle_Count', hue='Location', marker='o')
plt.title('Traffic Flow Throughout the Day')
plt.xlabel('Time')
plt.ylabel('Vehicle Count')
plt.grid(True)
plt.show()

plt.figure(figsize=(10, 6))
sns.barplot(data=traffic_df, x='Location', y='Pedestrian_Count', errorbar=None)
plt.title('Average Pedestrian Count by Location')
plt.xlabel('Location')
plt.ylabel('Pedestrian Count')
plt.grid(True)
plt.show()

def suggest_optimization(vehicle_count):
    if vehicle_count > 150:
        return "Implement dedicated entry/exit lanes."
    else:
        return "Current setup is sufficient."

traffic_df['Optimization_Suggestion'] = traffic_df['Vehicle_Count'].apply(suggest_optimization)

print("\nOptimization Suggestions Based on Traffic Data:")
print(traffic_df[['Time', 'Location', 'Vehicle_Count', 'Optimization_Suggestion']])



