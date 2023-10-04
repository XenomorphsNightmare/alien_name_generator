import json 

class Alien_names:
    def __init__(self, Alien_builder):
        self.first_name = Alien_builder.first_name
        self.second_name = Alien_builder.second_name
        self.third_name = Alien_builder.third_name
    



class Alien_builder:
    def __init__(self):
        self.first_name = None
        self.second_name = None
        self.third_name = None

    def get_first_name(self,first_name):
        self.first_name = first_name
        return self
    
    def get_second_name(self,second_name):
        self.second_name = second_name
        return self
    
    def get_third_name(self,third_name):
        self.third_name = third_name
        return self 
    
    def build(self):
        return Alien_names(self)
    


class Director:
    def __init__(self, builder):
        self.builder = builder
        self.data = {}

    def build_alien(self, first_name, second_name, third_name):
        return self.builder.get_first_name(first_name).get_second_name(second_name).get_third_name(third_name).build()
    




