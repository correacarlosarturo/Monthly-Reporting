# 📊 Monthly CSV Aggregator

This Python script processes a folder of daily `.csv` files, each named with a region-specific convention (e.g., `Data1_EUROPE.csv`, `Data2_AMER.csv`, etc.). It aggregates all numeric data for the **month**, extracts metadata (dataset, region, date range), and exports the result to a clean Excel file.

---

## 🔧 Features

- Parses and groups data by **month** (`APR-2025`, `MAY-2025`, etc.)
- Aggregates all **numeric values**
- Extracts **dataset** and **region** from file names
- Includes **start and end dates** of the data
- Outputs a single `.xlsx` file with one row per file

---

## 📁 Input File Naming Convention

Each input file should follow this format:

DataX_REGION.csv

Examples:
- `Data1_EUROPE.csv`
- `Data2_AMER.csv`
- `Data3_BR.csv`

---

## 📄 Input CSV Requirements

Each CSV should contain a `"Begin Date"` column in a format recognizable by `pandas.to_datetime()`. Example structure:

| Begin Date | End Date | Stopped by | Clean Messages | Total Threats |
|------------|----------|-------------|----------------|----------------|
| 2025-04-06 | 2025-04-07 | 234         | 29343          | 211            |

---

## 📤 Output

An Excel file named `monthly_summary.xlsx` with:

| dataset | region | month    | date_range_start | date_range_end | ...numeric sums... |
|---------|--------|----------|------------------|----------------|---------------------|
| Data1   | EUROPE | APR-2025 | 2025-04-06       | 2025-04-13     | ...                 |

---

## 🚀 Usage

### Step 1: Install dependencies (if needed)
```bash
pip install pandas openpyxl
Step 2: Run the script
Update the folder path in the script, or call it like:
```
Step 2: Run the script
Update the folder path in the script, or call it like:
```zsh
aggregate_and_export_monthly("/path/to/your/folder")
```

## 🧠 Notes
The script handles one month per file. If you need to handle multiple months per file, it can be extended easily.

Missing or malformed files will be skipped — make sure naming and formats are consistent.

## 🛠️ TODO / Nice-to-Haves
- Add CLI support
- Add log file / error handling
- Excel styling and chart summary
