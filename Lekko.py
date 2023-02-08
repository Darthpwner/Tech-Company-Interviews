# input = [
#   ["SJC", "DFW"],
#   ["LAX", "SFO"],
#   ["ATL", "SJC"],
#   ["EWR", "ATL"],
#   ["SFO", "EWR"]
# ]

# output:
# ["LAX", "SFO", "EWR", "ATL", "SJC", "DFW"]

# [Lax, SFO]  <- i
# [SFO, EWR] <- j

# No cycles for the time being

from typing import _SpecialForm, no_type_check_decorator

# Connections dict:
# SJC -> DFW
# LAX -> SFO
# ATL -> SJC
# EWR -> ATL
# SFO -> EWR

# input: start node

# SJC -> DFW
# LAX -> SFO -> EWR -> ATL -> SJC -> DFW

# # loop through the input
# take start node, save destination node
# Check if the destination node is a key and build out flight list from here


def process_flight(input):
    flight = []
    connections_dict = {}

    # Process input, save into connections dict
    for i in input:
        if i[0] not in connections_dict:
            connections_dict[i[0]] = i[1]
    print(connections_dict)

    # LAX -> SFO
    for i in input:
        start = i[0]
        curr_destination = i[1]
        flight = [start]
        while curr_destination in connections_dict:
            flight.append(curr_destination)
            curr_destination = connections_dict[curr_destination]
        flight.append(curr_destination)

        if len(flight) == len(input) + 1:   # We have complete path, return
            print("flight: {}\n".format(flight))
            return flight


input = [
  ["SJC", "DFW"],
  ["LAX", "SFO"],
  ["ATL", "SJC"],
  ["EWR", "ATL"],
  ["SFO", "EWR"]
]

process_flight(input)