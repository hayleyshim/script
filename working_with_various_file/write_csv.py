import csv

write_csv = [['name', 'lastname',],['yh','shim']]
with open('data.csv' ,'w') as csvFile:
    writer = csv.writer(csvFile)
    writer.writerow(write_csv)
    print(write_csv)