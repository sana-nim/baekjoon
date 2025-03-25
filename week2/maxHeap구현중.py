class MaxHeap:
    def __init__(self):
        self.heap = [None]  # 인덱스 1부터 시작하도록 설정

    def insert(self, value):
        self.heap.append(value)
        index = len(self.heap)-1

        while index > 1:
            if self.heap[index] > self.heap[index // 2]:
                self.heap[index],self.heap[index // 2] = self.heap[index // 2], self.heap[index]
                index = index//2
        return self.heap

    def delete(self):
        if len(self.heap) <= 0:
            return None

        # 삭제 (Delete)
        # 루트 노드 삭제
        # 마지막 노드를 루트로 이동
        root = self.heap[1]
        self.heap[1] = self.heap[-1]
        self.heap.pop()
        index = 1
        while index < len(self.heap):
            left_child = index * 2
            right_child = index * 2 + 1
            bigger = index
        # 자식 노드와 비교 → 더 큰 값과 교환
            if self.heap[bigger] < self.heap[left_child]:
                self.heap[bigger], self.heap[left_child] = self.heap[left_child], self.heap[bigger]
                bigger = left_child
                index = left_child

            if self.heap[bigger] < self.heap[right_child]:
                self.heap[bigger], self.heap[right_child] = self.heap[right_child], self.heap[bigger]
                bigger = right_child
                index = right_child

        return root
        # 힙 성질이 만족될 때까지 반복
        # 최대 log n번 교환 가능


    def heapify(self, index):
        # 특정 노드에서 시작
        # 자식 노드와 비교 → 더 큰 값과 교환
        # 힙 성질이 만족될 때까지 반복
        # 최대 log n번 교환 가능
        pass

    def print_heap(self):
        print(self.heap[1:])
