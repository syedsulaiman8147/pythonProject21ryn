class queue():
    def __init__(self):
        self.queue=[]
    def insert(self):
        data=int(input("enter the numbers"))
        self.queue.append(data)
    def delete(self):
        maxvalue=0
        for i in range(len(self.queue)):
            if self.queue[i]>self.queue[maxvalue]:
                maxvalue=i
        item = self.queue[maxvalue]
        del self.queue[maxvalue]
    print("remove element is")
    print()
    def display(self):
        if len(self.queue)==0:
            print("empty query")
        else:
         for i in self.queue():
                print(i)
q=queue()
while True:
     print('queue operation /n','1.append','2.delete','3.display','4.exit')
     ch=int(input("enter the operation"))
     if ch==1:
         q.insert()
     elif ch==2:
           q.delete()
     elif ch==3:
           q.display()
     elif ch==4:
           break
     else:
        print("invalid input")
