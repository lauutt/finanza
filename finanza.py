#!/usr/bin/env python3

import yfinance as yf
import datetime
import fincsv as cs
import sys
from fpdf import FPDF
from createrp import createpdf

def main(arguments):
	#Initialize sum of stocks values
	suma = 0.0
	#Filename to examine
	argv = sys.argv[1]
	#Return dictionary based on csv file
	empresas = cs.csv_to_dict(argv)
	#Initialize list of stocks
	stockslist = []

	for nombre, cantidad in empresas.items():
		#Get data from stock name
		get = yf.Ticker(nombre)
		try:
			#Multiply quantity of stocks * stock price
			invested = (cantidad * get.info['ask'])
		except:
			#Exception to extract information from crypto
			invested = (cantidad * get.info['regularMarketDayHigh'])
		suma+=invested
		stockslist.append(nombre + ': ' + str(round(invested, 2)))
		print(nombre + ': ' + str(round(invested, 2)))

	#Create PDF with information
	suma = str(round(suma,2))

	createpdf(stockslist, suma)

	print('Total : '+suma)


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))