import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import os


# PAGE CONFIGURATION
st.set_page_config(page_title="Unemployment Analysis Dashboard", page_icon=" ", layout="wide")


# BACKGROUND IMAGE
def set_background(image_path):
    if os.path.exists(image_path):
        import base64
        with open(image_path, "rb") as image:
            encoded = base64.b64encode(image.read()).decode()
        st.markdown(
            f"""
            <style>
            .stApp {{
                background-image: url("data:image/jpg;base64,{encoded}");
                background-size: cover;
                background-position: center;
                background-attachment: fixed;
            }}

            [data-testid="stHeader"] {{
                background-color: rgba(0,0,0,0);
            }}

            .block-container {{
                background-color: rgba(255,255,255,0.88);
                padding: 2rem;
                border-radius: 12px;
            }}
            </style>
            """,
            unsafe_allow_html=True
        )
set_background("images/background.jpg")


# CUSTOM CSS
st.markdown(
    """
    <style>
    h1, h2, h3 {
        color: #17365D;
    }
    .stMetric {
        background-color: white;
        padding: 15px;
        border-radius: 10px;
        border: 1px solid #dddddd;
    }
    </style>
    """,
    unsafe_allow_html=True
)


# DATA LOADING AND CLEANING
@st.cache_data
def load_data():
    file_path = "Unemployment in India.csv"
    if not os.path.exists(file_path):
        return None
    data = pd.read_csv(file_path)

    # Clean column names
    data.columns = data.columns.str.strip()

    # Clean text columns
    for col in ["Region", "Area", "Frequency"]:
        if col in data.columns:
            data[col] = data[col].astype("string").str.strip()

    # Date conversion
    data["Date"] = pd.to_datetime(data["Date"], dayfirst=True, errors="coerce")

    # Numeric conversion
    numeric_columns = ["Estimated Unemployment Rate (%)", "Estimated Employed", "Estimated Labour Participation Rate (%)"]
    for col in numeric_columns:
        data[col] = pd.to_numeric(data[col], errors="coerce")

    # Remove missing important values
    required_columns = ["Region", "Date", "Estimated Unemployment Rate (%)", "Estimated Employed", "Estimated Labour Participation Rate (%)"]
    data = data.dropna(subset=required_columns)

    # Remove duplicate rows
    data = data.drop_duplicates()

    # Add month column
    data["Month"] = data["Date"].dt.to_period("M").astype(str)
    return data.reset_index(drop=True)
df = load_data()

if df is None:
    st.error("Dataset not found! Keep 'Unemployment in India.csv' in the same folder as app.py.")
    st.stop()

if df.empty:
    st.error("No valid records found in the dataset.")
    st.stop()


# SIDEBAR NAVIGATION
st.sidebar.title("Unemployment Analysis")
st.sidebar.write("India Unemployment Data Analysis")
page = st.sidebar.radio("Navigation", ["Home", "Dashboard", "State Analysis", "COVID Analysis", "Dataset"])
st.sidebar.markdown("---")
st.sidebar.info("Oasis Infobyte Internship - Task 2")


# HOME PAGE
if page == "Home":
    st.title("Unemployment Analysis in India")
    st.subheader("Data Analysis and Visualization Dashboard")
    st.write(
        """
        This project analyzes unemployment trends across
        different regions of India using Python.
        The dashboard provides insights into unemployment
        rates, employment estimates, labour participation,
        regional differences and COVID-period comparisons.
        """
    )

    st.markdown("---")
    col1, col2, col3 = st.columns(3)
    col1.metric("Total Records", f"{len(df):,}")
    col2.metric("Total Regions", df["Region"].nunique())
    col3.metric("Average Unemployment", f"{df['Estimated Unemployment Rate (%)'].mean():.2f}%")
    st.markdown("---")
    st.subheader("Project Objectives")
    st.markdown(
        """
        - Analyze unemployment rates across Indian regions.
        - Understand monthly unemployment trends.
        - Compare unemployment in major states.
        - Identify regions with high unemployment.
        - Study relationships between numerical variables.
        - Compare pre-COVID and post-COVID unemployment.
        """
    )
    st.subheader("Dataset Preview")
    st.dataframe(df.head(10), use_container_width=True)


