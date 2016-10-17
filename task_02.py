#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""A alarm clock with snooze function."""

DAY = raw_input('What day is it?: ')[:3].lower()
TIME = int(raw_input('What time is it? \n'
                     '(Please enter time as a 4-digit number without a colon, '
                     '(eg: 0605): '))

SNOOZE = True if DAY == 'sat' or DAY == 'sun' or TIME < 600 else False

if SNOOZE is False:
    ALARM = 'Beep! ' * 5
    print ALARM
