class Dog:
    species = 'canine'
    count = 0

    def __init__(self, name, prev, next):
        self.name = name
        self.prev = prev
        self.next = next
        Dog.count += 1

d = Dog('fido', 'rover', 'chev')

print d.next
print d.prev
print d.name
print "how many dogs: " + str(Dog.count)

anotherdog = Dog('bree', 'fido', 'rover')

print anotherdog.name
print "how many dogs: " + str(Dog.count)
