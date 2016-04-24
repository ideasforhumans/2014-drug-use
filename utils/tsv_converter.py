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

source = open(os.path.abspath('../2014-drug-use/_data/DS0001/data.tsv')).read()

print(csv.reader(source))

reader_source = csv.reader(source)
source_data = list(reader_source)
print(source_data)
