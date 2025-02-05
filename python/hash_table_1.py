# for each hash map theres a different hash function, for this case our hash 
# function is using with ASCII table, the key - turned into sum of ASCII
# chars for each letter, total size of arr and the value.

class HashTable:
  def __init__(self):
    self.MAX = 100
    self.arr = [None for i in range(self.MAX)]
    
  def get_hash(self, key):
    h = 0
    for char in key:
      h += ord(char)
    return h % self.MAX

  def __setitem__(self, key, value):
    h = self.get_hash(key)
    self.arr[h] = value
  
  def __getitem__(self, key):
    h = self.get_hash(key)
    return self.arr[h]

  def __del__(self, key):
    h = self.get_hash(key)
    self.arr[h] = None

t = HashTable()
t['march 6'] = 50
t['dec 6'] = 2000
print(t.arr)