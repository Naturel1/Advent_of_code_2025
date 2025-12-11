from collections import defaultdict

lines = open("puzzle.txt").read().splitlines()

outputs = defaultdict(list)
for line in lines:
    a, b = line.split(": ")
    outputs[a] = b.split(" ")

visited = {}


def dfs(current, target):
    key = (current, target)
    if key in visited:
        return visited[key]
    if current == target:
        return 1
    out = 0
    for n in outputs[current]:
        out += dfs(n, target)
    visited[key] = out
    return out


p1 = dfs("you", "out")
print(p1)

if dfs("dac", "out") > 0:
    p2 = dfs("svr", "fft") * dfs("fft", "dac") * dfs("dac", "out")
else:
    p2 = dfs("svr", "dac") * dfs("dac", "fft") * dfs("fft", "out")

print(p2)