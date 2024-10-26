#1 
'''
understand:
write a method that takes an object and uses the damage parameter to decrease the opponent's hp
We will be printing out whether 2 different responses depending on the hp and dmg values.

plan:
1. check if hp is zero after the opponent was attacked. If that's the case then print "opponent fainted".
    otherwise, print the amount of damage dealt to the opponent.

'''

# class Pokemon():
# 	def  __init__(self, name, hp, damage):
# 		self.name = name
# 		self.hp = hp # hit points
# 		self.damage = damage # The amount of damage this pokemon does to its opponent every attack
		
# 	def attack(self, opponent):
# 		if opponent.hp - self.damage <= 0:
# 			print(f"{opponent.name} fainted.")
# 		else:
# 			print(f"{self.name} dealt {self.damage} damage to {opponent.name}")
	
# pikachu = Pokemon("Pikachu", 35, 20)
# bulbasaur = Pokemon("Bulbasaur", 45, 30) 

# opponent = bulbasaur
# pikachu.attack(opponent)



'''
2. 
understand: write a method that will take a list and turn it into a linked list.

plan:
1. create 2 nodes
2. connect them

3. 

understand: write a function that takes a head in the linked list and a new node and make new node the head in the linked list

plan:
1. set the first element to point to jigglypuff. All we need to do is change the pointer.
2. return the first element to update the function call
'''
# class Node:
# 	def __init__(self, value, next=None):
# 		self.value = value
# 		self.next = next
	
# # Creating the nodes
# node_1 = Node("Jigglypuff")
# node_2 = Node("Wigglytuff")

# def add_first(head, new_node):
# 	new_node.next = head
# 	return new_node

# # Linking node_1 to node_2
# node_1.next = node_2

# # print(node_1.value, "->", node_1.next.value)
# # print(node_2.value, "->", node_2.next)

# print(node_1.value, "->", node_1.next.value)

# new_node = Node("Ditto")
# node_1 = add_first(node_1, new_node)

# print(node_1.value, "->", node_1.next.value)



#4

'''
understand ---
write a function that takes the head of a linked list and returns the tail.

input: head of linked list
output: print the value of the tail. Tail being the last element in the linked list
constraints: no constraints
edge cases: list is empty
example: [1,2,3] --> pass 1, return 3

plan:

Iterate through the linked list so we can determine which value is the tail.
Tail would be the last value, meaning next = None

1. To iterate through the linked list, we could initialize a variable current and assign the head to it.
2. we can use a while loop that iterates continues to loop until current.next = None
3. check which value has next = None
4. return that value

edge case: if the head is none --> return None. We could check this before we start looping.
'''

# class Node:
# 	def __init__(self, value, next=None):
# 		self.value = value
# 		self.next = next

# def get_tail(head):
# 	current = head
# 	# print(current.value)
# 	if current is None:
# 		return None
# 	while current != None:
# 		if current.next == None:
# 			return current
# 		current = current.next

# num1 = Node("num1")
# num2 = Node("num2")
# num3 = Node("num3")
# num1.next = num2
# num2.next = num3


# head = num1
# tail = get_tail(num1)
# print(tail.value)



#5

'''
understand ---

write a function that replaces the original value with the replacement value. This function takes in three paremeters:
head, original, and replacement

input: head, original, replacement
output: updated version of the linked list with the replacement completed
constraints: none
edge: if the linked list is empty, return None

plan ---

1. if original is not in the linked list, we can return None
2. initialize variable called current to head
3. iterate through the linked list while the current value is not None. Increment current.
4. once we reach the "original" element in the linked list, then replace it with "replacement"
5. once we are done iterating, then return the linked list

'''
class Node:
	def __init__(self, value, next=None):
		self.value = value
		self.next = next
		
def ll_replace(head, original, replacement):
	current = head
	while current is not None: #None would be the end of the list
		if current.value == original: #if the current value is the value we want to change
			current.value = replacement #update the current value with the replacement
		current = current.next # increment current to go to the next node
	return current # we are updating the function call with the updated value


num3 = Node(5)
num2 = Node(6, num3)
num1 = Node(5, num2)
# initial linked list: 5 -> 6 -> 5

head = num1
def print_ll(head):
	current = head
	while current is not None:
		print(f"{current.value}")
		current = current.next

ll_replace(head, 5, "banana")
print_ll(head)
