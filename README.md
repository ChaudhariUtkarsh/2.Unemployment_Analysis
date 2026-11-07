# Unemployment Analysis in India 📊

An interactive data analysis dashboard built with **Python** and **Streamlit** to explore unemployment trends across Indian states, with a focus on the impact of COVID-19.

---

## Project Overview

This project analyzes the **Unemployment in India** dataset (768 records across 28 states/regions) covering the period from **May 2019 to June 2020**. It provides visual insights into unemployment rates, employment figures, and labour participation rates — broken down by state and rural/urban area.

The project includes both an **Exploratory Data Analysis (EDA) notebook** and an **interactive Streamlit dashboard**.

---

## Features

### Streamlit Dashboard (`app.py`)
- **Home** — Project summary with key metrics (total records, states, average unemployment rate)
- **Dashboard** — Monthly unemployment trend line chart + Top 10 states bar chart
- **State Analysis** — Per-state unemployment trend and Rural vs Urban comparison
- **COVID Analysis** — Before vs After COVID-19 (March 25, 2020) unemployment comparison
- **Dataset** — Searchable, filterable table with CSV download option

### EDA Notebook (`Unemployment_Analysis.ipynb`)
1. Import Libraries
2. Load Dataset
3. Dataset Shape Inspection
4. Check Missing Values
5. Data Cleaning and Type Conversion
6. Statistical Summary
7. Region-wise Average Unemployment Rate
8. Month-wise Unemployment Trend
9. Time-Series Analysis of 3 Major States

---

## Dataset

**File:** `Unemployment in India.csv`

| Column | Description |
|---|---|
| Region | Indian state / region |
| Date | Month-end date (May 2019 – June 2020) |
| Frequency | Data frequency (Monthly) |
| Estimated Unemployment Rate (%) | Unemployment rate |
| Estimated Employed | Number of employed persons |
| Estimated Labour Participation Rate (%) | Labour participation rate |
| Area | Rural or Urban |

> **Note:** The dataset contains 28 missing rows (196 total missing values across all columns), which are dropped during data cleaning.

---

## Tech Stack

| Tool | Purpose |
|---|---|
| Python | Core language |
| Pandas | Data loading & processing |
| NumPy | Numerical operations |
| Matplotlib | Static charts (EDA notebook) |
| Seaborn | Statistical visualizations (EDA notebook) |
| Plotly | Interactive charts (dashboard) |
| Streamlit | Web dashboard |

---

## Project Structure

```
2.Unemployment_Analysis/
├── app.py                        # Streamlit dashboard app
├── Unemployment in India.csv     # Dataset (768 records, 7 columns)
├── requirements.txt              # Python dependencies
├── images/
│   └── background.jpg            # Dashboard background image
└── Unemployment_Analysis.ipynb   # Jupyter notebook (EDA)
```

---

## Getting Started

**1. Create and activate a virtual environment**
```bash
# Create
python -m venv venv

# Activate (Windows)
venv\Scripts\activate

# Activate (macOS/Linux)
source venv/bin/activate
```

**2. Install dependencies**
```bash
pip install -r requirements.txt
```

**3. Install core libraries (if not using requirements.txt)**
```bash
pip install pandas numpy matplotlib seaborn
```

**4. Run the app**
```bash
streamlit run app.py
```

**5. Open in browser**
```
http://localhost:8501
```

---

## Key Insights

- Unemployment rates spiked significantly **after COVID-19 lockdown** (March 2020)
- Urban areas generally show higher unemployment volatility than rural areas
- **Tripura** (28.35%) and **Haryana** (26.28%) recorded the highest average unemployment rates
- **Meghalaya** (4.80%) and **Odisha** (5.66%) recorded the lowest average unemployment rates
- Average unemployment rate across all states: **~11.79%**
- Maximum recorded unemployment rate: **76.74%**

