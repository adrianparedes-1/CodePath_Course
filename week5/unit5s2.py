#1 
'''
understand:
write a method that takes an object and uses the damage parameter to decrease the opponent's hp
We will be priniting out whether 2 different responses depending on the hp and dmg values.

plan:
1. check if hp is zero after the opponent was attacked. If that's the case then print "opponent fainted".
    otherwise, print the amount of damage dealt to the opponent.

'''

class Pokemon():
	def  __init__(self, name, hp, damage):
		self.name = name
		self.hp = hp # hit points
		self.damage = damage # The amount of damage this pokemon does to its opponent every attack
		
	def attack(self, opponent):
		if opponent.hp - self.damage <= 0:
			print(f"{opponent.name} fainted.")
		else:
			print(f"{self.name} dealt {self.damage} damage to {opponent.name}")
	
pikachu = Pokemon("Pikachu", 35, 20)
bulbasaur = Pokemon("Bulbasaur", 45, 30) 

opponent = bulbasaur
pikachu.attack(opponent)


#2

