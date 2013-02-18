'''
A simple checkpointing system whose store is s3. Built on top of boto.
'''

import os
import boto
from boto.s3.key import Key
import pickle

class Checkpoint:
  def __init__(self, bucket=None, access_key=None,secret_key=None):
    if bucket is not None:
      self.bucket = bucket
    else:
      self.bucket = os.getenv('CHECKPOINT_BUCKET')
      if self.bucket is None:
        raise Exception('No bucket')
    if access_key is not None:
      self.access_key = access_key
    else:
      self.access_key = os.getenv('AWS_ACCESS_KEY_ID')
      if self.access_key is None:
        raise Exception('No access key')
    if secret_key is not None:
      self.secret_key = secret_key
    else:
      self.secret_key = os.getenv('AWS_SECRET_ACCESS_KEY')
      if self.secret_key is None:
        raise Exception('No secret key')
  
  def store(self, key, obj):
    conn = boto.connect_s3(self.access_key, self.secret_key)
    bucket = conn.get_bucket(self.bucket)
    k = Key(bucket)
    k.key = key
    k.set_contents_from_string(pickle.dumps(obj))
    conn.close()

  def load(self, key):
    conn = boto.connect_s3(self.access_key, self.secret_key)
    bucket = conn.get_bucket(self.bucket)
    k = Key(bucket)
    k.key = key
    o = pickle.loads(k.get_contents_as_string())
    conn.close()
    return o

  def list(self):
    conn = boto.connect_s3(self.access_key, self.secret_key)
    bucket = conn.get_bucket(self.bucket)
    o = bucket.list() 
    conn.close()
    return o

