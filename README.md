checkpoint
==========

A key/val store for checkpointing python objects to AWS S3.  The current serialization is pickle.  I'm working on improving everything.

Look how simple:

```python
from Checkpoint import Checkpoint

ch = Checkpoint(bucket='bucketnamehere')

x = [1,2,3,4,5,6, 7]

ch.store('mylist1', x)

y = ch.load('mylist1')

print y

l = ch.list()
for i in l:
  print i.key

```

Setup
=====

Since this is built on top of boto, you should have these two set:
* AWS_ACCESS_KEY_ID 
* AWS_SECRET_ACCESS_KEY 
 
Optionally, you can set your s3 bucket in the environment variable, CHECKPOINT_BUCKET. 

Checkpoint
==========

Our main class, Checkpoint, exposes a simple API to the user that allows them to load and store key/value pairs into s3.  Objects are serialized into s3 via store and deserialized back via load.

Functions
=========

Checkpoint.store(key, obj)
==========================

Stores obj at key in your bucket.  

e.g.

```python
ch.store('mylist1', x)
```

Checkpoint.load(key)
====================

Returns the object stored at key in your bucket.

e.g.
```python
y = ch.load('mylist1')
```

Checkpoint.list()
=================

Returns at interator over the items in your bucket.

e.g.
```python
l = ch.list()
for i in l:
  print i.key
```

