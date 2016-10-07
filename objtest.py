class Dog:
    species = 'canine'
    count = 0

    def __init__(self, name, prev, next):
        self.hasteeth = "yes"
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

print d.hasteeth

def fun():
    Dog.species = 'wolf'
    d.name = 'doggie'   # Unlike global vars, it seems global objects can be modified inside functions without specifying them as global.

print "species: " + Dog.species
print "dname: " + d.name
fun()
print "species: " + Dog.species
print "dname: " + d.name

# And now for something completely different. 
print "vtag, atag".rpartition(',')[2].strip()


# And now for something completely different. 
cat = 'media'
categories = {}
categories[cat] = {}
categories[cat]['video'] = 'video'
print categories

# And now for something completely different. 
a = b = "asdf"
print a
print b
