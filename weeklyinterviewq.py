x = {
    "cat": "bob",
    "dog": 23,
    19: 18,
    90: "fish"
}

total = 0

for key, value in x.items():
    # if type(value) == int:
    if isinstance(value, int):
        total += value

print(total)
