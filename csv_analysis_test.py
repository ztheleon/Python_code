
import csv

# Perform your analysis here and write to output_file
with open('input_file.csv', 'r') as csvfile:
        reader = csv.reader(csvfile)
        # Example analysis: count rows
        row_count = sum(1 for row in reader)        
    
with open('output_file.csv', 'w') as reportfile:
        reportfile.write(f"Row count: {row_count}\n")

   


    