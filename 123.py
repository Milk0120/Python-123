節點實現
class Node(object):
    def __init__(self,item):
        #item用来存放数据
        self.item = item
        #next是下一个节点的标识
        self.next = None
單鏈表實現
class SingleLinkList(object):
    def __init__(self,node = None):
        self._head = node

    def is_empty(self):
        return self._head == None

    def length(self):
        cur = self._head
        count = 0
        while cur != None:
            count += 1
            cur = cur.next
        return count

    def travel(self): #遍历链表
        cur = self._head
        while cur != None:
            print(cur.item)
            cur = cur.next
頭部添加
 def add(self,item): #头部添加
        #先创建一个保存item的节点
        node =  Node(item)
        #将新节点的链接域next指向头结点，即_head指向的位置
        node.next = self._head
        #将链表的头_head指向新的节点
        self._head = node
尾部添加
 def append(self,item): #尾部添加
        node = Node(item)
        #先判断链表是否为空，若是空链表，则将_head指向新的节点
        if self.is_empty():
            self._head = node
        #若不为空，则找到尾部，将尾部节点的next指向新的节点
        else:
            cur = self._head
            while cur.next != None:
                cur = cur.next
            cur.next = node
任意位置添加
    def insert(self,pos,item): #任意位置添加
        #若指定位置pos为第一个元素，则执行头部文件插入
        if pos <= 0:
            self.add(item)
        #若指定位置超过链表尾部，则执行插入尾部
        elif pos > (self.length()-1):
            self.append(item)
        #找到指定位置
        else:
            node = Node(item)
            count = 0
            #pre用来指向指定位置pos的前一个位置pos-1，初始节点开始移动到指定位置
            pre = self._head
            while count < (pos-1):
                count += 1
                pre = pre.next
            # 先将新节点node的next指向插入位置的节点
            node.next = pre.next
            #将插入的位置的前一个节点的next指向新节点
            pre.next = node
刪除節點
 def remove(self,item):
        cur = self._head
        pre = None
        while cur != None:
            #找到了指定元素
            if cur.item == item:
                #如果第一个就是要删除的节点
                if not pre:
                    #将头指针指向头结点的后一个节点
                    self._head = cur.next
                else:
                    #将删除位置的前一个节点的next指向删除位置的后一个节点
                    pre.next = cur.next
                break
            else:
                #继续按链表后移节点
                pre = cur
                cur = cur.next
查找節點
    def search(self,item):
        cur = self._head
        while cur != None:
            if cur.item == item:
                return True
            cur = cur.next
        return False
測試節點
if __name__ == "__main__":
    ll = SingleLinkList()
    ll.add(1)
    ll.add(2)
    ll.append(3)
    ll.insert(2,4)
    print("length:",ll.length())
    ll.travel()
    print(ll.search(3))
    print(ll.search(5))
    ll.remove(1)
    print("length:",ll.length())
    ll.travel()
