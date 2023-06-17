# tt2tv
Creates a Pine Script to display fills from Tastytrade / (ex Tastyworks) in Tradingview Charts

Usage: 

put a csv export from tastyworks executions into tw.csv
```
$ python3 tt2tv.py 
// © traderbonk
//@version=5
indicator("Tastytrade fills", overlay = true)

if syminfo.ticker(syminfo.tickerid) == "AAPL"
	label.new(timestamp("2023-01-03T20:56:56+0100"), 124.62, xloc = xloc.bar_time, yloc = yloc.price, size = size.tiny, style = label.style_triangledown, color = color.red)
if syminfo.ticker(syminfo.tickerid) == "AMZN"
	label.new(timestamp("2023-01-03T20:32:40+0100"), 85.19, xloc = xloc.bar_time, yloc = yloc.price, size = size.tiny, style = label.style_triangledown, color = color.red)
if syminfo.ticker(syminfo.tickerid) == "AMZN"
	label.new(timestamp("2023-01-03T20:32:40+0100"), 85.19, xloc = xloc.bar_time, yloc = yloc.price, size = size.tiny, style = label.style_triangledown, color = color.red)
if syminfo.ticker(syminfo.tickerid) == "AMZN"
	label.new(timestamp("2023-01-03T20:32:40+0100"), 85.19, xloc = xloc.bar_time, yloc = yloc.price, size = size.tiny, style = label.style_triangledown, color = color.red)

....
```


copy result into a TradingView Pine Script Buffer

