Farmer Survey Data Quality & Impact Analysis Dashboard | Python, Pandas, Streamlit, Plotly  
End-to-end data quality and insurance impact analysis pipeline + interactive dashboard for smallholder farmer survey data, simulating operational monitoring for agricultural insurance programs (inspired by Pula’s work in East Africa).  
•	Generated realistic synthetic survey data (1,500 records) mimicking KoBo/SurveyCTO exports with intentional quality issues (missing values, duplicates, outliers, invalid GPS).  
•	Implemented SOP-based quality checks and flagging system; achieved 84.5% clean records and identified regional/agent-level issues (e.g., Eastern region 77% clean, ENUM036 avg 0.31 issues).  
•	Calculated key insurance KPIs: 39.0% coverage rate, 16.8% claim rate, $30,980 total payouts, and flagged high-risk zones (Central region 21.8% claim rate) and agents (e.g., ENUM037 17.4% claim rate).  
•	Built interactive Streamlit dashboard with KPI cards, regional charts, filters (country/region/crop/date/insured status), quality alerts, and CSV export functionality.  
•	Demonstrates full analyst workflow: data generation → quality assurance → KPI reporting → actionable visualization for NGO/insurtech stakeholders.  
•	https://github.com/akeDataAnalyst/farmer-survey-insurance-dashboard

-------------------------------------
# Farmer Survey Data Quality & Impact Analysis Dashboard

## Project Overview

This end-to-end project simulates analysis of mobile-collected farmer survey data for agricultural insurance programs.  
It demonstrates the full data analyst workflow: synthetic data generation, quality assurance, KPI calculation, and interactive visualization.

**Business Problem**  
Agricultural insurance relies on high-quality field survey data, but programs face:  
- Missing, duplicate, inconsistent, or outlier records  
- Poor visibility into coverage, claims, payouts, and regional risks  
- Slow manual reporting for managers and donors  

**Solution**  
A Python-based pipeline + interactive Streamlit dashboard to:  
- Clean and validate data following SOPs  
- Compute insurance & impact KPIs  
- Visualize regional risks, agent performance, and data quality issues  
- Enable filtered exploration and export for operational decisions

**Key Outcomes**  
- Overall data quality: **84.5% clean records**  
- Insurance coverage: **39.0%**  
- Claim rate among insured: **16.8%**  
- Total payouts: **$30,979.56**  
- Actionable insights: high-claim regions (Central) and agents (e.g., ENUM037 at 17.39% claim rate)

## Tech Stack

- **Language**: Python  
- **Core Libraries**: pandas, numpy, matplotlib, seaborn, plotly  
- **Dashboard**: Streamlit  
- **Environment**: Jupyter Notebook + Python script (app.py)  
- **Data**: Synthetic but realistic CSV mimicking KoBoToolbox / SurveyCTO exports
