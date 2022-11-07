# Reference
# https://leetcode.cn/problems/lfu-cache/solution/yi-zhang-tu-shuo-ming-bai-by-powcai/
class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.freq = 1
        self.prev = self.next = None

class Double_Linked_List:
    def __init__(self):
        self.head = Node(None, None)
        self.tail = Node(None, None)
        self.head.next = self.tail
        self.tail.prev = self.head
        self.size = 0

    def append(self, node):
        self.tail.prev.next = node
        node.prev = self.tail.prev
        node.next = self.tail
        self.tail.prev = node
        self.size += 1

    # def pop(self):
    #     pop_node=self.head.next
    #     self.head.next=self.head.next.next

    #     self.head.next.pre=self.head

    #     self.length-=1
    #     return pop_node

    # def delete(self,delete_node):
    #     if self.length==0:
    #         # print("length=0")
    #         return
    #     temp_node=delete_node
    #     delete_node.pre.next=delete_node.next
    #     delete_node.next.pre=delete_node.pre

    #     self.length-=1
    #     return temp_node

    def pop(self, node=None):
        if self.size == 0:
            return
        if node is None:
            node = self.head.next
        node.prev.next = node.next
        node.next.prev = node.prev
        self.size -= 1
        return node

    def print_linked_list(self):
        temp = self.head
        while temp:
            print(temp.value)
            temp = temp.next


class LFUCache:
    def __init__(self, capacity: int):
        from collections import defaultdict
        self.key_to_node = {}
        self.freq = defaultdict(Double_Linked_List)
        self.min_freq = 0
        self.capacity = capacity

    def get(self, key: int) -> int:
        if key not in self.key_to_node:
            return -1
        node = self.key_to_node[key]
        node_freq = node.freq
        self.freq[node_freq].pop(node)
        if self.min_freq == node_freq and self.freq[node_freq].size == 0:
            self.min_freq += 1
        node.freq += 1
        self.freq[node.freq].append(node)
        return node.val

    def put(self, key: int, value: int) -> None:
        if self.capacity == 0:
            return
        if key in self.key_to_node:
            node = self.key_to_node[key]
            node_freq = node.freq
            self.freq[node_freq].pop(node)
            if self.min_freq == node_freq and self.freq[node_freq].size == 0:
                self.min_freq += 1
            node.freq += 1
            node.val = value
            self.freq[node.freq].append(node)
        else:
            if len(self.key_to_node) == self.capacity:
                node = self.freq[self.min_freq].pop()
                self.key_to_node.pop(node.key)
            node = Node(key, value)
            self.key_to_node[key] = node
            self.freq[1].append(node)
            self.min_freq = 1


# Your LFUCache object will be instantiated and called as such:
# obj = LFUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)

LFU = LFUCache(2)
# print(LFU.freq_dict[1].print_linked_list())
LFU.put(3, 1)
# print("my_dict",LFU.my_dict)
# print("freq_dict",LFU.freq_dict)
# print(LFU.freq_dict)
LFU.put(2, 1)
LFU.put(2, 2)
# print("my_dict",LFU.my_dict)
# print("freq_dict",LFU.freq_dict)
# print("---------------printing---------------------")
# print(LFU.freq_dict[1].print_linked_list())
LFU.put(4, 4)
LFU.get(2)


# # Reference
# # https://leetcode.cn/problems/lfu-cache/solution/yi-zhang-tu-shuo-ming-bai-by-powcai/
# class Node:
#     def __init__(self,value=None,key=None):
#         self.key=key
#         self.value=value
#         self.pre=None
#         self.next=None
#         self.freq=1

# class Double_Linked_List:
#     def __init__(self):
#         self.head=Node()
#         self.tail=Node()
#         self.head.next=self.tail
#         self.tail.pre=self.head
#         self.length=0

#     def append(self,append_node):
#         self.tail.pre.next=append_node
#         append_node.pre=self.tail.pre
#         append_node.next=self.tail
#         self.tail.pre=append_node

#         self.length+=1

#     def pop(self):
#         pop_node=self.head.next
#         self.head.next=self.head.next.next

#         self.head.next.pre=self.head


#         self.length-=1
#         return pop_node

#     def delete(self,delete_node):
#         if self.length==0:
#             # print("length=0")
#             return
#         temp_node=delete_node
#         delete_node.pre.next=delete_node.next
#         delete_node.next.pre=delete_node.pre

#         self.length-=1
#         return temp_node


#     def print_linked_list(self):
#         temp=self.head
#         while temp:
#             print(temp.value)
#             temp=temp.next


# class LFUCache:
#     def __init__(self, capacity: int):
#         from collections import defaultdict
#         self.capacity=capacity
#         self.my_dict={}
#         self.freq_dict=defaultdict(Double_Linked_List)
#         self.min_freq=0


#     def get(self, key: int) -> int:
#         if key not in self.my_dict:
#             return -1
#         else:
#             get_node=self.my_dict[key]
#             get_node_freq=get_node.freq
#             self.freq_dict[get_node_freq].delete(get_node)
#             if self.min_freq==get_node_freq and self.freq_dict[get_node_freq].length==0:
#                 self.min_freq+=1
#             get_node.freq+=1
#             self.freq_dict[get_node.freq].append(get_node)
#             return get_node.value


#     def put(self, key: int, value: int) -> None:
#         print("put")
#         if key in self.my_dict:
#             exist_node=self.my_dict[key]
#             exist_node_freq=exist_node.freq
#             self.freq_dict[exist_node_freq].delete(exist_node)
#             if self.min_freq==exist_node_freq and self.freq_dict[exist_node_freq].length==0:
#                 self.min_freq+=1
#             exist_node.freq+=1
#             exist_node.value=value
#             self.freq_dict[exist_node.freq].append(exist_node)
#         else:
#             if len(self.my_dict)==self.capacity:
#                 pop_node=self.freq_dict[self.min_freq].pop()
#                 self.my_dict.pop(pop_node.key)
#             append_node=Node(key,value)
#             self.my_dict[key]=append_node
#             self.freq_dict[1].append(append_node)
#             self.min_freq=1


# # Your LFUCache object will be instantiated and called as such:
# # obj = LFUCache(capacity)
# # param_1 = obj.get(key)
# # obj.put(key,value)
