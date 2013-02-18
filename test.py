from Checkpoint import Checkpoint

ch = Checkpoint(bucket='bucketnamehere')

x = [1,2,3,4,5,6, 7]

ch.store('mylist1', x)

y = ch.load('mylist1')

print y

l = ch.list()
for i in l:
  print i.key


