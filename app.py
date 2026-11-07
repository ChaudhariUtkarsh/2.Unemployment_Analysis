import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import base64
import os

# PAGE CONFIGURATION
st.set_page_config(page_title="Unemployment Analysis", page_icon="📊", layout="wide")

# BACKGROUND IMAGE + WHITE TEXT THEME
def set_background(image_file):
    if not os.path.exists(image_file):
        st.error("Background image not found: " + image_file)
        return
    with open(image_file, "rb") as file:
        encoded = base64.b64encode(file.read()).decode()
    st.markdown(
        f"""
        <style>

        .stApp {{
            background-image:
                linear-gradient(
                    rgba(3, 12, 30, 0.48),
                    rgba(3, 12, 30, 0.48)
                ),
                url("data:image/jpeg;base64,{encoded}");

            background-size: cover;
            background-position: center;
            background-repeat: no-repeat;
            background-attachment: fixed;
        }}

        .stApp h1,
        .stApp h2,
        .stApp h3,
        .stApp h4,
        .stApp p,
        .stApp label,
        .stApp li,
        .stApp span {{
            color: #FFFFFF !important;
        }}

        [data-testid="stHeader"] {{
            background: rgba(0,0,0,0);
        }}

        [data-testid="stSidebar"] {{
            background-color: rgba(3, 15, 38, 0.95);
            border-right: 1px solid #00D9FF;
        }}

        [data-testid="stSidebar"] * {{
            color: #FFFFFF !important;
        }}

        [data-testid="stMetric"] {{
            background-color: rgba(5, 30, 65, 0.82);
            padding: 20px;
            border-radius: 14px;
            border: 1px solid rgba(0, 217, 255, 0.5);
        }}

        [data-testid="stMetricValue"] {{
            color: #00E5FF !important;
            font-weight: bold;
        }}

        [data-testid="stMetricLabel"] {{
            color: #FFFFFF !important;
        }}

        .stButton button,
        .stDownloadButton button {{
            background-color: #0077B6;
            color: white !important;
            border: 1px solid #00D9FF;
            border-radius: 8px;
        }}

        .stButton button p,
        .stDownloadButton button p {{
            color: white !important;
        }}

        .stButton button:hover,
        .stDownloadButton button:hover {{
            background-color: #005F8D;
            border-color: #FFFFFF;
        }}

        .stTextInput input {{
            background-color: rgba(255,255,255,0.95);
            color: #000000 !important;
        }}

        div[data-baseweb="select"] {{
            background-color: white;
            border-radius: 8px;
        }}

        div[data-baseweb="select"] * {{
            color: #000000 !important;
        }}

        hr {{
            border-color: rgba(0,217,255,0.5);
        }}

        </style>
        """,
        unsafe_allow_html=True
    )

set_background("images/background.jpg")

# LOAD DATASET
@st.cache_data
def load_data():
    possible_files = ["Unemployment in India.csv", "Unemployment_in_India.csv"]
    file_path = None
    for file in possible_files:
        if os.path.exists(file):
            file_path = file
            break
    if file_path is None:
        return None
    df = pd.read_csv(file_path)
    df.columns = df.columns.str.strip()

    if "Date" in df.columns:
        df["Date"] = pd.to_datetime(df["Date"], errors="coerce", dayfirst=True)
    numeric_columns = ["Estimated Unemployment Rate (%)", "Estimated Employed", "Estimated Labour Participation Rate (%)"]

    for col in numeric_columns:
        if col in df.columns:
            df[col] = pd.to_numeric(df[col], errors="coerce")
    if "Region" in df.columns:
        df["Region"] = df["Region"].astype(str).str.strip()
    if "Area" in df.columns:
        df["Area"] = df["Area"].astype(str).str.strip()
    df = df.drop_duplicates()
    return df

df = load_data()

if df is None:
    st.error("Dataset not found! Keep your CSV file in the same folder as app.py.")
    st.stop()

# CHECK REQUIRED COLUMN
rate_column = "Estimated Unemployment Rate (%)"
if rate_column not in df.columns:
    st.error("Unemployment rate column is missing from the dataset.")
    st.stop()

# SIDEBAR NAVIGATION
st.sidebar.title("Unemployment Analysis")
st.sidebar.markdown("---")
page = st.sidebar.radio("Navigation", ["Home", "Dashboard", "State Analysis", "COVID Analysis", "Dataset"])
st.sidebar.markdown("---")
st.sidebar.info("Python Data Science Project")


# PLOTLY THEME FUNCTION
def apply_chart_theme(fig):
    fig.update_layout(
        template="plotly_dark",
        paper_bgcolor="rgba(3, 12, 30, 0.65)",
        plot_bgcolor="rgba(3, 12, 30, 0.45)",
        font=dict(color="white"),
        title_font=dict(color="#00E5FF"),
        legend=dict(font=dict(color="white"))
    )
    return fig


