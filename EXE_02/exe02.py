import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import statsmodels.api as sm

# Step 1: Load dataset
def load_data(file_path):
    df = pd.read_csv(file_path, parse_dates=['Date'])
    df.set_index('Date', inplace=True)
    return df

# Step 2: Scatter Plot - Visualizing stock closing price over time
def scatter_plot(df):
    plt.figure(figsize=(10, 6))
    plt.scatter(df.index, df['Close'], label='Stock Close Price', color='blue', alpha=0.5)
    plt.title('Stock Close Price Over Time (Scatter Plot)')
    plt.xlabel('Date')
    plt.ylabel('Close Price (USD)')
    plt.legend()
    plt.show()

# Step 3: Histogram - Distribution of Closing Prices
def histogram(df):
    plt.figure(figsize=(10, 6))
    sns.histplot(df['Close'], bins=30, kde=True, color='blue')
    plt.title('Distribution of Closing Prices')
    plt.xlabel('Close Price (USD)')
    plt.ylabel('Frequency')
    plt.show()

# Step 4: Box Plot - Outlier Detection in Closing Prices
def box_plot(df):
    plt.figure(figsize=(8, 6))
    sns.boxplot(y=df['Close'], color='blue')
    plt.title('Box Plot of Closing Prices')
    plt.ylabel('Close Price (USD)')
    plt.show()

# Step 5: Moving Average Plot
def moving_average_plot(df, window=30):
    df['Moving_Avg'] = df['Close'].rolling(window=window).mean()
    
    plt.figure(figsize=(10, 6))
    plt.plot(df['Close'], label='Original', color='blue', alpha=0.5)
    plt.plot(df['Moving_Avg'], label=f'{window}-Day Moving Average', color='red')
    plt.title(f'Moving Average (Window={window} Days)')
    plt.xlabel('Date')
    plt.ylabel('Close Price (USD)')
    plt.legend()
    plt.show()

# Step 6: Autocorrelation Plot
def autocorrelation_plot(df):
    sm.graphics.tsa.plot_acf(df['Close'].dropna(), lags=30)
    plt.title('Autocorrelation of Closing Prices')
    plt.show()

# Example usage
file_path = "D:/221501511/Download Data - STOCK_US_XNAS_AAPL (1).csv"
df = load_data(file_path)

# Call visualization functions
scatter_plot(df)
histogram(df)
box_plot(df)
moving_average_plot(df)
autocorrelation_plot(df)
