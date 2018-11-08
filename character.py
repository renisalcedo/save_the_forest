class Chagit racter:
    def __init__(self, status, level, name, hp, power, speed, cost, defense): 
        self.status = {'hp':hp, 'power':power, 'speed':speed, 'cost':cost, 'defense':defense}
        self.level = level
        self.name = name
  # properties and  method                      
    def get_status(self, status_key):
        return self.status[status_key]
    
    def recieve_damage(self, dmg)
        self.status['hp'] -= dmg
                       gl
                       
                       
        alive = true
                       
                       
                       
        
        if self.status['hp'] <= 0:
        return              alive = false 
      
        
        if self.status ['hp'] => 0:
        return
# creating parameters for status --> hp, power, speed, cost, defense 