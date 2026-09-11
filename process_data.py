import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from pptx import Presentation
from pptx.util import Inches, Pt
from pptx.dml.color import RGBColor
from pptx.enum.text import PP_ALIGN
import openpyxl
from openpyxl.styles import Font, PatternFill, Alignment, Border, Side
from openpyxl.utils import get_column_letter
import nbformat as nbf

# Set styles
plt.style.use('seaborn-v0_8-whitegrid')
plt.rcParams['font.family'] = 'DejaVu Sans'
plt.rcParams['font.size'] = 11

os.makedirs('d:/kanishka/visualizations', exist_ok=True)

# 1. Load Raw Data
print("Loading raw data...")
raw_path = 'd:/kanishka/Global_Superstore_Raw.csv'
df_raw = pd.read_csv(raw_path, encoding='latin1')
print(f"Raw data loaded: {df_raw.shape[0]} rows, {df_raw.shape[1]} columns")

# 2. Process Data
print("Processing data...")
df = df_raw.copy()

# Fix dates
df['Order Date'] = pd.to_datetime(df['Order Date'], format='%d-%m-%Y')
df['Ship Date'] = pd.to_datetime(df['Ship Date'], format='%d-%m-%Y')

# Derived Time features
df['Order_Year'] = df['Order Date'].dt.year
df['Order_Month'] = df['Order Date'].dt.month
df['Order_Year_Month'] = df['Order Date'].dt.to_period('M').astype(str)
df['Order_Day_of_Week'] = df['Order Date'].dt.day_name()
df['Shipping_Days'] = (df['Ship Date'] - df['Order Date']).dt.days

# Handle Missing Postal Codes
df['Postal Code'] = df['Postal Code'].fillna('Not Recorded')

# Derived Financial & Operational Metrics
df['Unit_Price'] = np.round(df['Sales'] / df['Quantity'], 2)
df['Unit_Cost'] = np.round((df['Sales'] - df['Profit']) / df['Quantity'], 2)
df['Profit_Margin_%'] = np.round((df['Profit'] / df['Sales']) * 100, 2)
df['Is_Profitable'] = (df['Profit'] > 0).astype(int)

# Discount Bins
bins = [-0.001, 0, 0.20, 0.50, 1.0]
labels = ['0% (No Discount)', '1-20% (Low)', '21-50% (Moderate)', '>50% (Heavy)']
df['Discount_Band'] = pd.cut(df['Discount'], bins=bins, labels=labels)

# Save Processed CSV
processed_csv_path = 'd:/kanishka/Processed_Data.csv'
df.to_csv(processed_csv_path, index=False)
print(f"Saved processed data to {processed_csv_path}")

# 3. Generate Analytical Visualizations
print("Generating charts...")

# Chart 1: Profit Margin by Discount Band
plt.figure(figsize=(9, 5))
disc_summary = df.groupby('Discount_Band', observed=False).agg(
    Total_Sales=('Sales', 'sum'),
    Total_Profit=('Profit', 'sum')
).reset_index()
disc_summary['Profit_Margin_%'] = (disc_summary['Total_Profit'] / disc_summary['Total_Sales']) * 100

colors = ['#2ca02c' if x > 0 else '#d62728' for x in disc_summary['Profit_Margin_%']]
bars = plt.bar(disc_summary['Discount_Band'], disc_summary['Profit_Margin_%'], color=colors, width=0.55, edgecolor='black', alpha=0.85)
plt.axhline(0, color='black', linewidth=1)
plt.title('Impact of Discount Bands on Operating Profit Margin (%)', fontsize=14, fontweight='bold', pad=15)
plt.xlabel('Discount Band', fontsize=12, fontweight='bold')
plt.ylabel('Profit Margin (%)', fontsize=12, fontweight='bold')
for bar in bars:
    yval = bar.get_height()
    va = 'bottom' if yval >= 0 else 'top'
    plt.text(bar.get_x() + bar.get_width()/2.0, yval + (2 if yval >= 0 else -6), f'{yval:.1f}%', ha='center', va=va, fontweight='bold', fontsize=11)
plt.tight_layout()
plt.savefig('d:/kanishka/visualizations/1_discount_margin_erosion.png', dpi=300)
plt.close()

# Chart 2: Regional Sales and Profit
plt.figure(figsize=(10, 5))
mkt_summary = df.groupby('Market').agg(Sales=('Sales', 'sum'), Profit=('Profit', 'sum')).reset_index().sort_values(by='Sales', ascending=False)
x = np.arange(len(mkt_summary))
width = 0.35
plt.bar(x - width/2, mkt_summary['Sales']/1e6, width, label='Sales ($M)', color='#1f77b4', edgecolor='black')
plt.bar(x + width/2, mkt_summary['Profit']/1e6, width, label='Profit ($M)', color='#2ca02c', edgecolor='black')
plt.xticks(x, mkt_summary['Market'], fontweight='bold')
plt.title('Global Market Performance: Sales vs. Net Profit ($ Millions)', fontsize=14, fontweight='bold', pad=15)
plt.ylabel('$ Millions', fontsize=12, fontweight='bold')
plt.legend(frameon=True)
plt.tight_layout()
plt.savefig('d:/kanishka/visualizations/2_market_sales_profit.png', dpi=300)
plt.close()

# Chart 3: Sub-Category Profitability Breakdown
plt.figure(figsize=(11, 6))
sub_summary = df.groupby('Sub-Category').agg(Profit=('Profit', 'sum')).reset_index().sort_values(by='Profit', ascending=True)
colors = ['#d62728' if x < 0 else '#1f77b4' for x in sub_summary['Profit']]
plt.barh(sub_summary['Sub-Category'], sub_summary['Profit']/1000, color=colors, edgecolor='black')
plt.axvline(0, color='black', linewidth=1)
plt.title('Sub-Category Net Profit / Loss ($ Thousands) - Highlighting Loss Centers', fontsize=14, fontweight='bold', pad=15)
plt.xlabel('Net Profit ($ in Thousands)', fontsize=12, fontweight='bold')
plt.ylabel('Sub-Category', fontsize=12, fontweight='bold')
plt.tight_layout()
plt.savefig('d:/kanishka/visualizations/3_subcategory_profit_loss.png', dpi=300)
plt.close()

# Chart 4: Shipping Days vs Order Priority
plt.figure(figsize=(8, 5))
sns.boxplot(data=df, x='Order Priority', y='Shipping_Days', order=['Critical', 'High', 'Medium', 'Low'], palette='Set2')
plt.title('Fulfillment Cycle: Actual Shipping Days by Stated Order Priority', fontsize=14, fontweight='bold', pad=15)
plt.xlabel('Order Priority Level', fontsize=12, fontweight='bold')
plt.ylabel('Days from Order to Shipment', fontsize=12, fontweight='bold')
plt.tight_layout()
plt.savefig('d:/kanishka/visualizations/4_shipping_duration_priority.png', dpi=300)
plt.close()

print("Charts created successfully.")
