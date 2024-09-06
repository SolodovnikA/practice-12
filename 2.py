text = input()
count = 1
mx = 0

for i in range(len(text)):
    if text[i-1] == text[i]:
        count += 1
        mx = max(count, mx)
    else:
        count = 1

print(mx)