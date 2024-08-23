class Human:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.say_info()
        
    def say_info(self):
        print(f"Привет, меня зовут {self.name}, мне {self.age}")  
        
    def birthday(self):
        self.age += 1
        print(f"У меня день рождения, мне теперь {self.age}")
    
    def __str__(self):
        return f'{self.name}'
        
    def __len__(self):
        return self.age
    
    def __lt__(self, other):
        return self.age < other.age
    
    def __gt__(self, other):
        return self.age > other.age
    
    def __eq__(self, other):
        return self.name == other.name and self.age == other.age #Если имена и возраст равны?
        
    def __boolP__(self):
        return self.age
        
    # def __del__(self):
    #     print(f'{self.name} ушел')
        
den = Human("Денис", 22)
max = Human("Макс", 22)

a = 6
print(den)
# if den:
#     den.say_info()
#print(den < max)
#print(den > max)
#max.birthday()
#print(den < max)
#print(den > max)
print(max == den)

# print(den.name, den.age) 

# den.age = 22 