# define a name-value pair object and how it looks like
class Node:
    """Defines a single node entry key value pair in the dictionary
    manages key value pairs, and keeps them paired up"""

    def __init__(self, key, value=None):
        self.key = key
        self.value = value
        self.hash = hash(self.key)

# if hash of one node is equal as othernode they are the same data
# and that is illegal in dictionaries. Cannot have duplicate keys.
# Hash Collision
    def __eq__(self, otherNode):
        return self.hash == otherNode.hash

# want it to be able to print itself when we're debugging. For humans.
# representation
    def __repr__(self):
        return f'{self.__class__.__name__}: k={self.key} v={self.value}'


# when you create a dictionary you need to tell it how many buckets its
# going to have. This creates the 10 empty buckets. then we can address
# then via the hash for each one.
class KashDict:
    def __init__(self, num_buckets=10):
        self.size = num_buckets
        self.buckets = [[] for _ in range(self.size)]

# to get a nice view of our dictionary
    def __repr__(self):
        return '\n'.join([f'{self.__class__.__name__}.{i}:{bucket}'
                         for i, bucket in enumerate(self.buckets)])

    def add(self, key, value=None):
        new_node = Node(key, value)
        # the bucket we are going to put the new node
        index = new_node.hash % self.size
        bucket = self.buckets[index]
        # but we need to check for a hash collision

        for node in bucket:
            if node == new_node:
                print('Removing duplication key')
                bucket.remove(node)
                break
        bucket.append(new_node)
    # put the new node into its bucket

    # to pull stuff out
    def get(self, key):
        node_to_find = Node(key)
        index = node_to_find.hash % self.size
        bucket = self.buckets[index]
        for node in bucket:
            if node_to_find == node:
                return node.value
        raise KeyError('That is not in my Dictionary, go make your own')
    
# square bracket indexing into the dictionary. adds d.get('kash'..) to ['kash']

    def __getitem__(self, key):
        return self.get(key)

# square bracket indexing into the dictionary. adds d.add(key value pair) to d[key]= value
    def __setitem__(self, key, value):
        return self.add(key, value)
