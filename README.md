# Unemployment Analysis with Python

## 1. Project Overview

Unemployment Analysis with Python is a Data Science project developed as
part of the Oasis Infobyte Internship Program.

The project focuses on Exploratory Data Analysis (EDA) of unemployment
data in India to identify regional and monthly unemployment trends and
understand the changes observed during the COVID-19 pandemic.

The project uses Python libraries such as Pandas, Matplotlib, Seaborn,
and Plotly for data analysis and visualization. A Streamlit dashboard is
also developed to present the analysis interactively.

## 2. Objective

The main objectives of this project are:

- Analyze unemployment trends across different regions of India.

- Calculate region-wise average unemployment rates.

- Understand month-wise unemployment trends.

- Compare unemployment rates across major Indian states.

- Identify the top 10 regions with the highest average unemployment
rates.

- Study correlations between unemployment rate, employment count, and
labour participation rate.

- Compare unemployment rates before and after March 2020.

- Create an interactive Streamlit dashboard for data visualization.

## 3. Dataset Information

**Dataset Name:** Unemployment in India

**Dataset Source:** Kaggle

**Dataset Link:**
https://www.kaggle.com/datasets/gokulrajkmv/unemployment-in-india

**Original Dataset Details:**

- Total Records: 768

- Total Columns: 7

- Total Regions: 28

- Date Range: May 2019 to June 2020

### Dataset Columns

| Column Name | Description |

|---|---|

| Region | Indian state or region |

| Date | Observation date |

| Frequency | Data recording frequency |

| Estimated Unemployment Rate (%) | Estimated unemployment percentage
|

| Estimated Employed | Estimated number of employed people |

| Estimated Labour Participation Rate (%) | Labour participation
percentage |

| Area | Rural or Urban classification |

**Cleaned Dataset Details:**

- Total Records: 740

- Total Columns: 8

- Missing Values: 0

- Additional Column: Month

The cleaned dataset is exported as `cleaned_unemployment_data.csv`.

## 4. Technologies Used

### Programming Language

- Python

### Libraries

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

## 5. Project Features

The project includes the following features:

1. Data Loading and Inspection

2. Dataset Shape and Column Inspection

3. Missing Value and Duplicate Detection

4. Data Cleaning and Type Conversion

5. Region-wise Average Unemployment Analysis

6. Month-wise Unemployment Trend Analysis

7. Three-State Combined Time-Series Chart

8. Top 10 Regions with Highest Average Unemployment

9. Correlation Heatmap

10. Pre-COVID vs Post-COVID Analysis

11. Written Observations and Findings

12. Cleaned Dataset Export

13. Interactive Streamlit Dashboard

## 6. Data Cleaning

The following data cleaning operations are performed:

- Loaded the original CSV dataset using Pandas.

- Removed unnecessary spaces from column names.

- Removed extra spaces from text values.

- Converted the Date column into datetime format.

- Converted unemployment rate, employment count, and labour
participation rate into numeric data types.

- Removed records with missing values in required analysis columns.

- Removed duplicate records.

- Created an additional Month column for monthly analysis.

- Sorted the cleaned dataset by region and date.

**Final Cleaned Dataset:**

- Rows: 740

- Columns: 8

- Missing Values: 0

## 7. Exploratory Data Analysis (EDA)

### 7.1 Region-wise Analysis

Calculated the average unemployment rate for each region to identify
regions with higher and lower unemployment levels.

### 7.2 Month-wise Trends

Analyzed monthly changes in unemployment rates to understand the overall
unemployment pattern over time.

### 7.3 Three-State Time-Series Analysis

Created a combined time-series line chart to compare unemployment trends
across:

- Maharashtra

- Uttar Pradesh

- Karnataka

### 7.4 Top 10 Regions Analysis

Created a bar chart showing the top 10 regions with the highest average
unemployment rates.

### 7.5 Correlation Heatmap

Created a correlation heatmap using the following numerical columns:

- Estimated Unemployment Rate (%)

- Estimated Employed

- Estimated Labour Participation Rate (%)

The heatmap helps identify positive and negative statistical
relationships among these variables.

**Note:** The original dataset contains an `Estimated
Employed` column representing employment count, not employment rate.
Therefore, employment count is used in the correlation heatmap instead
of employment rate.

