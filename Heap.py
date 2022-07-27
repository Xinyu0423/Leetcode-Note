from cgi import test


class Heap:
    def __init__(self,max_length):
        self.heap_list=[None for _ in range(max_length)]
        self.index=0

    def shift_up(self,index):
        if index<=0 or self.heap_list[index]<=self.heap_list[(index-1)//2]:
            return
        self.heap_list[(index-1)//2],self.heap_list[index]=self.heap_list[index],self.heap_list[(index-1)//2]
        self.shift_up((index-1)//2)

    def add(self,value):
        if self.index==len(self.heap_list):
            print("heap is full")
            return
        self.heap_list[self.index]=value
        self.shift_up(self.index)
        self.index+=1
        pass

    def shift_down(self,index):
        left_index=2*index+1
        right_index=2*index+2
        temp_index=index
        if left_index<self.index and self.heap_list[index]<self.heap_list[left_index] and self.heap_list[left_index]>self.heap_list[right_index]:
            self.heap_list[index],self.heap_list[left_index]=self.heap_list[left_index],self.heap_list[index]
            self.shift_down(left_index)
        elif right_index<self.index and self.heap_list[index]<self.heap_list[right_index]:
            self.heap_list[index],self.heap_list[right_index]=self.heap_list[right_index],self.heap_list[index]
            self.shift_down(right_index)
        return

    def remove(self):
        removed=self.heap_list[0]
        self.heap_list[0]=self.heap_list[self.index-1]
        print("index=",self.index)
        self.shift_down(0)
        self.heap_list[self.index-1]=None
        self.index-=1
        return removed
        

test_heap=Heap(8)
test_heap.add(6)
test_heap.add(4)
test_heap.add(5)
test_heap.add(2)
test_heap.add(1)
test_heap.add(3)
print(test_heap.heap_list)
test_heap.add(7)
print(test_heap.heap_list)
test_heap.remove()
print(test_heap.heap_list)
test_heap.remove()
print(test_heap.heap_list)


#         6
#     4       5
# 2      1   3  


    #         7
    #     4       6
    #   2    1  3    5

    #         6
    #     4       5
    # 2      1   3
    
