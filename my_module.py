class Array:
    def __init__(self) -> None:
        self.variable = []

    def __str__(self):
        return f"{self.variable}"

    def append(self, value):
        self.variable += [value]
        return self.variable

    def remove(self, value):
        for i in range(len(self.variable)):
            if self.variable[i] == value:
                del self.variable[i]
                break
            
    def insert(self, index, value):
        first_variable = self.variable[:index]
        second_variable = self.variable[index:]
        self.variable = first_variable + [value] + second_variable
        return self.variable

    def pop(self, index=-1):
        del self.variable[index]
        return self.variable
    
    def clear(self):
        self.variable = []
        return self.variable
    
