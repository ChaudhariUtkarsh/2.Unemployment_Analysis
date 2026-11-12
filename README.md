# Unemployment Analysis with Python

## 1. Project Overview

Unemployment Analysis with Python is a Data Science project developed as part of the Oasis Infobyte Internship Program.

The project performs Exploratory Data Analysis (EDA) on unemployment data in India to identify regional differences, monthly trends, and changes observed during the COVID-19 period. It uses Python data-analysis and visualization libraries and includes an interactive Streamlit dashboard.

---

## 2. Project Objectives

- Analyze unemployment trends across Indian regions.
- Calculate region-wise average unemployment rates.
- Examine month-wise unemployment trends.
- Compare unemployment trends across at least three major states.
- Identify the ten regions with the highest average unemployment rates.
- Explore correlations among unemployment rate, estimated employment rate, and labour participation rate.
- Compare unemployment rates before and after March 2020.
- Present the analysis through charts, written observations, and an interactive dashboard.

---

## 3. Dataset Information

- **Dataset Name:** Unemployment in India
- **Source:** Kaggle
- **Dataset Link:** [https://www.kaggle.com/datasets/gokulrajkmv/unemployment-in-india](https://www.kaggle.com/datasets/gokulrajkmv/unemployment-in-india)

### Original Dataset

| Detail | Value |
|--------|-------|
| Records | 768 |
| Columns | 7 |
| Regions | 28 |
| Date Range | May 2019 – June 2020 |

### Original Dataset Columns

| Column | Description |
|--------|-------------|
| Region | Indian state or region |
| Date | Observation date |
| Frequency | Data recording frequency |
| Estimated Unemployment Rate (%) | Estimated unemployment percentage |
| Estimated Employed | Estimated number of employed people |
| Estimated Labour Participation Rate (%) | Estimated labour participation percentage |
| Area | Rural or Urban classification |

### Cleaned Dataset

The project removes rows with missing values in required analysis columns, removes duplicate rows, converts data types, and creates additional analysis columns.

| Detail | Value |
|--------|-------|
| Records after cleaning | 740 |
| Columns in the updated cleaned file | 9 |
| Missing values in required cleaned data | 0 |
| Duplicate rows after cleaning | 0 |

The cleaned dataset contains the original seven columns plus:

- **Month** – month derived from the Date column for monthly analysis.
- **Estimated Employment Rate (%)** – an estimated value derived for the correlation heatmap.

> **Important:** `Estimated Employment Rate (%)` is not directly reported in the original Kaggle dataset. It is a derived estimate, and its assumptions and limitations are explained in the Correlation Heatmap section.

The cleaned data is saved as `cleaned_unemployment_data.csv`.

---

## 4. Technologies Used

### Programming Language
- Python

### Python Libraries
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Plotly

### Development Tools
- Jupyter Notebook
- Visual Studio Code
- Streamlit
- Git and GitHub

---

## 5. Project Features

1. Data loading and inspection
2. Dataset shape and column inspection
3. Missing-value and duplicate detection
4. Data cleaning and type conversion
5. Region-wise average unemployment analysis
6. Month-wise unemployment trend analysis
7. Three-state combined time-series chart
8. Top 10 regions by average unemployment rate
9. Correlation heatmap
10. Pre-COVID vs Post-COVID comparison
11. Written observations and findings
12. Cleaned dataset export
13. Interactive Streamlit dashboard

---

## 6. Data Cleaning and Preprocessing

The following preprocessing steps are performed:

- Load the original CSV file using Pandas.
- Remove extra spaces from column names and text values.
- Convert `Date` to a datetime data type.
- Convert unemployment rate, estimated employment count, and labour participation rate to numeric data types.
- Remove records missing values in required analysis columns.
- Remove duplicate records.
- Create a `Month` column from the date.
- Derive `Estimated Employment Rate (%)` for the correlation analysis.
- Sort the cleaned data by region and date.

### Final Cleaned Dataset

| Detail | Value |
|--------|-------|
| Rows | 740 |
| Columns | 9 |
| Missing values | 0 |
| Duplicate rows | 0 |

> The exact cleaned output depends on the source CSV and the preprocessing steps used in the notebook.

---

## 7. Exploratory Data Analysis (EDA)

### 7.1 Region-wise Average Unemployment

The average unemployment rate is calculated for each region. This analysis helps identify regions with relatively higher and lower average unemployment rates.

### 7.2 Month-wise Unemployment Trends

The data is grouped by month and the average unemployment rate is calculated. A time-series line chart is used to examine how the average unemployment rate changes over the available period.

### 7.3 Three-State Time-Series Comparison

A combined time-series line chart compares the unemployment rates of:

- Maharashtra
- Uttar Pradesh
- Karnataka

The chart uses date on the X-axis, unemployment rate on the Y-axis, and a separate line for each state.

### 7.4 Top 10 Regions by Average Unemployment

A bar chart displays the ten regions with the highest average unemployment rates. The chart is based on the average unemployment rate calculated for each region.

> The term **regions** is used because the dataset may include Union Territories as well as states.

### 7.5 Correlation Heatmap

The correlation heatmap displays the pairwise correlations among these three variables:

- Estimated Unemployment Rate (%)
- Estimated Employment Rate (%)
- Estimated Labour Participation Rate (%)

#### Estimated Employment Rate Calculation

The original dataset does not directly provide an employment-rate column. Therefore, the project derives an estimated employment rate using:

```
Estimated Employment Rate (%) =
    Labour Participation Rate (%) × (1 - Unemployment Rate (%) / 100)
```

This calculation follows the relationship:

- Labour force participation rate = labour force / population × 100
- Unemployment rate = unemployed people / labour force × 100
- Employment-to-population rate = employed people / population × 100

The derivation assumes that the unemployment rate and labour participation rate use compatible population bases, definitions, and reference periods.

#### Limitations and Interpretation

- The derived employment rate is an estimate; it is not an independently reported value in the original dataset.
- Its correlation with unemployment rate is partly determined by the formula used to calculate it.
- Therefore, this correlation should not be interpreted as an independent empirical finding.
- Correlation describes statistical association and does not establish causation.

---

## 8. Pre-COVID vs Post-COVID Analysis

The project divides the available observations using **1 March 2020** as the cutoff date:

- **Pre-COVID:** dates before 1 March 2020.
- **Post-COVID:** dates on or after 1 March 2020.

The average unemployment rate is calculated for each period.

### Comparison Results

| Period | Records | Average Unemployment Rate |
|--------|--------:|-------------------------:|
| Pre-COVID | 536 | 9.51% |
| Post-COVID | 204 | 17.77% |

**Difference:** approximately 8.26 percentage points.

> The available dataset shows a higher average unemployment rate in the period beginning March 2020 than in the earlier period. This is a descriptive comparison; it does not prove that COVID-19 alone caused the observed change.

---

## 9. Streamlit Dashboard

An interactive dashboard is developed using Streamlit.

### Dashboard Pages

**1. Home**
- Project introduction and objectives
- Key dataset information
- Dataset preview

**2. Dashboard**
- Key unemployment statistics
- Monthly unemployment trend
- Top 10 regions chart
- Three-state comparison chart
- Correlation heatmap

**3. State Analysis**
- State/region selection
- State-wise unemployment trend
- Rural vs Urban comparison, where the Area field is available
- Selected region's data

**4. COVID Analysis**
- Pre-COVID and Post-COVID averages
- Difference in percentage points
- Comparison chart
- Interpretation and limitation

**5. Dataset**
- Dataset preview
- Region filter
- Dataset information and missing-value summary
- CSV download option

---

## 10. Project Structure

```text
2.Unemployment_Analysis/
│
├── app.py
├── Unemployment in India.csv
├── cleaned_unemployment_data.csv
├── Unemployment_Analysis.ipynb
├── README.md
├── requirements.txt
│
└── images/
    └── background.jpg
```

> If your notebook has a different filename, use that actual filename when opening it.

---

## 11. Installation and Setup

### Step 1: Open the Project Folder

```bash
cd "E:\LocakDisk C\oasisinfobyte\2.Unemployment_Analysis"
```

### Step 2: Create a Virtual Environment (Optional)

```bash
python -m venv venv
```

### Step 3: Activate the Virtual Environment

**PowerShell:**
```powershell
.\venv\Scripts\Activate.ps1
```

> If PowerShell blocks script activation, use Command Prompt instead:

**Command Prompt:**
```cmd
venv\Scripts\activate
```

### Step 4: Install Dependencies

```bash
python -m pip install -r requirements.txt
```

### Step 5: Run the Jupyter Notebook

```bash
jupyter notebook
```

Open `Unemployment_Analysis.ipynb` (or your actual notebook filename) and run the cells in order.

### Step 6: Run the Streamlit Application

Keep `app.py`, `Unemployment in India.csv`, and the `images` folder in the project structure shown above. Then run:

```bash
streamlit run app.py
```

The dashboard should open in your default web browser.

---

## 12. Limitations

- The dataset covers a limited period from May 2019 to June 2020; it does not describe current unemployment conditions in India.
- The original dataset provides estimated employment count, not a directly reported employment rate.
- The employment-rate variable used in the heatmap is derived from unemployment rate and labour participation rate. Its validity depends on compatible definitions and population bases.
- The derived employment-rate correlation with unemployment rate is partly mathematical and should not be treated as an independent empirical relationship.
- The Pre-COVID and Post-COVID comparison is descriptive and does not establish that the pandemic alone caused the observed changes.
- Results depend on the quality, coverage, and definitions of the source dataset.

---

## 13. Conclusion

This project uses Python to explore unemployment trends in India across regions and over time. It includes data cleaning, exploratory analysis, visual comparisons, a correlation heatmap, and a descriptive Pre-COVID vs Post-COVID analysis.

The analysis highlights differences in regional unemployment averages and changes in the available observations across the selected periods. An interactive Streamlit dashboard provides a way to explore the results.

The project demonstrates practical use of Pandas, NumPy, Matplotlib, Seaborn, Plotly, and Streamlit for data analysis and visualization.

---

## Project Information

| Detail | Value |
|--------|-------|
| Internship Organization | Oasis Infobyte |
| Task | Task 2 – Unemployment Analysis with Python |
| Domain | Data Science |
| Programming Language | Python |
| Tools | Jupyter Notebook, Streamlit, VS Code, GitHub |
| Author | Utkarsh Y. Chaudhari |

---

**Thank You!**
