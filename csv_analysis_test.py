
import csv

def analyze_csv(input_file, output_file):
    # Perform your analysis here and write to output_file
    with open(input_file, 'r') as csvfile:
        reader = csv.reader(csvfile)
        # Example analysis: count rows
        row_count = sum(1 for row in reader)
    
    with open(output_file, 'w') as reportfile:
        reportfile.write(f"Row count: {row_count}\n")

    
    analyze_csv(input_file.csv, output_file.csv)