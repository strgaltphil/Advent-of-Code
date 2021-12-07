class Line:
    def __init__(self, start_x, start_y, end_x, end_y):
        self.start_x = int(start_x)
        self.start_y = int(start_y)
        self.end_x = int(end_x)
        self.end_y = int(end_y)

    def get_start(self):
        return (self.start_x, self.start_y)

    def get_end(self):
        return (self.end_x, self.end_y)

    def get_max_x(self):
        return max(self.start_x, self.start_x)

    def get_max_y(self):
        return max(self.start_y, self.end_y)
    
    def __repr__(self):
        return f"({self.start_x},{self.start_y} -> {self.end_x},{self.end_y})"

    def is_not_vertical(self):
        return self.start_x == self.end_x or self.start_y == self.end_y

    def get_slope(self):
        return int((self.end_y - self.start_y) / (self.end_x - self.start_x))

class Map:
    def __init__(self, dimension_x, dimension_y):
        self.dim_x = int(dimension_x)
        self.dim_y = int(dimension_y)
        self.fields = [0 for _ in range(self.dim_x * self.dim_y)]

    def __repr__(self):
        out_string = ""
        for y in range(self.dim_y):
            out_string = out_string + " ".join(str(f) for f in self.fields[y*self.dim_y:y*self.dim_x+self.dim_x]) + '\n'
        return out_string

    def check(self, line: Line):
        if line.is_not_vertical():
            # toggle x and y if needed. This is only allowed, if x1 == x2 or y1 == y2 is fulfilled -> only allowed for horizontal and vertical lines
            if line.end_x < line.start_x:
                line.end_x, line.start_x = line.start_x, line.end_x

            if line.end_y < line.start_y:
                line.end_y, line.start_y = line.start_y, line.end_y

            for x in range(line.start_x, line.end_x + 1):
                for y in range(line.start_y, line.end_y + 1):
                    self.fields[self.dim2_to_dim1(x, y)] += 1
        else:
            # toggle Points, if x2 < x1 for correct calculation of slope
            if line.start_x > line.end_x:
                line.start_x, line.end_x, line.start_y, line.end_y = line.end_x, line.start_x, line.end_y, line.start_y

            counter = 0
            for x in range(line.start_x, line.end_x + 1):
                self.fields[self.dim2_to_dim1(x, line.start_y + (counter * line.get_slope()))] += 1
                counter += 1            

    def dim2_to_dim1(self, x, y):
        return self.dim_x * y + x

    def get_overlapping_count(self):
        return len([f for f in self.fields if f > 1])

with open('input.txt', 'r') as file:
    data = [line.split(" -> ") for line in file.read().split('\n')]

lines = []

for d in data:
    coords = []
    for l in d:
        coords.extend(l.split(","))
    lines.append(Line(*coords))

# get dimensions for map 
max_x = max([l.get_max_x() for l in lines]) + 1
max_y = max([l.get_max_y() for l in lines]) + 1

map = Map(max_x, max_y)

for line in lines:
    map.check(line)

print(map.get_overlapping_count())
