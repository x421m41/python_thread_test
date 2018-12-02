from concurrent.futures import ThreadPoolExecutor
from queue import Queue
import time

class BackgroundWorker(object):

  def __init__(self):
    self.__executor = ThreadPoolExecutor()
    self.__result_queue = Queue()

  def __enter__(self):
    return self
  
  def __exit__(self, exc_type, exc_value, traceback):
    if self.__executor is not None:
      self.__executor.shutdown()
      print('executor shutdown')
    else:
      print('executor is not initialized')

  def submit(self, data):
    future = self.__executor.submit(self.__process, data)
    future.add_done_callback(self.__process_done)

  def take(self):
    if not self.__result_queue.empty():
      return self.__result_queue.get()
    else:
      return ''

  def __process(self, data):
    time.sleep(1)
    return 'result: %s' % data

  def __process_done(self, future):
    self.__result_queue.put(future.result())

