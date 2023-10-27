import function_exercises as f
import itertools as i
import json
json.load(open('profiles.json'))


f.calculate_tip(.05,100)

f.normalize_name("#########Stanny big big")

f.is_two(2)

marker = list(map(".".join,list(i.combinations("abc123",2))))
marker3 = list(map(".".join,list(i.combinations("abc123",3))))
marker2 = list(map(".".join,list(i.permutations("abcd",2))))

print(marker)

print(marker2)

print(marker3)
