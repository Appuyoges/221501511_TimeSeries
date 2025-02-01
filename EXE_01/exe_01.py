import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Step 1: Load dataset
def load_data(file_path):
    df = pd.read_csv(file_path, parse_dates=['Date'])
    df.set_index('Date', inplace=True)
    return df

# Step 2: Clean dataset
def clean_data(df):
    df.replace(',', '', regex=True, inplace=True)  # Remove commas from numeric values
    df = df.astype(float)  # Convert all values to float
    df = df.dropna()  # Drop missing values
    df = df[df > 0]  # Remove negative or zero values if present
    return df

# Step 3: Handle missing values
def handle_missing_data(df):
    df.fillna(method='ffill', inplace=True)  # Forward fill
    df.fillna(method='bfill', inplace=True)  # Backward fill
    return df

# Step 4: Preprocessing techniques
def preprocess_data(df):
    df['Return'] = df['Close'].pct_change()  # Calculate daily returns
    df['Volatility'] = df['Return'].rolling(window=5).std()  # Rolling volatility
    return df

# Step 5: Plot stock closing price over time
def visualize_data(df):
    plt.figure(figsize=(10, 6))
    plt.plot(df['Close'], label='Stock Close Price', color='blue')
    plt.title('Apple stock close prices')
    plt.xlabel('Date')
    plt.ylabel('Close Price (USD)')
    plt.legend()
    plt.show()

# Example usage
file_path = "D:/221501511/Download Data - STOCK_US_XNAS_AAPL (1).csv"
df = load_data(file_path)
df = clean_data(df)
df = handle_missing_data(df)
df = preprocess_data(df)
visualize_data(df)
print(df.head())
