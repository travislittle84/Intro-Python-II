class Item:
    def __init__(self, name, disc_type, max_distance, description):
        self.name = name
        self.disc_type = disc_type 
        self.max_distance = max_distance
        self.description = description
    def __str__(self):
        return f'{self.name}  {self.disc_type} {self.max_distance}'   

