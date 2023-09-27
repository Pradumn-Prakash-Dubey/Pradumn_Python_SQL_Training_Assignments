class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

class LinkedList:
    def __init__(self):
        self.head=None

    def append(self,data):
        new_node=Node(data)
        if self.head==None:
            self.head=new_node
            return
        else:
            current=self.head
            while current.next!=None:
                current=current.next
            current.next=new_node

    def insert(self,index,data):
        if index <=0:
            return f"Enter valid index"
        new_node=Node(data)
        if index==1:
            new_node.next=self.head
            self.head=new_node
            return
        else:
            current=self.head
            count=1
            while current!=None:
                if count==index-1:
                    new_node.next=current.next
                    current.next=new_node
                    return f"{data} inserted at {index}"
                count+=1
                current=current.next
            return f"Index given out of range"

    def remove(self,index):
        if index<=0:
            return f"Enter valid index"
        if index==1:
            if self.head!=None:
                data=self.head.data
                self.head=self.head.next
                return data
            else:
                return f"Nothing to remove"
        current=self.head
        count=1
        while current!=None:
            if count==index-1:
                if current.next!=None:
                    data=current.next.data
                    current.next=current.next.next
                    return data
                else:
                    return f"Nothing to remove, index out of range"
            count+=1
            current=current.next
        return f"Index out of range,cannot remove"

    
    def get(self,index):
        if index<=0:
            return f"Index should be valid"
        current=self.head
        count=1
        while current!=None:
            if count==index:
                return current.data
            count+=1
            current=current.next
        return f"Index out of range"
    
    def set(self,index,data):
        if index<=0:
            return f"Index should be valid"
        current=self.head
        count=1
        while current!=None:
            if count==index:
                current.data=data
                return
            count+=1
            current=current.next
        return f"Index out of range"
            
    def size(self):
        current=self.head
        count=0
        while current!=None:
            count+=1
            current=current.next
        return count
    
    def info(self):
        current=self.head
        while current!=None:
            print(current.data,end=" ")
            current=current.next
            
    
    def clear(self):
        self.head=None



    









    



    


