#!/usr/bin/env python

input = ["a", ["b","c","d"], [], ["e"], [[],"f",[],[],"g"]]
res = []
#LESSONS LEARNED HERE
# 1.) Strings are immutable in python. Cannot be modified. If they are, they arenot saved??? FIND OUT WHAT ACTUALLY HAPPENS HERE. Regardless, if res = "", the function does not work properly vs. if you used a list

# 2.) filtered_list = filter(None, old_list) will filter out all empty lists in the case that they cause problems... DO NOT FORGET EDGE CASES

def flatten(input, result):
	for i in input:
		print(i)
		if type(i) == type([]):
			flatten(i, result)
		else:
			result+=i
			print(result)
	return result

print(flatten(input, res))
