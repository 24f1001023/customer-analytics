
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# Generate synthetic data
np.random.seed(42)
data = pd.DataFrame({
    "Customer_Satisfaction": np.random.uniform(60, 95, 100),
    "Engagement_Score": np.random.uniform(40, 90, 100),
    "Purchase_Frequency": np.random.uniform(1, 10, 100),
    "Session_Duration": np.random.uniform(2, 15, 100),
    "Customer_Lifetime_Value": np.random.uniform(200, 1500, 100)
})

# Compute correlation
corr = data.corr()

# Styling
sns.set_style("whitegrid")
sns.set_context("talk")

# Create heatmap
plt.figure(figsize=(8, 8))
ax = sns.heatmap(corr, annot=True, cmap="coolwarm", square=True, linewidths=0.5, cbar=True)
plt.title("Customer Engagement Correlation Matrix", pad=20)

# Save output
plt.savefig('chart.png', dpi=64, bbox_inches='tight')
