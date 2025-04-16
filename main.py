import os
import pandas as pd

def aggregate_and_export_monthly(folder_path, output_excel="monthly_summary.xlsx"):
    all_files = [f for f in os.listdir(folder_path) if f.endswith('.csv')]
    summary_rows = []

    for file in all_files:
        file_path = os.path.join(folder_path, file)
        df = pd.read_csv(file_path)

        # Parse Begin Date
        df['Begin Date'] = pd.to_datetime(df['Begin Date'])

        # Get date range
        min_date = df['Begin Date'].min()
        max_date = df['Begin Date'].max()

        # Extract Year-Month for grouping
        df['YearMonth'] = df['Begin Date'].dt.to_period('M')

        # Sum numeric columns by YearMonth
        numeric_cols = df.select_dtypes(include='number').columns
        grouped = df.groupby('YearMonth')[numeric_cols].sum().reset_index()

        # Extract dataset and region from filename
        base_name = os.path.splitext(file)[0]
        parts = base_name.split('_')
        dataset = parts[0] if len(parts) > 0 else "unknown"
        region = parts[1] if len(parts) > 1 else "unknown"

        # Add metadata
        grouped['dataset'] = dataset
        grouped['region'] = region
        grouped['month'] = grouped['YearMonth'].dt.strftime('%b-%Y').str.upper()
        grouped['date_range_start'] = min_date.date()
        grouped['date_range_end'] = max_date.date()

        summary_rows.append(grouped)

    # Combine all monthly summaries
    final_df = pd.concat(summary_rows, ignore_index=True)

    # Reorder columns: metadata first
    meta_cols = ['dataset', 'region', 'month', 'date_range_start', 'date_range_end']
    final_df = final_df[meta_cols + [col for col in final_df.columns if col not in meta_cols + ['YearMonth']]]

    # Export to Excel
    output_path = os.path.join(folder_path, output_excel)
    final_df.to_excel(output_path, index=False)
    print(f"📊 Monthly aggregation complete. Excel file saved at: {output_path}")

# Example usage:
# aggregate_and_export_monthly("/your/folder/path")
