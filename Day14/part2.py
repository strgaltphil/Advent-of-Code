def resulting_pairs(pair: str) -> tuple:
    return (pair[0] + rules[pair], rules[pair] + pair[1], rules[pair])

with open("input.txt") as file:
    data = [line for line in file.read().split("\n") if line != ""]

template = [tuple(d) for d in data if " -> " not in d][0]
rules, pairs = dict(), dict()

for k, v in [d.split(" -> ") for d in data if " -> " in d]:
    rules[k] = v
    pairs[k] = int(0)

for i in range(len(template) - 1):
    pairs["".join(template[i:i+2])] += 1

result = dict()

for t in template:
    result[t] = result.get(t, 0) + 1

for _ in range(40):
    tmp = pairs.copy()
    for k, v in pairs.items():
        if v > 0:
            a, b, c = resulting_pairs(k)

            result[c] = result.get(c, 0) + v

            tmp[a] += v
            tmp[b] += v
            tmp[k] -= v
    pairs = tmp

print(f"Solution: {result[max(result, key=result.get)] - result[min(result, key=result.get)]}")