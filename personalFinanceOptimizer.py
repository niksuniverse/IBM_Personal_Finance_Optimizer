import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime

# Sample data for demonstration purposes (you can replace it with real CSV or user input)
data = {
    "Date": ["2024-12-01", "2024-12-02", "2024-12-03", "2024-12-04", "2024-12-05"],
    "Category": ["Food", "Transport", "Entertainment", "Utilities", "Miscellaneous"],
    "Amount": [200, 50, 120, 300, 100]
}

def load_data():
    # Converts the dictionary into a DataFrame. Replace this with `pd.read_csv("yourfile.csv")` to use a CSV file.
    df = pd.DataFrame(data)
    df['Date'] = pd.to_datetime(df['Date'])
    return df

# Visualization

def plot_expenses(df):
    plt.figure(figsize=(8, 5))
    category_sum = df.groupby('Category')['Amount'].sum()
    category_sum.plot(kind='bar', color='skyblue', alpha=0.7, edgecolor='black')
    plt.title("Expense Breakdown by Category")
    plt.ylabel("Amount Spent")
    plt.xlabel("Category")
    plt.xticks(rotation=45)
    plt.grid(axis='y', linestyle='--', alpha=0.7)
    plt.tight_layout()
    plt.show()

def savings_suggestions(df):
    total_expense = df['Amount'].sum()
    high_spending = df.groupby('Category')['Amount'].sum().idxmax()

    print("\n===== Financial Overview =====")
    print(f"Total Expense: {total_expense}")
    print(f"Highest Spending Category: {high_spending}")

    print("\n===== Suggestions =====")
    if total_expense > 500:
        print("\u2022 You're spending a lot! Consider cutting back in the highest spending category.")
    else:
        print("\u2022 Great job keeping your expenses low!")

    high_expense = df.loc[df['Category'] == high_spending, 'Amount'].sum()
    if high_expense > 0.3 * total_expense:
        print(f"\u2022 Reduce spending in {high_spending}. It accounts for a large portion of your expenses.")
    
    print("\u2022 Plan your monthly budget to allocate specific amounts for each category.")

def main():
    print("Welcome to the Personal Finance Optimizer!")
    df = load_data()
    
    print("\nHere is your expense data:\n")
    print(df)
    
    plot_expenses(df)
    savings_suggestions(df)

if __name__ == "__main__":
    main()
