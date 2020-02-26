from doubly_linked_list import DoublyLinkedList


class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.current = None
        self.storage = DoublyLinkedList()

    def append(self, item):
        # if the item is less than capacity, add
        if  self.storage.length < self.capacity:
        #     # invoke the add to tail function from the dll
            self.storage.add_to_tail(item)
        #     # set the new current to head
            self.current = self.storage.head
        #     print('self.current as head', self.current)
            

        elif self.storage.length == self.capacity:
            print('values', self.storage.head)
           
            # if not self.current:
            self.current.value = item

            if self.current is self.storage.tail:
            #     print('self.current.value', self.current.value)
                self.current = self.storage.head
            else:
                self.current = self.current.next
                print('self.current as tail', self.current.next)

        
            
        else:
            self.storage.add_to_head(item)


    def get(self):
        # Note:  This is the only [] allowed
        list_buffer_contents = []

        # TODO: Your code here
        curr = self.storage.head
        if curr is None:
            list_buffer_contents.append(curr.value)

        while curr is not None:
            print('curr value', curr.value)
            list_buffer_contents.append(curr.value)
            # print('self.storage.next', self.current.next)
            # curr = self.current.next
            curr = curr.next
            print('curr.next', curr)
        # list_buffer_contents.append(curr.value)
        return list_buffer_contents