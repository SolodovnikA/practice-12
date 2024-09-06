text = input()
text.replace(' ', '*')
count = 1
mx = 0

for i in range(len(text)):
    if text[i-1] == '*' and text[i] == '*':
        count += 1
        mx = max(count, mx)
    else:
        count = 1

print(mx)


'''
text = input()
text.replace(' ', '*')
print(len(max(text, key = len)))
'''