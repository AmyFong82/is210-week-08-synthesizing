#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Choosing colors for my room."""

BASE = raw_input('Which base color, "Seattle Gray" or "Manatee"?: ')

if BASE == 'Seattle Gray':
    ACCENT = raw_input('Which accent color, "Ceramic Glaze" or '
                       '"Cumulus Nimbus"?: ')
    if ACCENT == 'Ceramic Glaze':
        HIGHLIGHT = raw_input('Which highlight color, "Basically White" or '
                              '"White"?: ')
    elif ACCENT == 'Cumulus Nimbus':
        HIGHLIGHT = raw_input('Which highlight color, "Off-White" or '
                              '"Paper White"?: ')
elif BASE == 'Manatee':
    ACCENT = raw_input('Which accent color, "Platinum Mist" or '
                       '"Spartan Sage"?: ')
    if ACCENT == 'Platinum Mist':
        HIGHLIGHT = raw_input('Which highlight color, "Bone White" or '
                              '"Just White"?: ')
    elif ACCENT == 'Spartan Sage':
        HIGHLIGHT = raw_input('Which highlight color, "Fractal White" or '
                              '"Not White"?: ')
COLORS = 'Your selected colors are, {0}, {1}, and {2}.'.format(BASE, ACCENT,
                                                               HIGHLIGHT)
print COLORS
