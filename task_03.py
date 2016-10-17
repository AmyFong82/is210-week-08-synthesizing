#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""A mortgage calculator."""

import decimal

NAME = raw_input('What is your name? ')
P = int(raw_input('What is the amount of your principal? '))
T = int(raw_input('For how many years is this loan being borrowed? '))
PREQUA = raw_input('Are you pre-qualified? ')
MONTH = 12

if PREQUA[0] == 'Y' or PREQUA[0] == 'y':
    PREQUA = 'Yes'
elif PREQUA[0] == 'N' or PREQUA[0] == 'MONTH':
    PREQUA = 'No'

if P <= 199999:
    if 1 <= T <= 15:
        if PREQUA == 'Yes':
            RATE = decimal.Decimal(0.0363)
        else:
            RATE = decimal.Decimal(0.0465)
    elif 16 <= T <= 20:
        if PREQUA == 'Yes':
            RATE = decimal.Decimal(0.0404)
        else:
            RATE = decimal.Decimal(0.0498)
    elif 21 <= T <= 30:
        if PREQUA == 'Yes':
            RATE = decimal.Decimal(0.0577)
        else:
            RATE = decimal.Decimal(0.0639)

if 200000 <= P <= 999999:
    if 1 <= T <= 15:
        if PREQUA == 'Yes':
            RATE = decimal.Decimal(0.0302)
        else:
            RATE = decimal.Decimal(0.0398)
    elif 16 <= T <= 20:
        if PREQUA == 'Yes':
            RATE = decimal.Decimal(0.0327)
        else:
            RATE = decimal.Decimal(0.0408)
    elif 21 <= T <= 30:
        if PREQUA == 'Yes':
            RATE = decimal.Decimal(0.0466)
        else:
            RATE = 0

if P >= 1000000:
    if 1 <= T <= 15:
        if PREQUA == 'Yes':
            RATE = decimal.Decimal(0.0205)
        else:
            RATE = 0
    elif 16 <= T <= 20:
        if PREQUA == 'Yes':
            RATE = decimal.Decimal(0.0262)
        else:
            RATE = 0
    elif T > 20:
        RATE = 0

A = P * (1 + (RATE / MONTH))**(MONTH * T)

if RATE == 0:
    TOTAL = 'Loan not available.'
else:
    TOTAL = '${:,.0f}'.format(A)

P = '${:,.0f}'.format(P)

REPORT = 'Loan Report for: {0} \n'
REPORT += ('-' * 50 + '\n'
           '      {Principal:16}' + '{1:>10} \n'
           '      {Duration:16}' + '{2:>10} \n'
           '      {Prequ:16}' + '{3:>10} \n\n'
           '      {Total:6}' + '{4:>20}')
REPORT = REPORT.format(NAME, P, str(T)+'yrs', PREQUA, TOTAL,
                       Principal='Principal:', Duration='Duration:',
                       Prequ='Pre-qualifies?:', Total='Total:')
print REPORT
