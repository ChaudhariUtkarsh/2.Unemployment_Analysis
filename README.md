# 📊 Unemployment Analysis with Python

## 📌 Project Overview

Unemployment Analysis with Python is a data analysis project focused on understanding unemployment trends across different regions of India.

The project uses Python libraries to clean, analyze, and visualize unemployment data. It explores region-wise unemployment rates, monthly trends, state-wise comparisons, correlations between numerical variables, and changes in unemployment before and after March 2020.

The main objective is to identify unemployment patterns and present meaningful insights through interactive visualizations and a Jupyter Notebook.

---

## 🎯 Project Objectives

- Analyze unemployment rates across different regions of India.
- Study monthly unemployment trends.
- Compare unemployment rates across three major states.
- Identify the top 10 regions with the highest average unemployment rates.
- Analyze correlations between unemployment rate, employment count, and labour participation rate.
- Compare Pre-COVID and Post-COVID unemployment rates.
- Generate a cleaned dataset for further analysis.

---

## 📂 Dataset Information

**Dataset Name:** Unemployment in India

**Dataset Source:** Kaggle

**Dataset Author:** Gokulraj K M V

**Kaggle Link:**  
https://www.kaggle.com/datasets/gokulrajkmv/unemployment-in-india

**Original Dataset File:** `Unemployment in India.csv`

**Original Dataset Shape:** 768 rows × 7 columns

**Data Period:** May 2019 – June 2020

The dataset contains unemployment-related information across Indian regions, including Rural and Urban areas.

### Dataset Columns

| Column | Description |
|---|---|
| Region | Name of the Indian region |
| Date | Observation date |
| Frequency | Data observation frequency |
| Estimated Unemployment Rate (%) | Estimated unemployment percentage |
| Estimated Employed | Estimated number of employed people |
| Estimated Labour Participation Rate (%) | Labour participation percentage |
| Area | Rural or Urban area |

---

## 🛠️ Technologies Used

- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Streamlit
- Plotly
- Jupyter Notebook

---

## 📋 Project Features

### 1. Data Loading
- Load the unemployment dataset using Pandas.
- Display the first few records.

### 2. Shape Inspection
- Check the number of rows and columns.
- Display column names and dataset information.
- Generate statistical summaries.

### 3. Missing Value Analysis
- Identify missing values in each column.
- Check duplicate records.

### 4. Data Cleaning and Type Conversion
- Remove extra spaces from column names and text values.
- Convert Date into datetime format.
- Convert numerical columns into appropriate numeric types.
- Remove rows with missing essential values.
- Remove duplicate records.

### 5. Region-wise Analysis
- Calculate average unemployment rates for each region.
- Visualize region-wise unemployment rates using a bar chart.

### 6. Month-wise Trends
- Calculate monthly average unemployment rates.
- Display changes in unemployment using a line chart.

### 7. Three-State Combined Chart
- Compare unemployment trends for:
  - Maharashtra
  - Uttar Pradesh
  - Karnataka
- Visualize state-wise changes using a combined time-series line chart.

### 8. Top 10 Regions Bar Chart
- Identify the top 10 regions with the highest average unemployment rates.
- Display the results using a horizontal bar chart.

### 9. Correlation Heatmap
- Analyze the correlation between:
  - Estimated Unemployment Rate (%)
  - Estimated Employed (Employment Count)
  - Estimated Labour Participation Rate (%)
- Visualize relationships using a Seaborn heatmap.

**Note:** Estimated Employed represents employment count, not employment rate.

### 10. Pre-COVID vs Post-COVID Analysis
- Divide the dataset using 1 March 2020 as the cutoff date.
- Pre-COVID: Before 1 March 2020.
- Post-COVID: On or after 1 March 2020.
- Calculate average unemployment rates for both periods.
- Compare results using a bar chart.

### 11. Written Observations
- Add seven Markdown observation sections between analysis and visualization sections.
- Explain important patterns and findings.

### 12. Final Findings
- Display overall average unemployment rate.
- Identify regions with the highest and lowest average unemployment rates.
- Display Pre-COVID and Post-COVID comparisons.

### 13. Cleaned Dataset Export
- Export the cleaned dataset as `cleaned_unemployment_data.csv`.

---

## 📊 Streamlit Dashboard Features

The project also includes an interactive Streamlit dashboard.

### Dashboard Pages

- **Home:** Project introduction and overview.
- **Dashboard:** Key unemployment statistics, monthly trends, Top 10 regions, Three-State Combined Chart, and Correlation Heatmap.
- **State Analysis:** State-wise unemployment trends and Rural vs Urban analysis.
- **COVID Analysis:** Pre-COVID and Post-COVID comparison.
- **Dataset:** Dataset preview, filtering, and CSV download.

---

## 📁 Project Structure

```text
2.Unemployment_Analysis/
│
├── app.py
│
├── Unemployment in India.csv
│
├── cleaned_unemployment_data.csv
│
├── Unemployment_Analysis.ipynb
│
├── README.md
│
├── requirements.txt
│
└── images/
    └── background.jpg
```

---

## ⚙️ Installation and Setup

### Step 1: Clone the Repository

```bash
git clone YOUR_GITHUB_REPOSITORY_URL
```

### Step 2: Navigate to Project Folder

```bash
cd 2.Unemployment_Analysis
```

### Step 3: Create Virtual Environment

```bash
python -m venv venv
```

### Step 4: Activate Virtual Environment

**Windows PowerShell:**

```powershell
.\venv\Scripts\Activate.ps1
```

### Step 5: Install Required Libraries

```bash
pip install -r requirements.txt
```

### Step 6: Run Jupyter Notebook

```bash
jupyter notebook
```

Open `Unemployment_Analysis.ipynb` and select:

**Kernel → Restart Kernel and Run All Cells**

### Step 7: Run Streamlit Application

```bash
streamlit run app.py
```

The application will open in your browser.

---

## 📦 Requirements

Example `requirements.txt`:

```text
pandas
numpy
matplotlib
seaborn
streamlit
plotly
jupyter
```

---

## 📈 Expected Project Outcomes

- Understanding unemployment patterns across Indian regions.
- Identifying regions with relatively high unemployment rates.
- Analyzing monthly unemployment changes.
- Comparing unemployment trends across selected states.
- Understanding correlations between unemployment, employment count, and labour participation.
- Comparing average unemployment rates before and after March 2020.
- Creating an interactive unemployment analysis dashboard.

---

## ⚠️ Limitations

- The dataset covers May 2019 to June 2020 only.
- The analysis depends on the quality and coverage of the available dataset.
- Correlation does not establish causation.
- The Pre-COVID and Post-COVID comparison shows differences in averages but does not prove that COVID-19 caused those changes.
- The results should not be interpreted as current unemployment statistics.

---

## 👨‍💻 Author

**Utkarsh Y. Chaudhari**

BE – Information Technology  
Data Science

---

## 🏁 Conclusion

This project demonstrates how Python can be used for data cleaning, exploratory data analysis, statistical analysis, and visualization.

By analyzing unemployment data across Indian regions, the project provides insights into regional differences, monthly trends, state-wise comparisons, and Pre-COVID vs Post-COVID unemployment patterns.

The Jupyter Notebook and Streamlit dashboard make the analysis easier to understand and explore.

---

## 🔗 Dataset Reference

Kaggle – Unemployment in India:  
https://www.kaggle.com/datasets/gokulrajkmv/unemployment-in-india
