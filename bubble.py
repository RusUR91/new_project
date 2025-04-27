
a = int(input())
spisok = list(map(int, input().split()))

for run in range(a-1):
    for i in range(a-1-run):
        if spisok[i] > spisok[i+1]:
            spisok[i],spisok[i+1] = spisok[i+1],spisok[i]
print(spisok)


    