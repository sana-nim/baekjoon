from typing import MutableSequence

def insertion_sort(a: MutableSequence) -> None:
    n = len(a)
    for i in range(1,n):
        j = i
        tmp = a[i]
        while(j > 0 and a[j - 1] > tmp):
            a[j] = a[j - 1]
            j-=1
        a[j] = tmp

if __name__ == '__main__':
    print("단순 삽입 정렬")
    num = int(input("원소 수를 입력하세요: "))
    x = [None] * num  # 크기가 num인 리스트 선언

    for i in range(num):
        x[i] = int(input(f"{i + 1}번째 값을 입력하세요: "))  

    print("입력된 값:", x)  # 입력값 출력

    print(x)
    insertion_sort(x)
    print(x)