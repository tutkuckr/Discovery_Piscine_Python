#!/usr/bin/env python3

org_arr = [2, 8, 9, 48, 8, 22, -12, 2]
seen = set()
res = []

for i in org_arr:
	if i not in seen:
		seen.add(i)
		if i > 5:
			res.append(i + 2)
print(res)