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

## Day 5 - Data Quality & Validation

Loaded aggregated outputs from the analytics layer
Performed data quality checks using Pandas:
Missing value detection
Duplicate record checks
Data type validation
Validated aggregated results against business expectations
Generated a validation CSV to support repeatable quality checks
Used terminal-based inspection to confirm pipeline correctness
Learned the importance of validating data before trusting outputs
Understood why validation should be a separate pipeline stage
Built confidence in the reliability of aggregated datasets

## Day 6 - Assertion-Based Data Quality Enforcement

Upgraded validation logic to include assertion-based checks

Implemented hard stops to prevent the pipeline from continuing when data quality issues are detected

Added automated checks for:

Missing values

Duplicate records

Invalid numeric values

Generated a validation CSV report to create an audit trail of data quality results

Ensured the pipeline fails loudly instead of silently when assumptions are violated

Learned the difference between validating data and enforcing data quality

Practiced defensive programming principles in data pipelines

Understood how assertions improve reliability and trust in automated workflows

## Day 7 — Data Validation Logging & Error Handling
## Part 1 - Pipeline Logging Setup

Today focused on making the data pipeline more production-ready by introducing structured logging.

What I implemented:

Added Python logging module to track pipeline activity

Configured log file output (pipeline.log)

Created automatic log directory using os.makedirs

Logged key pipeline events such as:

Start of validation process

File loading status

Dataset validation results

Error messages

Key Learning:

Instead of relying on terminal prints, real data pipelines use persistent log files so engineers can monitor, debug, and audit pipeline runs.

## Part 2 — Error Handling & Robust File Loading

This step focused on making the pipeline resilient to failures.

What I implemented:

Wrapped data loading inside try/except blocks

Handled common pipeline errors:

Missing file paths

Unexpected runtime exceptions

Logged failures clearly instead of crashing silently

Ensured pipeline continues safely even if an error occurs
