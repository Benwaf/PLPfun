# Iris Dataset Analysis Script
# Script performs data loading, basic analysis, and visualizations using pandas, seaborn, and matplotlib

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.datasets import load_iris

# Load the Iris dataset
iris_raw = load_iris()

# Convert to DataFrame
iris_df = pd.DataFrame(data=iris_raw.data, columns=iris_raw.feature_names)
iris_df['species'] = pd.Categorical.from_codes(iris_raw.target, iris_raw.target_names)

# Display first few rows
print("First 5 rows of the dataset:")
print(iris_df.head())

# Dataset structure
print("\nDataset Info:")
iris_df.info()

# Check for missing values
print("\nMissing Values:")
print(iris_df.isnull().sum())

# Basic statistics
print("\nBasic Statistics:")
print(iris_df.describe())

# Mean values by species
print("\nMean Values Grouped by Species:")
print(iris_df.groupby('species').mean(numeric_only=True))

# Set style for plots
sns.set(style="whitegrid")

# Task 1. Line chart - petal length
plt.figure(figsize=(10, 5))
plt.plot(iris_df.index, iris_df['petal length (cm)'], label='Petal Length (cm)', color='teal')
plt.title("Line Chart: Petal Length across Samples")
plt.xlabel("Sample Index")
plt.ylabel("Petal Length (cm)")
plt.legend()
plt.tight_layout()
plt.show()

# Task 2. Bar chart - average petal length by species
plt.figure(figsize=(7, 5))
sns.barplot(data=iris_df, x='species', y='petal length (cm)', palette='viridis')
plt.title("Bar Chart: Average Petal Length by Species")
plt.xlabel("Species")
plt.ylabel("Average Petal Length (cm)")
plt.tight_layout()
plt.show()

# Task3. Histogram - petal length distribution
plt.figure(figsize=(8, 5))
sns.histplot(iris_df['petal length (cm)'], bins=20, kde=True, color='coral')
plt.title("Histogram: Petal Length Distribution")
plt.xlabel("Petal Length (cm)")
plt.ylabel("Frequency")
plt.tight_layout()
plt.show()

# Task 4. Scatter plot - sepal vs. petal length
plt.figure(figsize=(8, 6))
sns.scatterplot(data=iris_df, x='sepal length (cm)', y='petal length (cm)', hue='species', palette='Set1')
plt.title("Scatter Plot: Sepal Length vs Petal Length")
plt.xlabel("Sepal Length (cm)")
plt.ylabel("Petal Length (cm)")
plt.legend(title='Species')
plt.tight_layout()
plt.show()
