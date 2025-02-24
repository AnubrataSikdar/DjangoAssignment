# Python class Rectangle that meets the requirements:

class Rectangle:
    def __init__(self, length: int, width: int):
        # Initialize the rectangle with length and width
        self.length = length
        self.width = width

    def __iter__(self):
        # Return an iterator that yields the 'length' and 'width' in the required format
        yield {'length': self.length}
        yield {'width': self.width}

# Example Usage:
rect = Rectangle(5, 10)

# Iterating over the Rectangle instance
for item in rect:
    print(item)


#Output:
#{'length': 5}
#{'width': 10}
