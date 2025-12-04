import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# 1. Setup and Style
# Setting a professional theme using seaborn
sns.set_style("whitegrid")
sns.set_context("talk") # increases font scale for presentations

# Ensure reproducibility
np.random.seed(42)

# 2. Generate Synthetic Data
# Simulating 200 customer records for 'Marketing Campaign Effectiveness'
n_points = 200

# Marketing Channels
channels = ['Social Media', 'Email', 'Paid Search', 'Referral']
channel_data = np.random.choice(channels, n_points, p=[0.3, 0.25, 0.3, 0.15])

# Customer Acquisition Cost (CAC) - generating realistic variances per channel
# Logic: Email is cheap, Search is expensive, Referral is varied
base_costs = {
    'Social Media': 40, 
    'Email': 15, 
    'Paid Search': 85, 
    'Referral': 25
}
cac_values = []
for channel in channel_data:
    noise = np.random.normal(0, 10)
    cost = max(5, base_costs[channel] + noise) # Ensure cost is at least 5
    cac_values.append(cost)

# Customer Lifetime Value (CLV)
# Logic: CLV is generally a multiple of CAC, but varies by channel quality
clv_values = []
for i, cost in enumerate(cac_values):
    channel = channel_data[i]
    if channel == 'Referral':
        multiplier = np.random.uniform(4.0, 7.0) # High value customers
    elif channel == 'Email':
        multiplier = np.random.uniform(3.0, 5.0)
    else:
        multiplier = np.random.uniform(1.5, 4.5)
    
    clv_values.append(cost * multiplier)

# Create DataFrame
df = pd.DataFrame({
    'Acquisition Cost (CAC)': cac_values,
    'Lifetime Value (CLV)': clv_values,
    'Marketing Channel': channel_data
})

# 3. Create Scatterplot
# Setting figure size to 8x8 inches. At 64 DPI, this targets 512x512 pixels.
plt.figure(figsize=(8, 8))

# Generating the scatterplot
scatter = sns.scatterplot(
    data=df,
    x='Acquisition Cost (CAC)',
    y='Lifetime Value (CLV)',
    hue='Marketing Channel',
    style='Marketing Channel', # Adds shape distinction for accessibility
    s=100, # Marker size
    palette='viridis', # Professional, distinct color palette
    alpha=0.8 # Slight transparency for overlapping points
)

# 4. Professional Styling
plt.title('Customer Lifetime Value vs. Acquisition Cost\nby Marketing Channel', 
          pad=20, fontweight='bold', fontsize=16)
plt.xlabel('Acquisition Cost ($)', fontsize=12)
plt.ylabel('Lifetime Value ($)', fontsize=12)

# Adjust legend position and styling
plt.legend(title='Channel', bbox_to_anchor=(1.05, 1), loc='upper left', borderaxespad=0.)

# 5. Save Chart
# Using dpi=64 to achieve the required resolution based on figure size
plt.savefig('chart.png', dpi=64, bbox_inches='tight')

# Display plot (optional, for verification if running in notebook)
# plt.show()
