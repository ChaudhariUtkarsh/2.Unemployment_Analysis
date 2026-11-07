# Unemployment Analysis in India 📊

An interactive data analysis dashboard built with **Python** and **Streamlit** to explore unemployment trends across Indian states, with a focus on the impact of COVID-19.

---

## Project Overview

This project analyzes the **Unemployment in India** dataset (768 records across 28 states/regions) covering the period from 2019 to 2020. It provides visual insights into unemployment rates, employment figures, and labour participation rates — broken down by state and rural/urban area.

---

## Features

- **Home** — Project summary with key metrics (total records, states, average unemployment rate)
- **Dashboard** — Monthly unemployment trend line chart + Top 10 states bar chart
- **State Analysis** — Per-state unemployment trend and Rural vs Urban comparison
- **COVID Analysis** — Before vs After COVID-19 (March 25, 2020) unemployment comparison
- **Dataset** — Searchable, filterable table with CSV download option

---

## Dataset

**File:** `Unemployment in India.csv`

| Column | Description |
|---|---|
| Region | Indian state / region |
| Date | Month-end date |
| Frequency | Data frequency (Monthly) |
| Estimated Unemployment Rate (%) | Unemployment rate |
| Estimated Employed | Number of employed persons |
| Estimated Labour Participation Rate (%) | Labour participation rate |
| Area | Rural or Urban |

---

## Tech Stack

| Tool | Purpose |
|---|---|
| Python | Core language |
| Pandas | Data loading & processing |
| NumPy | Numerical operations |
| Plotly | Interactive charts |
| Streamlit | Web dashboard |

---

## Project Structure

```
2.Unemployment_Analysis/
├── app.py                        # Streamlit dashboard app
├── Unemployment in India.csv     # Dataset
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

**3. Run the app**
```bash
streamlit run app.py
```

**4. Open in browser**
```
http://localhost:8501
```

---

## Key Insights

- Unemployment rates spiked significantly **after COVID-19 lockdown** (March 2020)
- Urban areas generally show higher unemployment volatility than rural areas
- States like Tripura and Haryana recorded the highest average unemployment rates

---

## Internship

This project was developed as part of the **Oasis Infobyte Data Science Internship**.








