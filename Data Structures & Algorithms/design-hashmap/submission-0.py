class MyHashMap:

    def __init__(self):
        self.number_buckets = 19997 
        self.table = [[] for _ in range(self.number_buckets)] 

    # Renamed from 'add' to 'put' to match the error message
    def put(self, key: int, value: int) -> None:
        bucket_ind = key % self.number_buckets

        for pair in self.table[bucket_ind]:
            if pair[0] == key:
                pair[1] = value
                return 

        self.table[bucket_ind].append([key, value])

    def remove(self, key: int) -> None:
        bucket_ind = key % self.number_buckets

        for i, pair in enumerate(self.table[bucket_ind]):
            if pair[0] == key:
                self.table[bucket_ind].pop(i)
                return
        

    # Renamed 'get' is already correct in your previous logic
    def get(self, key: int) -> int:
        bucket_ind = key % self.number_buckets
        
        for pair in self.table[bucket_ind]:
            if pair[0] == key:
                return pair[1] 
        
        return -1

# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)