import json
import sys
import math

class UnitManager:
	def __init__(self):
		self.units = []

	def add_unit(self, unit):
		self.units.append(unit)

	def nearest_similar_units(self, unit, limit):
		# nearest = []
		# mostSimilar = None

		data_dict = {}

		distance = None

		maxDistance = -sys.maxsize - 1
		maxKey = None

		for i in self.units:
			distance = math.sqrt((unit.lat - i.lat)**2 + (unit.lng - i.lat)**2)
			
			if len(data_dict) < limit:
				if unit.beds == i.beds:	# Filter based on number of beds
					data_dict[unit.id] = (distance, unit.address, unit.city, unit.beds)
			else:
				if unit.beds != i.beds:
					continue
				else:
					for key, value in data_dict:
						if value[0] > maxDistance:
							maxDistance = value[0]
							maxKey = key

					if distance < max(seq):		# Kick out largest distance
						nearest.remove(data_dict[maxKey])
						nearest.append(distance)

		print("{} nearest units: {}".format(limit, data_dict))

class Unit:
	def __init__(self, id, address, baths, beds, city, floor, has_elevator, has_parking, has_pool, has_view, lat, lng, square_feet):
		self.id = id
		self.address = address
		self.baths = baths
		self.beds = beds
		self.city = city
		self.floor = floor
		self.has_elevator = has_elevator
		self.has_parking = has_parking
		self.has_pool = has_pool
		self.has_view = has_view
		self.lat = lat
		self.lng = lng
		self.square_feet = square_feet


unitManager = UnitManager()

# Implement this later 
# fp = open('units_small.json')
# print(fp)

with open('units_small.json') as json_data:
	d = json.load(json_data)
	# print(d)

for line in d:
	print(line)
	print(line["id"])
	unit = Unit(line["id"], line["address"], line["baths"], line["beds"], line["city"], line["floor"], line["has_elevator"], line["has_parking"], line["has_pool"], line["has_view"], line["lat"], line["lng"], line["square_feet"])

	unitManager.add_unit(unit)	# Add individual units

	unitManager.nearest_similar_units(unit, 3)	# Nearest check