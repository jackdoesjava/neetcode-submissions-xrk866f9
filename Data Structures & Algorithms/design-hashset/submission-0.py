class MyHashSet:

    def __init__(self):
        self.number_buckets = 19997 # width of hashtable
        # create a list by putting an empty list in each slot
        # _ (throwaway variable)
        self.table= [[] for _ in range(self.number_buckets)] 

    def add(self, key: int) -> None:
        bucket_ind = key % self.number_buckets

        if key not in self.table[bucket_ind]:
            self.table[bucket_ind].append(key)

    def remove(self, key: int) -> None:
        bucket_ind = key % self.number_buckets
        
        if key in self.table[bucket_ind]:
            self.table[bucket_ind].remove(key)
        

    def contains(self, key: int) -> bool:
        bucket_ind = key % self.number_buckets

        return key in self.table[bucket_ind]
# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)