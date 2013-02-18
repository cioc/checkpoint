checkpoint
==========

A key/val store for checkpointing python objects to AWS S3.  The current serialization is pickle.  I'm working on improving everything.

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

Checkpoint.store
================

Checkpoint.load
===============

Checkpoint.list
===============

