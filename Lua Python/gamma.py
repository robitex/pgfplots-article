#!/usr/bin/python

#
# Copyright (C) 2011 Agostino De Marco
#                    <agostino dot demarco at unina dot it>
#                    Roberto Giacomelli
#                    <giaconet dot mailbox at gmail dot com>
#
#    This work may be distributed and/or modified under the
#    conditions of the LaTeX Project Public License, either
#    version 1.3 of this license or any later version.
#    The latest version of this license is in
#    http://www.latex-project.org/lppl.txt and version 1.3
#    or later is part of all distributions of LaTeX version
#    2005/12/01 or later.
#
# This work has the LPPL maintenance status `maintained'.
# 
# The Current Maintainer of this work are Agostino De Marco
# and Roberto Giacomelli
#

# import delle librerie necessarie
import os
import numpy as np
from scipy.special import gamma as Gamma

def add(v):
	"""Simplify to append data to content"""
	content.append(v+'\n')

# definizione dei limiti del grafico
# per il facile 'aggiustamento'
x0, x1 = -5.0, 5.2
y0, y1 = -6.5, 7.0

# dominio lineare sull'asse x
x = np.arange(x0, x1, 0.005)

# creazione dei vettori di ordinata
y = Gamma(x)

# 'gestione' delle discontinuita
y[y>100*y1] = 'inf'
y[y<100*y0] = 'inf'

# costruzione dati di plottaggio
data = []
data.extend(''.join(['{0} {1}\n'.format(u, v) \
                    for u, v in zip(x,y)]))

# scrittura file dati
f = open('data.txt', 'w')
f.writelines(data)
f.close()

# creazione sorgente TeX
content = []
add('% build by a Python script\n')
add('\\documentclass{standalone}')
add('\\usepackage{lmodern}')
add('\\usepackage{pgfplots}')
add('\\begin{document}')
add('\\begin{tikzpicture}')
add('\\begin{axis}[')

# opzioni grafico
add('title={The $\\Gamma$ function},')
add('tick label style={font=\scriptsize},')
add('xmin='+str(x0)+',')
add('xmax='+str(x1)+',')
add('ymin='+str(y0)+',')
add('ymax='+str(y1)+',')
add('xtick={-5,...,5},')
add('grid=major,')
add('unbounded coords=jump')
add(']')

# plottaggio
add('\\addplot+[no markers] file {data.txt};')
add('\\addplot[mark=*,only marks,fill=red] coordinates {')
add('(2,1)')
add('(3,2)')
add('(4,6)')
add('};')
# chiusura sorgente
add('\\end{axis}')
add('\\end{tikzpicture}')
add('\\end{document}')

# scrittura file sorgente
filename = 'graficoGamma'
s = open(filename+'.tex', 'w')
s.writelines(content)
s.close()

# compilazione del grafico
os.system('pdflatex ' + filename)
os.remove(filename +'.aux')
os.remove(filename +'.log')








