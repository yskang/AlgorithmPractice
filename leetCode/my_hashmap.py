# Title: Design Hashmap
# Link: https://leetcode.com/problems/design-hashmap/submissions/

class MyHashMap:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.size = 10000
        self.table = [[] for _ in range(self.size)]

    def put(self, key: int, value: int) -> None:
        """
        value will always be non-negative.
        """
        hash_value = key % self.size
        for i, [k, v] in enumerate(self.table[hash_value]):
            if k == key:
                self.table[hash_value][i][1] = value
                break
        else:
            self.table[hash_value].append([key, value])

    def get(self, key: int) -> int:
        """
        Returns the value to which the specified key is mapped, or -1 if this map contains no mapping for the key
        """
        hash_value = key % self.size

        for k, v in self.table[hash_value]:
            if k == key:
                return v
        return -1            
        

    def remove(self, key: int) -> None:
        """
        Removes the mapping of the specified value key if this map contains a mapping for the key
        """
        hash_value = key % self.size
        for i, [k, v] in enumerate(self.table[hash_value]):
            if k == key:
                self.table[hash_value] = self.table[hash_value][:i] + self.table[hash_value][i+1:]

# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)


def solution():
    my_hashmap = MyHashMap()
    my_hashmap.put(1, 1)
    my_hashmap.put(2, 2)
    my_hashmap.get(1)
    my_hashmap.get(3)
    my_hashmap.put(2, 1)
    my_hashmap.get(2)
    my_hashmap.remove(2)
    my_hashmap.get(2)


def main():
    print(solution())


if __name__ == '__main__':
    main()