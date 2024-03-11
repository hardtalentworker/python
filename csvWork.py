import csv
import collections

with open("KD_csv.csv",encoding="utf-8") as f:
	lines_csv=csv.reader(f,delimiter=";")
	headers=next(lines_csv)
	for row in lines_csv:
		print(row[0])
		break

print("="*80)

with open("KD_csv.csv",encoding="utf-8") as f:
	lines_csv=csv.reader(f,delimiter=";")
	headers=next(lines_csv)
	row_all=collections.namedtuple('Row',headers)
	for r_one in lines_csv:
		row=row_all(*r_one)
		print(row.IP)
		break
		
print("="*80)

with open("KD_csv.csv",encoding="utf-8") as f:
	lines_csv=csv.DictReader(f,delimiter=";")
	for row in lines_csv:
		print(row['IP'])
		break
