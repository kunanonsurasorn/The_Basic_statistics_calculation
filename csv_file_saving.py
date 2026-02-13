import csv

def save_statistics_csv(csv_filename,result_statistics):
    if not csv_filename.endswith(".csv"):
        csv_filename = csv_filename+".csv"

    with open(csv_filename,mode="w",newline='') as file:
        writer = csv.writer(file)
        writer.writerow(result_statistics.keys())
        writer.writerow(result_statistics.values())