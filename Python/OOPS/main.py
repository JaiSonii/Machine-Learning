class agent:
    
    def __init__(self,name):
        self.name = name
        self.health = 100
        self.damage_dealt = 0
        self.age = 25
        self.alive = True
    
    def info(self):
        print(f"name: {self.name}")
        print(f"damage dealt: {self.damage_dealt}")
        print(f"health: {self.health}")
        print(f"age: {self.age}")
        print(f"Alive: {self.alive}")
 
    def punched(self):
        self.damage_dealt -= 10
        if self.health <= 0:
            self.alive = False
    
    def shot(self):
        self.health -= 50
        if self.health <= 0:
            self.alive = False
    
class boss(agent):
    def __init__(self,name):
        super().__init__(name)
        self.health = 1000 
        self.age = 500  
                  
agent1 = agent("jai")
boss1 = boss("nalla boss")
agent1.shot()
agent1.shot()
agent1.info()