#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__="Markus Strehlau"
__version__="2010-07-02"

#import sys
#import time
from operator import itemgetter
from subprocess import call


Cupslist={} #def. dict

FilterMonat= "Jun"



def main():
     
	i=0

	for line in open("page_log"):
		username = line.split(' ')[1]
		seitenzahl = line.split(' ')[-2]
		datum = line.split('/')[1]+line.split('/')[2][0:4]

		if (FilterMonat in datum):
			if(Cupslist.has_key(username)==False):
				Cupslist[username]=int(seitenzahl)
			else:
				Cupslist[username]+= int(seitenzahl)
    	# Open a file
	fo = open("plot.txt", "wb") #Die befehls Datei fuer gnuplot
	out = open("blame.csv", "wb") # Daten
	fo.write( 'set ylabel "seiten"\nset xtics ');

	gnu = '('

	for blame in sorted(Cupslist.items(), key=itemgetter(1)):
		i+=1
		print('"%s", %s') %blame 
		out.write('"%s", %s\n' %blame)
		gnu+=('"%s" %i, '  % (blame[0], i))
#		fo.write('"%s" %i, '  % (blame[0], i));
		

	gnu=gnu.rstrip(', ')
#	gnu.rstrip(',')
	gnu+= ')'

	fo.write ('%s\nplot "blame.csv" using 2 w boxes' % gnu)

	# Close opend file
	fo.close()

#	call(['gnuplot "plot.txt"']) #will noch nicht so wie ich will
	
                        
if __name__ == "__main__":
   main()
