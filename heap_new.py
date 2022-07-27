class Heap:
    def __init__(self,heap):
        self.heap=heap
    
    def heapify(self):
        # 这里看不太明白
        for i in range((len(self.heap)+1)//2-1,-1,-1):
            self.shift_down(i)

    def shift_down(self,index):
        left=index*2+1
        right=index*2+2
        if left<len(self.heap) and self.heap[left]>self.heap[index]:
            largest=left
        else:
            largest=index
        # 这里为什么不使用left，right和index相互比较，而是先赋值largest再和right比较
        if right<len(self.heap) and self.heap[right]>self.heap[largest]:
            largest=right
        if largest!=index:
            self.heap[largest],self.heap[index]=self.heap[index],self.heap[largest]
            self.shift_down(largest)


    def shift_up(self,index):
        parent=(index+1)//2-1
        # 这里为什么不是(index-1)//2
        if parent>=0 and self.heap[parent]<self.heap[index]:
            smallest=parent
        else:
            smallest=index
        if smallest!=index:
            self.heap[smallest],self.heap[index]=self.heap[index],self.heap[smallest]
            self.shift_up(smallest)

    def add(self,value):
        self.heap.append(value)
        self.shift_up(len(self.heap)-1)
    
    def pop(self):
        self.heap[0],self.heap[len(self.heap)-1]=self.heap[len(self.heap)-1],self.heap[0]
        value=self.heap.pop()
        self.shift_down(0)
        return value


# my_heap=Heap([2,1,3,6,4,5])
# my_heap.heapify()
# print(my_heap.heap)
# my_heap.pop()
# print(my_heap.heap)
# my_heap.pop()
# print(my_heap.heap)
# my_heap.add(10)
# print(my_heap.heap)

my_heap=Heap([3,2,1,5,6,4])
my_heap.heapify()
print(my_heap.heap)