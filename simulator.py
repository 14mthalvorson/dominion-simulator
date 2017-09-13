# Simulator class used to simulated multiple games of Dominion
class Simulator:
    aggregate_play_matrix = []
    aggregate_buy_matrix = []

    def __init__(self, num_players):
        self.num_players = num_players

    def simulate(self, num_games):
        for i in range(num_games):
            g = Game(4)
            winners = g.winners
            # Add matrices


# Game class represents a single game of Dominion
class Game:
    card_information = {
        'Copper': {'Category':'Treasure', 'Cost': 0, 'Play_Order': 0, 'Money': 1},
        'Silver': {'Category': 'Treasure', 'Cost': 3, 'Play_Order': 0, 'Money': 2},
        'Gold': {'Category': 'Treasure', 'Cost': 6, 'Play_Order': 0, 'Money': 3},

        'Estate': {'Category': 'Victory', 'Cost': 2, 'Play_Order': -1, 'VP': 1},
        'Duchy': {'Category': 'Victory', 'Cost': 5, 'Play_Order': -1, 'VP': 3},
        'Province': {'Category': 'Victory', 'Cost': 8, 'Play_Order': -1, 'VP': 6}

        #'Cellar': {'Category': 'Action', 'Cost': 2, 'Play_Order': -1, 'Actions': 1},
        #'Moat': {'Category': 'Action', 'Cost': 2, 'Play_Order': -1, 'Cards': 2},
        #'Village': {'Category': 'Action', 'Cost': 3, 'Play_Order': -1, 'Actions': 2, 'Cards': 1},
        #'Merchant': {'Category': 'Action', 'Cost': 3, 'Play_Order': -1, 'Actions': 1, 'Cards': 1},
        #'Workshop': {'Category': 'Action', 'Cost': 3, 'Play_Order': -1},
        #'Smithy': {'Category': 'Action', 'Cost': 4, 'Play_Order': -1, 'Cards': 3},
        #'Remodel': {'Category': 'Action', 'Cost': 4, 'Play_Order': -1, 'Drop': 1},
        #'Militia': {'Category': 'Action', 'Cost': 4, 'Play_Order': -1, 'Money': 2},
        #'Market': {'Category': 'Action', 'Cost': 5, 'Play_Order': -1, 'Actions': 1, 'Buys': 1, 'Cards': 1, 'Money': 1},
        #'Mine': {'Category': 'Action', 'Cost': 5, 'Play_Order': -1}
    }

    # Initialize a game, provided a number of players
    def __init__(self, num_players, center_pile={}):

        # Initialize starting center pile
        if len(center_pile) == 0:
            self.center_pile = {
                'Copper': 10,
                'Silver': 10,
                'Gold': 10,

                'Estate': 10,
                'Duchy': 10,
                'Province': 10,

                'Cellar': 10,
                'Moat': 10,
                'Village': 10,
                'Merchant': 10,
                'Workshop': 10,
                'Smithy': 10,
                'Remodel': 10,
                'Militia': 10,
                'Market': 10,
                'Mine': 10
            }

        # Initialize player list
        self.num_players = num_players
        self.player_list = []
        for i in range(num_players):
            self.player_list.append(Player())
        # Shuffle player list here

        # Variable to track round
        self.round = 1

    def next_turn(self):
            


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


# Card_Matrix Class
class Card_Matrix:
    def __init__(self, type):

        # type can be 'play', 'buy', or 'drop'
        self.type = type






