Correlation indicates statistical association and does not establish
causation.

## 8. COVID-19 Analysis

The project compares unemployment rates before and after March 2020 to
study changes during the COVID-19 period.

**COVID-19 Cutoff Date:** 2020-03-01

### Comparison Results

| Period | Records | Average Unemployment Rate |

|---|---:|---:|

| Pre-COVID | 536 | 9.51% |

| Post-COVID | 204 | 17.77% |

**Difference:** Approximately 8.26 percentage points.

### Observation

The average unemployment rate increased from approximately 9.51% before
March 2020 to approximately 17.77% from March 2020 onward.

This comparison highlights a substantial increase in unemployment during
the post-COVID period. However, this descriptive analysis does not prove
that COVID-19 alone caused the increase.

## 9. Streamlit Dashboard

An interactive dashboard is developed using Streamlit to explore
unemployment data through visualizations and filters.

### Dashboard Pages

**1. Home**

- Project introduction

- Overview and navigation

**2. Dashboard**

- Key unemployment statistics

- Monthly unemployment trends

- Top 10 regions

- Three-state comparison chart

- Correlation heatmap

**3. State Analysis**

- Region selection

- State-wise unemployment trends

- Rural and Urban comparison

**4. COVID Analysis**

- Pre-COVID and Post-COVID comparison

- Average unemployment rates

- COVID-period visualization

**5. Dataset**

- Dataset preview

- Dataset filters

- Dataset information

- CSV download option

## 10. Project Structure

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

**Note:** The cleaned CSV file is generated after running the
notebook. The notebook filename in your folder may be
`Unemployment_Analysis_Updated.ipynb` if you are using the updated
version.

## 11. Installation and Setup

### Step 1: Clone the Repository

```bash

git clone <YOUR_GITHUB_REPOSITORY_URL>{=html}

```

### Step 2: Navigate to the Project Folder

```bash

cd 2.Unemployment_Analysis

```

### Step 3: Create a Virtual Environment (Optional)

```bash

python -m venv venv

```

### Step 4: Activate the Virtual Environment

For Windows:

```bash

venv`\Scripts`{=tex}`\activate`{=tex}

```

### Step 5: Install Required Libraries

```bash

pip install -r requirements.txt

```

### Step 6: Run Jupyter Notebook

```bash

jupyter notebook

```

Open `Unemployment_Analysis.ipynb` and run all cells.

### Step 7: Run Streamlit Application

```bash

streamlit run app.py

```

The Streamlit application will open in your default web browser.

## 12. Limitations

- The dataset covers a limited period from May 2019 to June 2020.

- The original dataset contains estimated employment count instead of
employment rate.

- Therefore, employment count is used in the correlation heatmap
instead of employment rate.

- The analysis is based on the available dataset and its recorded
observations.

- The Pre-COVID and Post-COVID comparison is descriptive and does not
establish a direct causal relationship between the pandemic and
unemployment changes.

- The results may not represent current unemployment conditions in
India.

### Correlation Heatmap Limitation

The original dataset does not contain an Employment Rate (%) column.

It provides Estimated Employed (employment count) instead.

Therefore, the correlation heatmap uses:

- Estimated Unemployment Rate (%)

- Estimated Employed

- Estimated Labour Participation Rate (%)

Employment count is not the same as employment rate. An actual
employment rate cannot be calculated without the required population
denominator.

## 13. Conclusion

This project provides an exploratory analysis of unemployment trends in
India using Python.

The analysis identifies regional differences, monthly trends, and
changes in unemployment rates across selected states.

The Pre-COVID and Post-COVID comparison shows an increase in the average
unemployment rate during the period beginning March 2020.

The project also demonstrates the use of Python data analysis libraries,
data cleaning techniques, statistical correlation, data visualization,
and Streamlit dashboard development.

Overall, this project provides practical experience in Exploratory Data
Analysis and communicating data-driven findings through interactive
visualizations.

## Project Information

**Internship Organization:** Oasis Infobyte

**Task:** Task 2 -- Unemployment Analysis with Python

**Domain:** Data Science

**Programming Language:** Python

**Tools:** Jupyter Notebook, Streamlit, VS Code, GitHub

**Author:** Utkarsh Y. Chaudhari

---

**Thank You!**