import math

dino = {}
sol = []

def read_data(path):
	with open(path, "r") as csv_file:
		for line in csv_file:
			info = line.split(",")
			name = info[0]
			sub = info[1]
			sub2 = info[2]
			if name not in dino:
				dino[name] = [sub]
			else:
				dino[name] = dino[name] + [sub] + [sub2]
	return dino

def speed(STRIDE_LENGTH, LEG_LENGTH):
	rate = ((float(STRIDE_LENGTH) / float(LEG_LENGTH)) - 1) * math.sqrt(float(LEG_LENGTH) * 9.8)
	return rate


def run():
	read_data("dataset1.csv")
	read_data("dataset2.csv")

	for i in dino:
		if len(dino[i]) == 3 and "bipedal" in dino[i][2]:
			rate = speed(dino[i][1], dino[i][0])
			sol.append([rate, i])
	order = sorted(sol, reverse=True)

	print("dino: {}".format(dino))
	print("order: {}".format(order))

	for name in order:
		print(name[1])

run()