# DASHBOARD PAGE
elif page == "Dashboard":
    st.title("Unemployment Dashboard")

    # KPI Metrics
    col1, col2, col3, col4 = st.columns(4)
    avg_unemployment = df["Estimated Unemployment Rate (%)"].mean()
    total_employed = df["Estimated Employed"].mean()
    avg_participation = df["Estimated Labour Participation Rate (%)"].mean()
    col1.metric("Average Unemployment", f"{avg_unemployment:.2f}%")
    col2.metric("Average Estimated Employed", f"{total_employed:,.0f}")
    col3.metric("Labour Participation", f"{avg_participation:.2f}%")
    col4.metric("Total Regions", df["Region"].nunique())
    st.markdown("---")


    # MONTHLY TREND
    st.subheader("Monthly Unemployment Trend")
    monthly_data = (df.groupby("Month")["Estimated Unemployment Rate (%)"].mean().reset_index())
    monthly_data["Month"] = pd.to_datetime(monthly_data["Month"])
    fig_monthly = px.line(monthly_data, x="Month", y="Estimated Unemployment Rate (%)", markers=True, title="Monthly Average Unemployment Rate", labels={"Month": "Month", "Estimated Unemployment Rate (%)": "Unemployment Rate (%)"})
    st.plotly_chart(fig_monthly, use_container_width=True)


    # TOP 10 REGIONS
    st.subheader("Top 10 Regions by Unemployment Rate")
    top_10 = (df.groupby("Region")["Estimated Unemployment Rate (%)"].mean().sort_values(ascending=False).head(10).reset_index())
    fig_top10 = px.bar(top_10, x="Estimated Unemployment Rate (%)", y="Region", orientation="h", color="Estimated Unemployment Rate (%)", color_continuous_scale="Reds", title="Top 10 Regions with Highest Average Unemployment")
    fig_top10.update_layout(yaxis={"categoryorder": "total ascending"})
    st.plotly_chart(fig_top10, use_container_width=True)


    # THREE-STATE COMBINED CHART
    st.subheader("Three-State Combined Comparison")
    major_states = ["Maharashtra", "Uttar Pradesh", "Karnataka"]
    state_data = df[df["Region"].isin(major_states)].copy()
    available_states = state_data["Region"].unique()

    if len(available_states) > 0:
        three_state_data = (state_data.groupby(["Date", "Region"])["Estimated Unemployment Rate (%)"].mean().reset_index())
        fig_states = px.line(
            three_state_data,
            x="Date",
            y="Estimated Unemployment Rate (%)",
            color="Region",
            markers=True,
            title="Maharashtra vs Uttar Pradesh vs Karnataka",
            labels={"Date": "Date", "Estimated Unemployment Rate (%)": "Unemployment Rate (%)", "Region": "State"}
        )
        fig_states.update_layout(hovermode="x unified")
        st.plotly_chart(fig_states, use_container_width=True)
        if len(available_states) < 3:
            st.warning("Some selected states are not available in the dataset.")
    else:
        st.warning("Maharashtra, Uttar Pradesh and Karnataka data not found in the dataset.")


    # CORRELATION HEATMAP
    st.subheader("Correlation Heatmap")
    correlation_columns = ["Estimated Unemployment Rate (%)", "Estimated Employed", "Estimated Labour Participation Rate (%)"]
    correlation_data = df[correlation_columns].apply(pd.to_numeric, errors="coerce")
    correlation_matrix = correlation_data.corr()
    fig_heatmap = px.imshow(correlation_matrix, text_auto=".2f", color_continuous_scale="RdBu_r", aspect="auto", title="Correlation Between Unemployment, Employment and Labour Participation")
    st.plotly_chart(fig_heatmap, use_container_width=True)
    st.caption("Estimated Employed represents employment count, not employment rate. Correlation does not imply causation.")


