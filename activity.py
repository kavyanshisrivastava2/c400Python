import requests
import csv

print("Starting script...")

# Step 1: Download the CSV file from the given URL
url = 'https://d37ci6vzurychx.cloudfront.net/misc/taxi_zone_lookup.csv'
print(f"Downloading CSV file from {url}...")
response = requests.get(url)

csv_file_path = 'taxi_zone_lookup.csv'
with open(csv_file_path, 'wb') as file:
    file.write(response.content)
print(f"CSV file downloaded and saved as {csv_file_path}.")

total_records = 0
unique_boroughs = set()
brooklyn_count = 0

print("Processing CSV file...")
with open(csv_file_path, 'r') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        total_records += 1
        unique_boroughs.add(row['Borough'])
        if row['Borough'] == 'Brooklyn':
            brooklyn_count += 1

print("CSV file processing complete.")

output = f"""
Total Number of Records: {total_records}
Unique Boroughs (in sorted order): {', '.join(sorted(unique_boroughs))}
Number of Records for Brooklyn Borough: {brooklyn_count}
"""

print("Preparing to save output...")
output_file_path = 'taxi_zone_output.txt'
with open(output_file_path, 'w') as output_file:
    output_file.write(output)
print(f"Output saved to {output_file_path}.")
