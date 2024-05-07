class Mylist:
    def __init__(self, list):
        self.list=list
    def append(self,a):
         self.list.append(a) 
         return self.list
    def count(self, b):
        if b in self.list:
           return self.list.count(b)
        else:
            return 0
    def join(self):
        return '-'.join(map(lambda x: str(x), self.list))
    def pop(self):
        return self.list.pop(), self.list  

list1=Mylist([1,2,3])
print(list1.append(2))
print(list1.count(4))
print(list1.join())
print(list1.pop())