# STATE ANALYSIS PAGE
elif page == "State Analysis":
    st.title("State-wise Analysis")
    states = sorted(df["Region"].dropna().unique().tolist())
    selected_state = st.selectbox("Select a State", states)
    state_df = df[df["Region"] == selected_state].copy()
    st.subheader(f"Unemployment Analysis: {selected_state}")

    col1, col2 = st.columns(2)
    col1.metric("Average Unemployment Rate", f"{state_df['Estimated Unemployment Rate (%)'].mean():.2f}%")
    col2.metric("Average Estimated Employed", f"{state_df['Estimated Employed'].mean():,.0f}")

    # State trend
    state_trend = (state_df.groupby("Date")["Estimated Unemployment Rate (%)"].mean().reset_index())
    fig_state = px.line(state_trend, x="Date", y="Estimated Unemployment Rate (%)", markers=True, title=f"Unemployment Trend - {selected_state}")
    st.plotly_chart(fig_state, use_container_width=True)

    # Rural vs Urban
    if "Area" in state_df.columns:
        st.subheader("Rural vs Urban Comparison")
        area_data = (state_df.groupby("Area")["Estimated Unemployment Rate (%)"].mean().reset_index())
        fig_area = px.bar(area_data, x="Area", y="Estimated Unemployment Rate (%)", color="Area", title="Average Unemployment Rate: Rural vs Urban")
        st.plotly_chart(fig_area, use_container_width=True)
    st.subheader("State Dataset")
    st.dataframe(state_df, use_container_width=True)


# COVID ANALYSIS PAGE
elif page == "COVID Analysis":
    st.title("Pre-COVID vs Post-COVID Analysis")
    COVID_DATE = pd.Timestamp("2020-03-01")
    pre_covid = df[df["Date"] < COVID_DATE]
    post_covid = df[df["Date"] >= COVID_DATE]
    pre_avg = pre_covid["Estimated Unemployment Rate (%)"].mean()
    post_avg = post_covid["Estimated Unemployment Rate (%)"].mean()
    difference = post_avg - pre_avg
    st.info(f"Comparison cutoff date: {COVID_DATE.date()}")

    col1, col2, col3 = st.columns(3)
    col1.metric("Pre-COVID Average", f"{pre_avg:.2f}%" if pd.notna(pre_avg) else "N/A")
    col2.metric("Post-COVID Average", f"{post_avg:.2f}%" if pd.notna(post_avg) else "N/A")
    col3.metric("Difference", f"{difference:.2f} pp" if pd.notna(difference) else "N/A")

    comparison = pd.DataFrame({"Period": ["Pre-COVID", "Post-COVID"], "Average Unemployment Rate": [pre_avg, post_avg]})
    fig_covid = px.bar(comparison, x="Period", y="Average Unemployment Rate", color="Period", title="Pre-COVID vs Post-COVID Unemployment Rate", text_auto=".2f")
    st.plotly_chart(fig_covid, use_container_width=True)
    st.subheader("COVID Period Observations")
    if pd.notna(pre_avg) and pd.notna(post_avg):

        if difference > 0:
            st.write(
                f"The average unemployment rate increased "
                f"by {difference:.2f} percentage points "
                f"in the post-COVID period."
            )

        elif difference < 0:
            st.write(
                f"The average unemployment rate decreased "
                f"by {abs(difference):.2f} percentage points "
                f"in the post-COVID period."
            )
        else:
            st.write("The average unemployment rate remained the same.")
    st.caption("This comparison describes the available dataset. It does not establish that COVID-19 alone caused the observed changes.")


# DATASET PAGE
elif page == "Dataset":
    st.title("Unemployment Dataset")
    st.write("Explore, filter and download the unemployment dataset.")
    search_region = st.selectbox("Filter by Region", ["All"] + sorted( df["Region"].dropna().unique().tolist()))

    if search_region != "All":
        display_df = df[df["Region"] == search_region]
    else:
        display_df = df.copy()

    st.subheader("Dataset Preview")
    st.dataframe(display_df, use_container_width=True)
    st.markdown("---")
    col1, col2 = st.columns(2)
    col1.metric("Rows", len(display_df))
    col2.metric("Columns", len(display_df.columns))

    # Download filtered dataset
    csv_data = display_df.to_csv(index=False).encode("utf-8")
    st.download_button(label="Download Dataset as CSV", data=csv_data, file_name="cleaned_unemployment_data.csv", mime="text/csv")
    st.markdown("---")

    st.subheader("Dataset Information")

    st.write("Column Names:")
    st.write(df.columns.tolist())

    st.write("Missing Values:")
    st.dataframe(df.isnull().sum().rename("Missing Values"))

    st.write("Statistical Summary:")
    st.dataframe(df.describe(include="all"), use_container_width=True)


# FOOTER
st.markdown("---")
st.markdown(
    """
    <div style="text-align:center;">
        <p><b>Unemployment Analysis in India</b></p>
        <p>Developed using Python, Streamlit, Pandas and Plotly</p>
        <p>Oasis Infobyte Internship - Task 2</p>
    </div>
    """,
    unsafe_allow_html=True
)
