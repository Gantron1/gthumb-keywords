class Dog:

    def __init__(self, name, prev, next):
        self.name = name
        self.prev = prev
        self.next = next

d = Dog('fido', 'rover', 'chev')

print d.next
print d.prev
print d.name
