#!/usr/bin/env python
import xlrd
import csv

# open the tsv file(output) in unicode format
with open('outTSV.tsv', 'w', encoding='utf-8') as TSVfile:
    wr = csv.writer(TSVfile, delimiter="\t")

    # open the xlsx file
    xlfile = xlrd.open_workbook('xlsx file with csv format')
    # retrieve sheet
    sheet = xlfile.sheet_by_index(0)

    # write rows into TSVfile
    for row in range(sheet.nrows):
        wr.writerow(sheet.row_values(row))
