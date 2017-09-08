# Simulator class used to simulated multiple games of Dominion
class Simulator:
    aggregate_play_matrix = []
    aggregate_buy_matrix = []

    def __init__(self, num_players):
        self.num_players = num_players

    def simulate(self, num_games):
        for i in range(num_games):
            #TODO


# Game class represents a single game of Dominion
class Game:
    card_information = {
        'Copper': {'Category':'Treasure', 'Cost': 0, 'Play_Order': 0, 'Money': 1},
        'Silver': {'Category': 'Treasure', 'Cost': 3, 'Play_Order': 0, 'Money': 2},
        'Gold': {'Category': 'Treasure', 'Cost': 6, 'Play_Order': 0, 'Money': 3},

        'Estate': {'Category': 'Victory', 'Cost': 2, 'Play_Order': -1, 'VP': 1},
        'Duchy': {'Category': 'Victory', 'Cost': 5, 'Play_Order': -1, 'VP': 3},
        'Province': {'Category': 'Victory', 'Cost': 8, 'Play_Order': -1, 'VP': 6},

        'Cellar': {'Category': 'Action', 'Cost': 2, 'Play_Order': -1, 'Actions': 1},
        'Moat': {'Category': 'Action', 'Cost': 2, 'Play_Order': -1, 'Cards': 2},
        'Village': {'Category': 'Action', 'Cost': 3, 'Play_Order': -1, 'Actions': 2, 'Cards': 1},
        'Merchant': {'Category': 'Action', 'Cost': 3, 'Play_Order': -1, 'Actions': 1, 'Cards': 1},
        'Workshop': {'Category': 'Action', 'Cost': 3, 'Play_Order': -1},
        'Smithy': {'Category': 'Action', 'Cost': 4, 'Play_Order': -1, 'Cards': 3},
        'Remodel': {'Category': 'Action', 'Cost': 4, 'Play_Order': -1, 'Drop': 1},
        'Militia': {'Category': 'Action', 'Cost': 4, 'Play_Order': -1, 'Money': 2},
        'Market': {'Category': 'Action', 'Cost': 5, 'Play_Order': -1, 'Actions': 1, 'Buys': 1, 'Cards': 1, 'Money': 1},
        'Mine': {'Category': 'Action', 'Cost': 5, 'Play_Order': -1}


    }

    def __init__(self, num_players):

        # Initialize player list
        self.num_players = num_players
        self.player_list = []
        for i in range(num_players):
            self.player_list.append(Player())

        self.center_pile = {}


# Player class
class Player:
    def __init__(self):
        self.hand = []
        self.deck = Deck()
        self.play_matrix = []
        self.buy_matrix = []

    # Buys card from center pile and moves it to Player's discard pile
    def buy_card(self, card_name):
        #TODO

    # Removes card from Player's draw pile and moves to hand
    def draw_card




# Deck class used by each Player to represent his/her deck
class Deck:
    def __init__(self):
        self.draw_pile = []
        self.discard_pile = []

    # Initializes each Player's starting deck, based on dictionary passed as argument
    def initialize_deck(self, card_dictionary):
        for card_name in card_dictionary.keys():
            for number in card_dictionary.get(card_name, 0):
                self.draw_pile.append(Card(card_name))
        # shuffle method


# Card class represents a playing card in Dominion
class Card:
    def __init__(self, name, category, cost):
        self.name = name
        self.category = category
        self.cost = cost






















