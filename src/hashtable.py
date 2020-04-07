# '''
# Linked List hash table key/value pair
# '''


class LinkedPair:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None

    def __repr__(self):
        return f"<{self.key}, {self.value}>"

    def set_next(self, new_next):
        self.next = new_next


class LinkedList:
    def __init__(self, head=None):
        self.head = head

    def insert(self, key, value):
        new_node = LinkedPair(key, value)
        new_node.set_next(self.head)
        self.head = new_node

    def search(self, key):
        current = self.head
        found = False

        while current and found is False:
            if current.key == key:
                found = True
            else:
                current = current.next
        if current is None:
            return False
        return current


class HashTable:
    '''
    A hash table that with `capacity` buckets
    that accepts string keys
    '''

    def __init__(self, capacity):
        self.capacity = capacity  # Number of buckets in the hash table
        self.storage = [None] * capacity

    def _hash(self, key):
        '''
        Hash an arbitrary key and return an integer.

        You may replace the Python hash with DJB2 as a stretch goal.
        '''
        return hash(key)

    def _hash_djb2(self, key):
        '''
        Hash an arbitrary key using DJB2 hash

        OPTIONAL STRETCH: Research and implement DJB2
        '''
        pass

    def _hash_mod(self, key):
        '''
        Take an arbitrary key and return a valid integer index
        within the storage capacity of the hash table.
        '''
        return self._hash(key) % self.capacity

    def insert(self, key, value):
        '''
        Store the value with the given key.
        # Part 1: Hash collisions should be handled with an error warning. (Think about and
        # investigate the impact this will have on the tests)
        # Part 2: Change this so that hash collisions are handled with Linked List Chaining.
        Fill this in.
        '''
        # Hashmod the key to find the bucket
        index = self._hash_mod(key)

        if self.storage[index] == None:
            self.storage[index] = LinkedList()
            self.storage[index].insert(key, value)
        else:
            node = self.storage[index].search(key)
            if node:
                node.value = value
            else:
                self.storage[index].insert(key, value)
        ''' # Check if a pair already exists in the bucket
        pair = self.storage[bucket]
        if pair is not None:
            # If so, overwrite the key/value and throw  a warning
            if pair.key != key:
                print("Warning: Overwriting value")
                pair.key = key
            pair.value = value
        else:
            # If not, Creat a new LinkedPair and place it in the bucket
        '''

    def remove(self, key):
        '''
        Remove the value stored with the given key.

        Print a warning if the key is not found.

        Fill this in.
        '''
        # Get the index from hashmod
        index = self._hash_mod(key)
        # Check if a pair exists in the bucket with matchin keys
        if self.storage[index] is not None and self.storage[index].key == key:
            # If so, return the value
            self.storage[index] = None
        else:
            raise ValueError("Key is not found.")

    def retrieve(self, key):
        '''
        Retrieve the value stored with the given key.

        Returns None if the key is not found.

        Fill this in.
        '''
        # Get the index from hashmod
        index = self._hash_mod(key)

        # Check if a pair exists in the bucket with matchin keys
        if self.storage[index] is not None and self.storage[index].key == key:
            # If so, return the value
            return self.storage[index].value
        else:
            # Else return None
            return None

    def resize(self):
        '''
        Doubles the capacity of the hash table and
        rehash all key/value pairs.

        Fill this in.
        '''
        self.capacity = self.capacity * 2
        new_hash_table = HashTable(self.capacity)

        for i in range(len(self.storage)):
            if self.storage[i] is not None:
                current_node = self.storage[i].head
                while current_node:
                    new_hash_table.insert(current_node.key, current_node.value)
                    current_node = current_node.next
        self.storage = new_hash_table.storage
        new_hash_table = None


if __name__ == "__main__":
    ht = HashTable(2)

    ht.insert("line_1", "Tiny hash table")
    ht.insert("line_2", "Filled beyond capacity")
    ht.insert("line_3", "Linked list saves the day!")

    print("")

    # Test storing beyond capacity
    print(ht.retrieve("line_1"))
    print(ht.retrieve("line_2"))
    print(ht.retrieve("line_3"))

    # Test resizing
    old_capacity = len(ht.storage)
    ht.resize()
    new_capacity = len(ht.storage)

    print(f"\nResized from {old_capacity} to {new_capacity}.\n")

    # Test if data intact after resizing
    print(ht.retrieve("line_1"))
    print(ht.retrieve("line_2"))
    print(ht.retrieve("line_3"))

    print("")
