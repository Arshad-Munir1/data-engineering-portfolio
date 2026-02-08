# Week 01 — Retail Sales ETL Pipeline

## Project Goal

Build a simple ETL pipeline using Python and Pandas to clean raw retail sales data and prepare it for analytics.

## Tools Used

- Python
- Pandas
- CSV Dataset

## Pipeline Steps

1. Extract raw CSV file
2. Clean missing values
3. Standardise column names
4. Create revenue metric
5. Export cleaned dataset

## Status

🚧 In Progress

### Day 1: Python Fundamentals
- Refreshed Python basics: variables, lists, dictionaries
- Built small scripts to calculate sales metrics
- Prepared environment for ETL projects

### Day 2 — Data Ingestion with Pandas

Objective: Load and explore a real retail dataset.

What I did:

Loaded Superstore CSV dataset using Pandas

Handled encoding issues during ingestion

Explored dataset structure using head(), info(), and describe()

Identified data types and columns for transformation stage

Skills Practiced:

Pandas DataFrames

CSV ingestion

Encoding handling

Data profiling

## Day 3 - ETL Transform Layer
Cleaned and standardized column names
Converted `order_date` and `ship_date` to datetime
Created `profit_margin` metric
Rounded numeric financial columns
Saved cleaned dataset for downstream use

## Day 4 - Aggregation & Analytics Layer
- Aggregated sales and profit by region
- Generated category-level performance summaries
- Created monthly sales and profit trends
- Validated data and sanity-checked outputs in Excel

- Learned to turn raw rows into business-ready insights
- Practiced idempotent pipeline patterns
- Understood the importance of data validation