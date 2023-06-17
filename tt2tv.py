#!/usr/bin/env python
# coding: utf-8

import numpy as np
import pandas as pd


df = pd.read_csv('tw.csv', sep=',')

## Create pine script
for index, row in df.iterrows():
    if row['Type'] == "Trade":
        sym = row['Symbol']
        shape = 'label.style_triangleup' if row['Action'].startswith("BUY") else 'label.style_triangledown'
        color = 'color.green' if shape == 'label.style_triangleup' else 'color.red'
        ts = row['Date']
        price = abs(row['Average Price'])

        print(f"if syminfo.ticker(syminfo.tickerid) == \"{sym}\"")
        print(f"\tlabel.new(timestamp(\"{ts}\"), {price}, xloc = xloc.bar_time, yloc = yloc.price, size = size.tiny, style = {shape}, color = {color})")




