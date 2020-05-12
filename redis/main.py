import redis
import random
import hashlib
import time
import os
import urllib.parse as urlparse

redis_url = os.getenv('REDISTOGO_URL')
urlparse.uses_netloc.append('redis')
url = urlparse.urlparse(redis_url)
r = redis.Redis(host=url.hostname, port=url.port, db=0, password=url.password)
  
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
