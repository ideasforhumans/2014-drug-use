# Carly Gibson
# Joey Figaro
# Apr. 23, 2016
# converts TSV files to CSV

#
#  Required modules
#
import os
import inspect

source = open(os.path.abspath('../2014-drug-use/_data/DS0001/data.tsv')).read()
print(source)
