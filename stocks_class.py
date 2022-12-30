class Stock:
	def __init__(self, name, shares, price):
		self.name = name
		self.shares = shares
		self.price = price

	def value(self):
		return self.shares * self.price

	def sell(self, nshares):
		self.shares -= nshares

# Read a portfolio file into a list of stock objects
def read_portfolio(filename):
	stocks = []
	for line in open(filename):
		fields = line.split()
		s = Stock(fields[0], int(fields[1]), float(fields[2]))
		stocks.append(s)
	return stocks

# Read prices into a dictionary
def read_prices(filename):
	prices = {}
	for line in open(filename):
		fields = line.split(',')
		prices[fields[0]] = float(fields[1])
	return prices
