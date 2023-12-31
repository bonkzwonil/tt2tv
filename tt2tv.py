#!/usr/bin/env python
# coding: utf-8

import numpy as np
import pandas as pd


df = pd.read_csv('tw.csv', sep=',', usecols = ['Date', 'Type', 'Average Price', 'Symbol', 'Action'], thousands = ',' , dtype = {'Average Price': np.float32})

#preamble
print("// © traderbonk")

print("//@version=5")
print("indicator(\"Tastytrade fills\", overlay = true)")

print("")

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




