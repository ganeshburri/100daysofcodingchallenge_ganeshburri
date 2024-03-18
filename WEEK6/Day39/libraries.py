import pandas as pd
import matplotlib.pyplot as plt
# Data
data = {
    "Fruit": ["Apples", "Oranges", "Bananas", "Strawberries", "Grapes"],
    "Price": [1.5, 2.0, 0.8, 3.0, 2.5],
    "Quantity": [20, 33, 45, 12, 40]
}

# Creating a DataFrame
df = pd.DataFrame(data)
# Calculating total value
df['Total Value'] = df['Price'] * df['Quantity']
print(df)
# Finding the fruit with the highest total value
max_value_fruit = df.loc[df['Total Value'].idxmax()]
print(f"The fruit with the highest total value is: {max_value_fruit['Fruit']}")


# Setting up the plot
plt.figure(figsize=(8, 4))
plt.bar(df['Fruit'], df['Quantity'], color='skyblue')

# Adding titles and labels
plt.title('Quantity of Fruits in the Market')
plt.xlabel('Fruit')
plt.ylabel('Quantity')

# Displaying the plot
plt.show()