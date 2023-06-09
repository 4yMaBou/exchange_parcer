import ccxt

exchange = ccxt.okcoinusd()
okcoinusd1 = ccxt.okcoinusd({"id":'okcoinusd1'})
okcoinusd2 = ccxt.okcoinusd({"id":'okcoinusd2'})
id = 'btcchina'
btcchina = eval('ccxt.%s ()' % id)
coinbasepro = getattr (ccxt, 'coinbasepro') ()

