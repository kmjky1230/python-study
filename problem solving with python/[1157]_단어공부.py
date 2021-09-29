string = input()
# change string to upper type word
string = string.upper()
size = len(string)

# A ~ Z의 개수를 저장할 수 있는 size의 list 생성
list = list(0 for i in range(ord('Z') - ord('A') + 1))

for i in range(ord('Z') - ord('A') + 1):
    for j in string:
        if chr(ord('A') + i) == j:
            list[i] += 1

max = 0
idx = 0
dup = False
for i in range(ord('Z') - ord('A') + 1):
    if max < list[i]:
        max = list[i]
        idx = i
        dup = False
    elif max == list[i] & max != 0:
        dup = True

if dup:
    print('?')
else:
    print(chr(ord('A') + idx))