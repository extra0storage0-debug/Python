# r, c = map(int, input().split())
# mat = []
# for i in range(r):
#     row = list(map(int, input().split()))
#     mat.append(row)

# for i in mat:
#     tot = 0
#     for j in i:
#         tot += j
#     print(tot)



n = int(input())
d = {}

for i in range(n):
    key, value = input().split()
    d[key] = int(value)

highest = 0

for j in d.values():
    if highest < j:
        highest = j

print(highest)

