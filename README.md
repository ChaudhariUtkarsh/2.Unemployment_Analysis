# Unemployment Analysis with Python

## Project Overview

The **Unemployment Analysis with Python** project focuses on performing Exploratory Data Analysis (EDA) on unemployment data in India. The project explores regional unemployment patterns, monthly trends, employment indicators, and the impact of the COVID-19 period.

The project uses Python data analysis and visualization libraries to understand unemployment trends and present insights through a Jupyter Notebook and an interactive Streamlit dashboard.

## Objectives

- Analyze unemployment trends across different Indian regions.
- Study month-wise unemployment rate changes.
- Compare unemployment trends across major states.
- Identify the top 10 regions with the highest average unemployment rate.
- Examine correlations between unemployment rate, employment count, and labour participation rate.
- Compare unemployment levels before and after the COVID-19 split date.
- Build an interactive Streamlit dashboard for data exploration.

## Dataset Information

**Dataset Name:** Unemployment in India

**Source:** Kaggle

**Dataset Link:**  
https://www.kaggle.com/datasets/gokulrajkmv/unemployment-in-india

**Dataset Details:**
- Original records: 768 rows
- Original columns: 7
- Regions: 28
- Date range after cleaning: May 2019 – June 2020

**Dataset Columns:**
- `Region`
- `Date`
- `Frequency`
- `Estimated Unemployment Rate (%)`
- `Estimated Employed`
- `Estimated Labour Participation Rate (%)`
- `Area`

The cleaned dataset also includes a `Month` column for monthly analysis.

## Technologies Used

- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Plotly
- Streamlit
- Jupyter Notebook

## Project Features

### 1. Data Loading and Inspection
- Load the unemployment dataset.
- Inspect dataset shape and column information.
- Check missing values and duplicate records.

### 2. Data Cleaning
- Remove unnecessary spaces from column names.
- Convert date and numerical columns into appropriate data types.
- Handle missing values.
- Remove duplicate records.
- Create a Month column.

### 3. Region-wise Analysis
- Calculate average unemployment rates by region.
- Visualize regional unemployment comparisons.

### 4. Month-wise Trend Analysis
- Analyze monthly changes in unemployment rates.
- Display trends using line charts.

### 5. Three-State Combined Chart
- Compare Maharashtra, Uttar Pradesh, and Karnataka.
- Visualize monthly unemployment trends together.

### 6. Top 10 Regions Analysis
- Identify the top 10 regions with the highest average unemployment rates.
- Display results using a bar chart.

### 7. Correlation Heatmap
- Analyze correlations between:
  - Estimated Unemployment Rate (%)
  - Estimated Employed
  - Estimated Labour Participation Rate (%)

**Dataset Limitation:** The dataset provides Estimated Employed as an employment count, not an employment-rate percentage. Therefore, the heatmap uses Employment Count.

### 8. Pre-COVID vs Post-COVID Analysis
- COVID split date: `2020-03-01`
- Calculate average unemployment rate before the split date.
- Calculate average unemployment rate on and after the split date.
- Compare both periods using a bar chart.

### 9. Written Observations
- Include seven Markdown observation sections in the Jupyter Notebook.
- Explain data cleaning, regional trends, monthly trends, state comparisons, top 10 regions, correlation, and COVID-period analysis.

### 10. Cleaned Dataset Export
- Export the cleaned dataset as `cleaned_unemployment_data.csv`.
- Verify the exported dataset's shape and missing values.

## Streamlit Dashboard Features

The interactive Streamlit application includes the following pages:

### Home
- Project introduction.
- Overview of unemployment analysis.

### Dashboard
- Key performance indicators.
- Monthly unemployment trend.
- Top 10 regions chart.
- Three-state combined chart.
- Correlation heatmap.

### State Analysis
- Select and analyze individual regions.
- View unemployment trends.
- Compare Rural and Urban areas.

### COVID Analysis
- Pre-COVID and Post-COVID comparison.
- Average unemployment rate analysis.

### Dataset
- View cleaned dataset.
- Filter records.
- Download dataset as CSV.
- Inspect dataset information.

## Project Structure

```text
2.Unemployment_Analysis/
│
├── app.py
├── Unemployment_Analysis.ipynb
│
├── Unemployment in India.csv
├── cleaned_unemployment_data.csv
│
├── README.md
├── requirements.txt
│
└── images/
    └── background.jpg
```

## Installation and Setup

### Step 1: Clone the Repository

```bash
git clone YOUR_GITHUB_REPOSITORY_URL
```

### Step 2: Navigate to the Project Folder

```bash
cd 2.Unemployment_Analysis
```

### Step 3: Create a Virtual Environment (Optional)

```bash
python -m venv venv
```

Activate it on Windows:

```bash
venv\Scripts\activate
```

### Step 4: Install Required Libraries

```bash
pip install -r requirements.txt
```

### Step 5: Run Jupyter Notebook

```bash
jupyter notebook
```

Open `Unemployment_Analysis.ipynb` and execute the cells.

### Step 6: Run Streamlit Application

```bash
streamlit run app.py
```

The application will open in your default browser.

## Requirements

Create a `requirements.txt` file with:

```text
streamlit
pandas
numpy
plotly
matplotlib
seaborn
jupyter
```

Install dependencies using:

```bash
pip install -r requirements.txt
```

## Limitations

- The dataset covers May 2019 to June 2020 after cleaning, so it does not represent current unemployment statistics.
- The dataset contains an employment count rather than an employment-rate percentage.
- The COVID analysis is a descriptive comparison and does not establish causation.
- Correlation between variables does not imply a cause-and-effect relationship.
- Findings depend on the quality and coverage of the supplied dataset.

## Conclusion

The Unemployment Analysis with Python project provides an exploratory understanding of unemployment trends across Indian regions and over time.

Through data cleaning, statistical analysis, visualizations, correlation analysis, and pre-COVID versus post-COVID comparison, the project highlights patterns in the available unemployment dataset.

The Streamlit dashboard makes the analysis accessible through an interactive interface.

---

**Project:** Unemployment Analysis with Python  
**Internship Organization:** Oasis Infobyte  
**Task:** Task 2 – Data Science Internship  
**Tools:** Python, Pandas, NumPy, Matplotlib, Seaborn, Plotly, Streamlit, Jupyter Notebook
