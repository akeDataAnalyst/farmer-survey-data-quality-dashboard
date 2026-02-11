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
