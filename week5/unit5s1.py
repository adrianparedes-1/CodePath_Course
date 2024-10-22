#3

'''
understand: update previous code to change property  is_caught from false to true. Print the output.

Plan: Update the squirtle instance so that is_caught is set to True. 

'''

# class Pokemon:
#     def __init__(self, name, types):
#         self.name = name
#         self.types = types
#         self.is_caught = True

#     def print_pokemon(self):
#         print({
#             "name": self.name,   # Output: "name": "Squirtle",
#             "types": self.types, # Output: "types": ["Water"],
#             "is_caught": self.is_caught # Output: "is_caught": False
#         })

# squirtle = Pokemon("Squirtle", ["Water"])
# squirtle.print_pokemon()

#6

'''
understand: update the pokemon class with a new method that updates the Pokemon's list of types with a string.

plan:
add a string to the types parameter of the class

'''

# class Pokemon:
#     def __init__(self, name, types):
#         self.name = name
#         self.types = types
#         self.is_caught = True

#     def print_pokemon(self):
#         print({
#             "name": self.name,   # Output: "name": "Squirtle",
#             "types": self.types, # Output: "types": ["Water"],
#             "is_caught": self.is_caught # Output: "is_caught": False
#         })

#     def add_type(self, new_type):
#         self.types.append(new_type)

# jigglypuff = Pokemon("Jigglypuff", ["Normal"])
# jigglypuff.print_pokemon()

# jigglypuff.add_type("Fairy")
# jigglypuff.print_pokemon()


#Problem Set 2


'''
1.
Step 1: Copy the following code into Replit.

Step 2: Instantiate an instance of the class Card and store it in a variable named card. The Card object should have the suit "Spades" and the rank "8".

2.
Step 1: Update the Card class with the new method print_card() provided below:

def print_card(self):
	print(f"{self.rank} of {self.suit}")
Step 2: Create an instance of the class and store it in a variable named card. The object should have suit "Clubs" and rank "Ace".

Step 3: Then, call the method print_card() on your card.

Expected Output: Ace of Clubs

3. 

Step 1: Using the same Card class from Problem 2, update your code so that the suit of card is "Hearts" instead of "Clubs".

Step 2: Use the print_card() method to verify that card was updated.

Expected Output: Ace of Hearts

4. 
Update the Card class with a new method is_valid() that takes in no parameters except self. The method should return True if:

The suit is one of the following values: "Hearts", "Spades", "Clubs", "Diamonds"
The rank is one of the following values: "2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King", "Ace"
Otherwise, the method should return False

understand: write a method that returns true if the suit and rank have certain values.

plan: we could create a list of the acceptable values for suit and rank, then iterate through the list to see if the value matches one in the list


5.
Update the Card class with a new method get_value() that takes in no parameters except self.

The function returns the card's value depending on the card's rank:

If the card has rank 2, 3, 4, 5, 6, 7, 8, 9, 10, the method should return the rank as an integer
If the card has rank Ace, the method should return 1 as the card's value
If the card has rank Jack, the method should return 11 as the card's value
If the card has rank Queen, the method should return 12 as the card's value
If the card has rank King, the method should return 13 as the card's value
If the card is invalid, the method should return None


'''

class Card():
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank
    
    def is_valid(self):
        suits_lst = ["Hearts", "Spades", "Clubs", "Diamonds"]
        ranks_lst = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King", "Ace"]

        if self.suit in suits_lst and self.rank in ranks_lst:
            return True
        else:
            return False

    def get_value(self):
        
        '''
        if self.rank != "Jack" or "Queen" or "King":

        You were trying to say "if the rank is not Jack, Queen, or King," 
        but what Python understood was "if the rank is not Jack, or if Queen exists, or if King exists" 
        (and Queen and King always exist as strings). This caused Python to always think the condition 
        was true and try to convert something like "Jack" to a number, which caused the error.
        
        '''
        if self.rank not in ["Jack", "Queen", "King"]:
            return int(self.rank)
        elif self.rank == "Jack":
            return 11
        elif self.rank == "Queen":
            return 12
        elif self.rank == "King":
            return 13
        else:
            return None

    def print_card(self):
        print(f"{self.rank} of {self.suit}")


# card = Card("Spades", "8")
# Card.print_card(card)
# card2 = Card("Hearts", "Ace")
# Card.print_card(card2)

# my_card = Card("Hearts", "7")
# print(my_card.is_valid())

# second_draw = Card("Spades", "Joker")
# print(second_draw.is_valid())


# card = Card("Hearts", "7")
# print(card.get_value())

# card_two = Card("Spades", "Jack")
# print(card_two.get_value())



#6

'''
understand: write a method that will add a card to the player's hand and another one that will remove a card from the player's hand

input: card
output: updated hand with new card or removed card
constraints: to remove a card, there must be card in the hand. to add a card there must be a card in Card.
examples: card_one = Card("Hearts", "3")
          card_two = Card("Spades", "8")

player1_hand = Hand()
# cards = []

player1_hand.add_card(card_one)
# cards = [card_one]

player1_hand.add_card(card_two)
# cards = [card_one, card_two]

player1_hand.remove_card(card_one)
# cards = [card_two]

plan:

add method: we will add a card to self.cards from Card
how will we add a card from card

remove method: we will remove a card from self.cards


'''

class Hand:
    def __init__(self):
        self.cards = []
    
    def remove_card(self, card):
        self.cards.remove(card)
    
    def add_card(self, card):
        self.cards.append(card)  
    
    def print_cards(self):
        for card in self.cards:
            card.print_card()
    
card_one = Card("Hearts", "3")
card_two = Card("Spades", "8")

player1_hand = Hand()
# cards = []

player1_hand.add_card(card_one)
player1_hand.print_cards()
# cards = [card_one]

player1_hand.add_card(card_two)
player1_hand.print_cards()
# cards = [card_one, card_two]

player1_hand.remove_card(card_one)
player1_hand.print_cards()
# cards = [card_two]