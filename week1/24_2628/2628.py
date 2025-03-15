paper = list(map(int, input().split()))
cnt = int(input())
width_list = []
height_list = []

width_max = paper[0]
height_max = paper[1]
row_max = 0
column_max = 0
target = []
for i in range(cnt):
    target.append(list(map(int, input().split())))

target.sort()

for i in range(cnt):
    if target[i][0] == 1:
        width_list.append(target[i][1])
    else:
        height_list.append(target[i][1])

width_list.insert(0, 0)
height_list.insert(0, 0)
width_list.append(width_max)
height_list.append(height_max)

for i in range(len(height_list)-1):
    if(height_list[i+1] - height_list[i] > row_max):
        row_max = height_list[i+1] - height_list[i]
for i in range(len(width_list)-1):
    if(width_list[i+1] - width_list[i] > column_max):
        column_max = width_list[i+1] - width_list[i]

print(row_max*column_max)