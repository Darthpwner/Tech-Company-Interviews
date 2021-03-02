def are_rotations(str1, str2):
	size_1 = len(str1)
	size_2 = len(str2)

	if size_1 != size_2:
		print("False\n")
		return False

	concat = str1 + str1
	print("str1: {}".format(str1))
	print("str2: {}".format(str2))
	print("concat: {}".format(concat))
	if str2 in concat:
		print("True\n")
		return True
	else:
		print("False\n")
		return False

are_rotations("ABCD", "CDAB")
are_rotations("ABCAD", "DABCA")
are_rotations("ABCD", "DCBA")
are_rotations("ABCD", "DBAC")
