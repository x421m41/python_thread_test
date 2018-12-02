import queue
import time
from worker import BackgroundWorker

data = 0
with BackgroundWorker() as bw:

  while data <= 20:
    data += 1
    time.sleep(0.2)
    print(data)
    bw.submit(data)
    result = bw.take()
    if result:
      print(result)
