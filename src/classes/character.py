class Status:
    def __init__(self, health, atk, spd, dfnd):
        self.stats =  {'health': health, 'atk':atk, 'spd':spd, 'dfnd':dfnd}
 
    def stat_assign(self, stat, val): 
        self.stats[stat] += val  

    def get_status(self, status_key):
       return self.stats[status_key]

# character will inherit from the status 
class Character(Status):
    def __init__(self, level, name, cost, health=250, spd=5, dfnd=5, atk=5): 
        Status.__init__(self, health, atk, spd, dfnd)
        self.level = level
        self.name = name
              
    def recieve_damage(self, dmg):
        defense = self.stats['dfnd']
        dmg -= defense

        self.stats['health'] -= dmg
        
        return self.get_status('health') <= 0