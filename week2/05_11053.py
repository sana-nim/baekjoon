def binarySearch(board, target):
    start, end = 0, len(board) - 1
    while start <= end:
        mid = (start + end) // 2
        if board[mid] < target:
            start = mid +1
        else:
            end = mid-1
    return start

n = int(input())
a = list(map(int, input().split()))
board = []

for num in a:
    if not board or num > board[-1]:
        board.append(num)
    else:
        SearchNumber = binarySearch(board,num)
        board[SearchNumber] = num
print(len(board))
print (board)
