import function_exercises as f
import itertools as i
import json
profile = json.load(open('profiles.json'))


f.calculate_tip(.05,100)

f.normalize_name("#########Stanny big big")

f.is_two(2)

marker = list(i.product("abc",[1,2,3]))
marker2 = list(i.combinations("abcd",2))
marker3 = list(i.permutations("abcd",2))

print(marker)
print(len(marker))

print(marker2)
print(len(marker2))

print(marker3)
print(len(marker3))
active_users = 0
inactive_users = 0
for l in profile:
    if l["isActive"]==True:
            active_users += int(l["isActive"]) 
for e in profile:
    if e["isActive"]==False:
            inactive_users += int(e["isActive"]) 
print(f"The number of active users is {active_users}, and the number of inactive users is {inactive_users}")

