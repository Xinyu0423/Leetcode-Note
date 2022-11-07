from telnetlib import DO


class Node:
    def __init__(self,value=None):
        self.value=value
        self.pre=None
        self.next=None

class Double_Linked_List:
    def __init__(self):
        self.head=Node()
        self.tail=Node()
        self.head.next=self.tail
        self.tail.pre=self.head
        self.length=0

    def append(self,append_node):
        self.tail.pre.next=append_node
        append_node.pre=self.tail.pre
        append_node.next=self.tail
        self.tail.pre=append_node

        self.length+=1

    def pop(self):
        self.head.next.next.pre=self.head
        self.head.next=self.head.next.next

        self.length-=1

    def delete(self,delete_node):
        delete_node.pre.next=delete_node.next
        delete_node.next.pre=delete_node.pre

        self.length-=1
        

    def print_linked_list(self):
        temp=self.head
        while temp:
            print(temp.value)
            temp=temp.next



            

double_linked_list=Double_Linked_List()
temp=Node(2)
double_linked_list.append(Node(1))
double_linked_list.append(temp)
double_linked_list.append(Node(3))

double_linked_list.delete(temp)
double_linked_list.print_linked_list()
# double_linked_list.pop()
# double_linked_list.pop()
# double_linked_list.pop()
# double_linked_list.print_linked_list()
# double_linked_list.append(Node(4))
# double_linked_list.print_linked_list()
# "3->4"