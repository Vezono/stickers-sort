import redis
import random
import hashlib
import time
r = redis.Redis()
  
def set_salt():
  global r
  salt = generate_salt()
  r.mset({'salt': salt})
  
def generate_salt():
  tth = str(time.time()).encode()
  h = hashlib.sha1(tth).hexdigest()
  return h[:20]

while True:
  time.sleep(random.randint(180, 1800))
  set_salt()
