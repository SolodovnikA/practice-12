text = input()
cur = None
cnt = 0
for i in range(len(text)):
    cur = text[i]
    cnt = text.count(cur)
    if cnt == 3:
        print(cur)
        break
    else:
        text = text.replace(cur, '')
