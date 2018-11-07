from Character import Character

class Player(Character):
    def __init__(self, weapon, sprite):
        Character.__init__(self)
        self.weapon = weapon
        self.sprite = sprite 
 
    def shoot(self):
        ##shoots projectile

        atk = self.get_stat('atk')

        return atk  

        ## look for pygames animations // create a seperate function to animate and call it in the shoot method
        ## pygame clock
        ## equation which accounts for speed, and time

    def defend(self):
        #reflect damage from the attacker 
            dfnd = self.get_stat('dfnd')
            dmg = 
        
        ## equation ()
        return defnd status
        #dmg = (hp - defense) / defense


    def set_prop(self, status_key, value):
        self.stats[status_key] += value
    #Updates key property of player with a given value

    def upgrade(self):
        self.level <= 5
        self.level += 1

        set_prop()
    #upgrade: Level 5 is the max level of upgrade. 
    #Level by 1 and set the property depending on the character.




