# VirtuBox Infotech - Data Analyst Assessment Project

**Role:** Data Analyst (B2B Technology Company Context)  
**Dataset:** Global Superstore (51,290 Transactions across 147 Countries)  
**Deliverable Package:** Google Sheet, Python Pipeline, Jupyter Notebook, 7-Slide Presentation, and Executive Dashboard Blueprint.

---

## 1. Executive Summary & Business Context
As a Data Analyst at a B2B technology and commercial solutions firm, leadership requested an end-to-end investigation into **business opportunities, performance gaps, and operational improvements**. 

While the enterprise achieved strong top-line sales of **$12.64M**, net operating profit stalled at **$1.47M (11.6% margin)**. Our analysis uncovered critical profit leakages:
1. **The Heavy Discount Trap:** Discounts exceeding 20% caused **-$814,800+** in cumulative losses.
2. **Product Loss Centers:** The **Tables** sub-category lost **-$64,083** globally (-8.46% margin) due to freight overhead and promotional discounts.
3. **Regional Disparities:** **APAC** ($436K profit) and **EU** ($373K profit) produce over 55% of global profit, while emerging markets suffer high logistics drain.
4. **Logistics Bottlenecks:** Critical priority orders meet SLA (1.8 days), but expedited courier surcharges consume 26.5% of order value.

By instituting pricing floor guardrails, restructuring underperforming product lines, and reallocating sales resources, the company can immediately recover **$400,000–$500,000 in annual EBITDA**.

---

## 2. Directory & Deliverables Structure

All deliverables required by VirtuBox are generated and located in this directory:

```
d:/kanishka/
│
├── Assessment-Test-(Data-Analyst)-v1 (1).pdf    # Assessment Brief
├── Global_Superstore_Raw.csv                   # Raw Dataset (51,290 rows × 24 cols)
├── Processed_Data.csv                          # Analysis-Ready Dataset with Engineered Features
│
├── VirtuBox_Assessment_Workbook.xlsx           # Excel Workbook containing Tabs: Q1, Q2, Q3, Q4, Q5, Q6, Q7, Q8, Q10
├── VirtuBox_Analysis_Notebook.ipynb            # Jupyter Notebook with full EDA, Code & Visualizations
├── VirtuBox_Executive_Presentation.pptx        # 7-Slide Executive PowerPoint Presentation (Ready for Google Slides)
├── process_data.py                             # Python Data Engineering & Visualization Pipeline
├── generate_deliverables.py                    # Script generating the complete submission package
│
├── visualizations/                             # High-Resolution Visualizations
│   ├── 1_discount_margin_erosion.png           # Profit margin drop across discount tiers
│   ├── 2_market_sales_profit.png               # Sales vs Profit across 7 global markets
│   ├── 3_subcategory_profit_loss.png           # Sub-category profit & loss breakdown
│   └── 4_shipping_duration_priority.png        # Fulfillment lead time by priority level
│
└── README.md                                   # This Project Documentation & Methodology
```

---

## 3. Google Sheet Setup Instructions
To prepare the **Single Google Sheet** required for final submission:

1. Open **Google Drive** and click **New > Google Sheets**. Name the spreadsheet:  
   `VirtuBox_Data_Analyst_Assessment_[Your_Name]`
2. Import the worksheets:
   * **Tab 1: `Data`** — Upload `Global_Superstore_Raw.csv`.
   * **Tab 2: `Q1`** — Copy from `VirtuBox_Assessment_Workbook.xlsx` (Sheet `Q1`).
   * **Tab 3: `Q2`** — Copy from `VirtuBox_Assessment_Workbook.xlsx` (Sheet `Q2`).
   * **Tab 4: `Processed Data`** — Upload `Processed_Data.csv`.
   * **Tab 5: `Q3`** — Copy from `VirtuBox_Assessment_Workbook.xlsx` (Sheet `Q3`).
   * **Tab 6: `Q4`** — Copy from `VirtuBox_Assessment_Workbook.xlsx` (Sheet `Q4`).
   * **Tab 7: `Q5`** — Copy from `VirtuBox_Assessment_Workbook.xlsx` (Sheet `Q5`).
   * **Tab 8: `Q6`** — Copy from `VirtuBox_Assessment_Workbook.xlsx` (Sheet `Q6`).
   * **Tab 9: `Q7`** — Copy from `VirtuBox_Assessment_Workbook.xlsx` (Sheet `Q7`).
   * **Tab 10: `Q8`** — Copy from `VirtuBox_Assessment_Workbook.xlsx` (Sheet `Q8`) and insert your Looker Studio screenshots and link.
   * **Tab 11: `Q10`** — Copy from `VirtuBox_Assessment_Workbook.xlsx` (Sheet `Q10`).

*(Tip: You can also open `VirtuBox_Assessment_Workbook.xlsx` directly in Google Sheets by selecting **File > Open > Upload**!)*

---

## 4. Google Looker Studio Dashboard Setup (Worksheet Q8)
To create the interactive Google Looker Studio dashboard:

1. Go to [Looker Studio](https://lookerstudio.google.com/) and click **Create > Report**.
2. Select **Google Sheets** as the connector and select your uploaded spreadsheet (`Processed Data` tab).
3. Build the following 5 visual components:
   * **Top Executive Scorecards:**
     - Metric 1: `Sales` (Sum, display as $12.6M)
     - Metric 2: `Profit` (Sum, display as $1.47M)
     - Metric 3: `Profit_Margin_%` (Average / calculated field, display as 11.6%)
     - Metric 4: `Order ID` (Count Distinct, display as 51,290)
   * **Chart 1 (Discount vs Margin):** Column Chart with Dimension `Discount_Band` and Metric `Profit_Margin_%` or `Profit`.
   * **Chart 2 (Geographic Performance):** Geo Map or Clustered Bar Chart with Dimension `Market` / `Country` and Metrics `Sales`, `Profit`.
   * **Chart 3 (Product Breakdown):** Horizontal Bar Chart with Dimension `Sub-Category` and Metric `Profit` (Sorted ascending to highlight Tables).
   * **Chart 4 (Logistics SLA):** Clustered Column Chart with Dimension `Order Priority` and Metric `Shipping_Days` (Average).
   * **Interactive Global Filters:** Dropdown filters for `Order_Year`, `Market`, `Segment`, and `Category`.
4. Click **Share**, set permissions to *"Anyone with the link can view"*, copy the link, take a screenshot of your report, and paste both into **Worksheet Q8**.

---

## 5. Final Google Drive Submission Checklist
Create **ONE Google Drive folder** named:  
`VirtuBox_Assessment_DataAnalyst_[Your_Name]`

Include:
- [x] **1. Google Sheet:** Containing all 11 tabs (`Data`, `Q1`, `Q2`, `Processed Data`, `Q3`, `Q4`, `Q5`, `Q6`, `Q7`, `Q8`, `Q10`).
- [x] **2. Code:** [VirtuBox_Analysis_Notebook.ipynb](file:///d:/kanishka/VirtuBox_Analysis_Notebook.ipynb) or [process_data.py](file:///d:/kanishka/process_data.py).
- [x] **3. Supporting Calculations / Files:** [Processed_Data.csv](file:///d:/kanishka/Processed_Data.csv) and chart images from `visualizations/`.
- [x] **4. Management Presentation:** [VirtuBox_Executive_Presentation.pptx](file:///d:/kanishka/VirtuBox_Executive_Presentation.pptx) (or upload to Google Slides).
- [x] **5. README / Methodology:** This [README.md](file:///d:/kanishka/README.md) file.
