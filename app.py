import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

# Page config
st.set_page_config(
    page_title="Farmer Survey & Insurance Impact Dashboard",
    page_icon="🌾",
    layout="wide"
)

# Title & Intro
st.title("🌾 Farmer Survey Data Quality & Insurance Impact Dashboard")
st.markdown("""
This interactive dashboard analyzes smallholder farmer survey data from East/Southern Africa (Ethiopia, Kenya, Zambia focus).  
It highlights insurance coverage, claim payouts, regional risks, and data quality issues.

Use filters in the sidebar to explore. Data is synthetic but realistic for portfolio demonstration.
""")

# Load data (cache for performance)
@st.cache_data
def load_data():
    df = pd.read_csv('farmer_survey_cleaned_2026.csv', parse_dates=['survey_date'])
    regional = pd.read_csv('regional_kpis.csv')
    agent = pd.read_csv('agent_kpis.csv')
    return df, regional, agent

df, regional_kpis, agent_kpis = load_data()

# Sidebar Filters
st.sidebar.header("Filters")

# Country & Region (cascading)
countries = sorted(df['country'].unique())
selected_countries = st.sidebar.multiselect("Country", countries, default=countries)

filtered_df = df[df['country'].isin(selected_countries)]

regions = sorted(filtered_df['region'].unique())
selected_regions = st.sidebar.multiselect("Region", regions, default=regions)

filtered_df = filtered_df[filtered_df['region'].isin(selected_regions)]

# Crop
crops = sorted(filtered_df['crop'].unique())
selected_crops = st.sidebar.multiselect("Crop", crops, default=crops)
filtered_df = filtered_df[filtered_df['crop'].isin(selected_crops)]

# Date range
min_date = filtered_df['survey_date'].min().date()
max_date = filtered_df['survey_date'].max().date()
date_range = st.sidebar.date_input("Survey Date Range", (min_date, max_date), min_value=min_date, max_value=max_date)

if len(date_range) == 2:
    start_date, end_date = date_range
    filtered_df = filtered_df[(filtered_df['survey_date'].dt.date >= start_date) & 
                              (filtered_df['survey_date'].dt.date <= end_date)]

# Insured status
insured_options = ['All', 'Yes', 'No']
selected_insured = st.sidebar.selectbox("Insurance Status", insured_options)
if selected_insured != 'All':
    filtered_df = filtered_df[filtered_df['insured'] == selected_insured]

# Apply filters count
st.sidebar.markdown(f"**Filtered Records:** {len(filtered_df)}")

# KPI Cards (Top Row)
st.header("Key Performance Indicators")

col1, col2, col3, col4 = st.columns(4)

total_farmers = filtered_df['farmer_id'].nunique()
insured_count = filtered_df[filtered_df['insured'] == 'Yes']['farmer_id'].nunique()
coverage_rate = (insured_count / total_farmers * 100) if total_farmers > 0 else 0
total_payout = filtered_df['payout_amount_usd'].sum()

col1.metric("Total Unique Farmers", f"{total_farmers:,}")
col2.metric("Insured Farmers", f"{insured_count:,}", delta=f"{coverage_rate:.1f}% coverage")
col3.metric("Total Payout (USD)", f"${total_payout:,.2f}")
col4.metric("Avg Payout per Claim (USD)", 
            f"${filtered_df[filtered_df['claim_triggered'] == 'Yes']['payout_amount_usd'].mean():,.2f}" 
            if filtered_df['claim_triggered'].eq('Yes').any() else "$0.00")

# Regional Charts
st.header("Regional Insights")

if not filtered_df.empty:
    # Coverage & Claim Rate Bar + Line
    fig_region = go.Figure()

    fig_region.add_trace(go.Bar(
        x=regional_kpis['region'],
        y=regional_kpis['coverage_rate'],
        name='Coverage Rate (%)',
        marker_color='skyblue'
    ))

    fig_region.add_trace(go.Scatter(
        x=regional_kpis['region'],
        y=regional_kpis['claim_rate'],
        name='Claim Rate (%)',
        yaxis='y2',
        line=dict(color='red', width=3),
        mode='lines+markers'
    ))

    fig_region.update_layout(
        title='Insurance Coverage vs Claim Rate by Region',
        xaxis_title='Region',
        yaxis_title='Coverage Rate (%)',
        yaxis2=dict(title='Claim Rate (%)', overlaying='y', side='right'),
        legend=dict(x=0.01, y=0.99),
        barmode='group'
    )

    st.plotly_chart(fig_region, use_container_width=True)

    # Total Payout Bar
    fig_payout = px.bar(regional_kpis, x='region', y='total_payout',
                        title='Total Payout by Region (USD)',
                        labels={'total_payout': 'Total Payout (USD)', 'region': 'Region'},
                        color='total_payout', color_continuous_scale='Viridis')
    st.plotly_chart(fig_payout, use_container_width=True)

else:
    st.warning("No data after applying filters. Try adjusting selections.")

# Data Quality Alert Section
st.header("Data Quality Alerts")
if 'total_issues' in df.columns:
    high_issue_regions = df[df['total_issues'] > 2]['region'].value_counts().head(5)
    if not high_issue_regions.empty:
        st.warning(f"**High Issue Regions (avg >2 issues/record):** {high_issue_regions.to_dict()}")
    else:
        st.success("Data quality looks good across filtered records!")

# Agent Performance Table (Top 10)
st.header("Field Agent Performance (Top 10 by Farmers Surveyed)")
st.dataframe(agent_kpis.head(10).style.format({
    'insured_pct': '{:.1f}%',
    'claim_pct': '{:.1f}%'
}))

# Download Buttons
st.header("Export Data")
col_download1, col_download2 = st.columns(2)

csv_clean = filtered_df.to_csv(index=False).encode('utf-8')
col_download1.download_button(
    label="Download Filtered Cleaned Data (CSV)",
    data=csv_clean,
    file_name="filtered_farmer_survey.csv",
    mime="text/csv"
)

csv_regional = regional_kpis.to_csv(index=False).encode('utf-8')
col_download2.download_button(
    label="Download Regional KPIs (CSV)",
    data=csv_regional,
    file_name="regional_kpis.csv",
    mime="text/csv"
)

# Footer / Portfolio Note
st.markdown("---")
st.caption("""
**Developed by Aklilu Abera** | Inspired by agricultural insurance challenges in Africa  
Demonstrates: Data cleaning (SOPs), quality scoring, KPI calculation, interactive visualization, and actionable insights.""")


# In[ ]:




