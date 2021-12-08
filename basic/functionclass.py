class Computer(object):
    def __init__(self , model , color ,company, processer , RAM ) :
        self.model = model
        self.color = color
        self.company = company
        self.processer = processer
        self.RAM = RAM
        
  
            
hp = Computer("hp omen 15" , "black and red" , "hp" , "Intel(R) Core(TM) i7" , "24gb")
print(hp.model)
print(hp.color)
print(hp.processer)
print(hp.RAM)
print(hp.company)
            
        
            
        