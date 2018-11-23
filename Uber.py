# Enter your code here. Read input from STDIN. Print output to STDOUT
#Given 2 sets of intervals.

#Interval is defined with left and right border and discrete points, like [2, 3], [0, 0], etc.

#Set of intervals is non intersected set of sorted intervals, for example: [0, 0], [2, 2], [5, 10] is a valid set of intervals

#1st set: [0, 2], [5, 10], [16, 20] # M - nuymber of lists
#2nd set: [1, 5], [10, 18], [20, 23]



# i is ptr to s1, j is ptr to s2
for i, j in range(0, len(s1) + len(s2)):
    if s2[j][1] <= s1[i][0]:
        j += 1
    elif s1[i][1] <= s2[j][0]:
        i += 1
        
    intersection.append(s1[i][2], s2[j][1])

# combined set: [0, 2], [1, 5], [5, 10], [10, 18], [16,  20], [20, 23]

# curr, after
# for i in range(0, len(combinedList) - 1)
[combinedList[i + 1][0], combinedList[i][1]]
# [after[0], curr[1]]
# [1, 2], [5, 5], [10, 10], [16, 18], [20, 20]

#AND Result (find intersection of elements): [1, 2], [5, 5], [10, 10], [16, 18], [20, 20]

#1st set: [0, 1], [4, 22], [23, 26], [27, 29]
#2nd set: [1, 5], [10, 24]


#AND Result (find intersection of elements): [1, 1], [4, 5], [10, 22], [23, 24]


def intersection(set1, set2):
    intersection = []
    
    for i in set1:
        for j in set2:
            if j[0] <= i[1] and j[1] >= i[0]:
                left = max(i[0], j[0])
                right = min(i[1], j[1])
                intersection.append([left, right])
                
        
    return intersection
    
set1 = [[0, 2], [5, 10], [16, 20]]
set2 = [[1, 5], [10, 18], [20, 23]]

set3 = [[0, 1], [2, 2], [3, 5], [19, 25]]

set4 = [[0, 1], [4, 22], [23, 26], [27, 29]]
set5 = [[1, 5], [10, 24]]

print(intersection(set1, set2))
print(intersection(set1, set3)) # [0, 1], [1, 2], [5, 5], [19, 20]
print(intersection(set4, set5))
