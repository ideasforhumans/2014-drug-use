# Carly Gibson
# Joey Figaro
# Apr. 23, 2016
# converts TSV files to CSV

#
#  Required modules
#
import os
import inspect
import logging
import csv

logging.basicConfig(level = logging.DEBUG, format='[%(levelname)s] %(asctime)s -- %(message)s')
logging.debug('Converting .csv to .tsv...')

source = open(os.path.abspath('../2014-drug-use/_data/DS0001/dummy.tsv')).read()
output = open(os.path.abspath('../2014-drug-use/_data/DS0001/dummy.csv', 'w', newline = '')

reader_source = csv.reader(source, dialect = csv.excel_tab)
#source_data = list(reader_source)
#writer_source = csv.writer(output)

"""for row in source:
    writer_source.writerow(row)
    
output.close()"""
