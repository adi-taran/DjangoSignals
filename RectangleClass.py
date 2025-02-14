class Rectangle: 
    def __init__(self, length: int, width: int): 
        
        self.dimensions = {'length': length, 'width': width} 
        self.keys = list(self.dimensions.keys()) 
        self.index = 0

    def __iter__(self): 
        return self

    def __next__(self): 
        if self.index < len(self.keys):
            key = self.keys[self.index]
            value = self.dimensions[key]
            self.index += 1 #increses by 1
            return {key: value}
        raise StopIteration 
    
    def __repr__(self): 
        return f"Rectangle({self.dimensions['length']}, {self.dimensions['width']})"

rectangle_data = Rectangle(14, 31) 
for data in rectangle_data:
    print(data)

print(rectangle_data)
