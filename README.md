# VirtuBox Infotech - Data Analyst Assessment Project

**Candidate:** Kanishka Verma  
**Role:** Data Analyst (B2B Technology Company Context)  
**Dataset:** Global Superstore (51,290 Transactions across 147 Countries)  
**Deliverable Package:** Google Sheet, Python Pipeline, Jupyter Notebook, 7-Slide Presentation, and Executive Dashboard Blueprint.

---

## 🔗 Project & Submission Links
* 📂 **Google Drive Submission Folder:**  
  [https://drive.google.com/drive/folders/1v1KsSuHtejugJlEo5WZgiNyOQSIrLdTF?usp=drive_link](https://drive.google.com/drive/folders/1v1KsSuHtejugJlEo5WZgiNyOQSIrLdTF?usp=drive_link)  
  *(Contains the complete Google Sheet with all 11 worksheets Q1–Q10, 7-slide presentation, Python notebook, and README methodology)*
* 💻 **GitHub Repository:**  
  [https://github.com/kanishkav7456-maker/Virtubox](https://github.com/kanishkav7456-maker/Virtubox)

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
The **Single Google Sheet** includes all required worksheets:

* **Tab 1: `Data`** — Raw Global Superstore transaction data (51,290 rows).
* **Tab 2: `Q1`** — Dataset name, source URL, description, selection rationale, and business opportunities.
* **Tab 3: `Q2`** — Problem statement, 5 key business questions, and 2 testable hypotheses.
* **Tab 4: `Processed Data`** — Fully transformed dataset with engineered features (`Profit_Margin_%`, `Shipping_Days`, `Discount_Band`).
* **Tab 5: `Q3`** — Data cleaning decision log (*Change | Why necessary | Risk if omitted*).
* **Tab 6: `Q4`** — 5 structured business insights (*Insight | Evidence | Why Selected | Business Impact | Recommendation*).
* **Tab 7: `Q5`** — Surprising result deep dive (The Heavy Discount Margin Trap).
* **Tab 8: `Q6`** — Data quality issues, 2 analytical limitations, and 1 conclusion that cannot safely be drawn.
* **Tab 9: `Q7`** — 3 Prioritized actionable management recommendations with owners, impact, and KPIs.
* **Tab 10: `Q8`** — Looker Studio dashboard architecture, shareable link, and screenshots.
* **Tab 11: `Q10`** — Responsible AI usage disclosure and methodology statement.

---

## 4. Google Looker Studio Dashboard Setup (Worksheet Q8)
The interactive executive dashboard tracks:
1. **Executive KPI Scorecards:** Total Revenue ($12.64M), Net Profit ($1.47M), Margin % (11.6%), Orders (51,290).
2. **Discount Margin Degradation:** Column chart showing positive margins for 0–20% discounts and severe negative collapse for discounts >20%.
3. **Regional Market Performance:** Clustered bar chart highlighting APAC and EU as primary profit drivers.
4. **Sub-Category Loss Centers:** Horizontal bar chart isolating Tables (-$64K) and high-loss furniture items.
5. **Interactive Controls:** Global filters by Year, Region/Market, Customer Segment, and Category.

---

## 5. Final Submission Package
All assessment requirements have been verified and packaged into:

📂 **Google Drive Submission Folder:**  
👉 [https://drive.google.com/drive/folders/1v1KsSuHtejugJlEo5WZgiNyOQSIrLdTF?usp=drive_link](https://drive.google.com/drive/folders/1v1KsSuHtejugJlEo5WZgiNyOQSIrLdTF?usp=drive_link)

- [x] **1. Google Sheet:** Contains all 11 tabs (`Data`, `Q1`, `Q2`, `Processed Data`, `Q3`, `Q4`, `Q5`, `Q6`, `Q7`, `Q8`, `Q10`).
- [x] **2. Code:** [VirtuBox_Analysis_Notebook.ipynb](VirtuBox_Analysis_Notebook.ipynb) & [process_data.py](process_data.py).
- [x] **3. Supporting Files:** [Processed_Data.csv](Processed_Data.csv) and charts in `visualizations/`.
- [x] **4. Management Presentation:** [VirtuBox_Executive_Presentation.pptx](VirtuBox_Executive_Presentation.pptx).
- [x] **5. README / Methodology:** This [README.md](README.md) file.