# HOME PAGE
if page == "Home":
    st.title("Unemployment Analysis in India")
    st.subheader("Welcome to Unemployment Analysis Dashboard")
    st.write("""This project analyzes unemployment trends in India using Python, Pandas, NumPy, Plotly and Streamlit.""")
    st.markdown("---")
    st.markdown("### Project Objectives")
    st.markdown(
        """
        - Analyze unemployment rates across Indian states.
        - Understand employment trends.
        - Compare rural and urban unemployment.
        - Study the impact of COVID-19.
        - Visualize important unemployment statistics.
        """
    )
    st.markdown("---")

    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric("Total Records", f"{len(df):,}")
    with col2:
        if "Region" in df.columns:
            st.metric("Total States / Regions", df["Region"].nunique())
    with col3:
        average = df[rate_column].mean()
        st.metric("Average Unemployment", f"{average:.2f}%")


# DASHBOARD PAGE
elif page == "Dashboard":
    st.title("Unemployment Dashboard")
    avg_rate = df[rate_column].mean()
    max_rate = df[rate_column].max()
    min_rate = df[rate_column].min()

    col1, col2, col3 = st.columns(3)
    col1.metric("Average Unemployment", f"{avg_rate:.2f}%")
    col2.metric("Maximum Unemployment", f"{max_rate:.2f}%")
    col3.metric("Minimum Unemployment", f"{min_rate:.2f}%")
    st.markdown("---")

    # Monthly Trend
    if "Date" in df.columns:
        monthly_data = (df.dropna(subset=["Date"]).set_index("Date").resample("ME")[rate_column].mean().reset_index())
        fig = px.line(
            monthly_data,
            x="Date",
            y=rate_column,
            title="Monthly Unemployment Rate Trend",
            markers=True,
            color_discrete_sequence=["#00E5FF"]
        )
        apply_chart_theme(fig)
        st.plotly_chart(fig, use_container_width=True)

    # State-wise Analysis
    if "Region" in df.columns:
        state_data = (df.groupby("Region")[rate_column].mean().reset_index().sort_values(by=rate_column, ascending=False).head(10))
        fig = px.bar(
            state_data,
            x="Region",
            y=rate_column,
            title="Top 10 Regions by Average Unemployment Rate",
            color=rate_column,
            color_continuous_scale="Blues"
        )
        apply_chart_theme(fig)
        st.plotly_chart(fig, use_container_width=True)


# STATE ANALYSIS PAGE
elif page == "State Analysis":
    st.title("State-wise Unemployment Analysis")
    if "Region" not in df.columns:
        st.error("Region column is missing.")
        st.stop()
    selected_region = st.selectbox("Select State / Region", sorted(df["Region"].dropna().unique()))
    state_data = df[df["Region"] == selected_region].copy()
    st.subheader(f"Analysis for {selected_region}")

    if "Date" in state_data.columns:
        state_data = state_data.sort_values("Date")
        fig = px.line(
            state_data,
            x="Date",
            y=rate_column,
            title=f"Unemployment Trend - {selected_region}",
            markers=True,
            color_discrete_sequence=["#00E5FF"]
        )
        apply_chart_theme(fig)
        st.plotly_chart(fig, use_container_width=True)

    # Rural vs Urban Analysis
    if "Area" in state_data.columns:
        area_data = (state_data.groupby("Area")[rate_column].mean().reset_index())
        fig = px.bar(
            area_data,
            x="Area",
            y=rate_column,
            color="Area",
            title="Rural vs Urban Unemployment",
            color_discrete_sequence=[
                "#00D9FF",
                "#0077B6"
            ]
        )
        apply_chart_theme(fig)
        st.plotly_chart(fig, use_container_width=True)
    st.subheader("State Dataset")
    st.dataframe(state_data, use_container_width=True)


# COVID ANALYSIS PAGE
elif page == "COVID Analysis":
    st.title("COVID-19 Impact on Unemployment")
    if "Date" not in df.columns:
        st.error("Date column is missing.")
        st.stop()
    covid_date = pd.Timestamp("2020-03-25")
    covid_data = df.dropna(subset=["Date"]).copy()
    covid_data["Period"] = np.where(covid_data["Date"] < covid_date, "Before COVID", "After COVID")
    comparison = (covid_data.groupby("Period")[rate_column].mean().reset_index())
    fig = px.bar(
        comparison,
        x="Period",
        y=rate_column,
        color="Period",
        title="Before vs After COVID-19 Unemployment",
        color_discrete_sequence=[
            "#00D9FF",
            "#0077B6"
        ]
    )
    apply_chart_theme(fig)
    st.plotly_chart(fig, use_container_width=True)
    st.subheader("COVID-19 Comparison")
    st.dataframe(comparison, use_container_width=True)


# DATASET PAGE
elif page == "Dataset":
    st.title("Unemployment Dataset")
    st.write("Explore and download the complete dataset.")
    search = st.text_input("Search by State / Region")
    display_df = df.copy()

    if search and "Region" in display_df.columns:
        display_df = display_df[display_df["Region"].str.contains(search, case=False, na=False)]
    st.dataframe(display_df, use_container_width=True, height=450)
    csv = display_df.to_csv(index=False).encode("utf-8")
    st.download_button(label="Download Dataset", data=csv, file_name="unemployment_analysis.csv", mime="text/csv")


# FOOTER
st.markdown("---")
st.markdown(
    """
    <div style="text-align:center; padding:10px;">
        <p>Unemployment Analysis with Python</p>
        <p>Developed using Python, Pandas, NumPy, Plotly and Streamlit</p>
    </div>
    """,
    unsafe_allow_html=True
)
