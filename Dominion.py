# Card_Matrix Class
class CardMatrix:
    def __init__(self, type):

        # type can be 'play', 'buy', or 'drop'
        self.type = type


# Simulator class used to simulated multiple games of Dominion
class Simulator:
    aggregate_play_matrix = CardMatrix('play')
    aggregate_buy_matrix = CardMatrix('buy')
    aggregate_drop_matrix = CardMatrix('drop')

    def __init__(self, num_players):
        self.num_players = num_players

    def simulate(self, num_games):
        for i in range(num_games):
            g = Game(4)
            g.run()
            g.get_winners()


class TestThis:
    def __init__(self):
        print('print this')

    def test_return(self):
        return 'hello'


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
    def __init__(self, num_players=4, center_pile=None):

        # Initialize starting center pile
        if center_pile is None:
            self.center_pile = {
                'Copper': 10,
                'Silver': 10,
                'Gold': 10,

                'Estate': 10,
                'Duchy': 10,
                'Province': 10
            }

            '''
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
            '''

        # Initialize player list
        self.player_list = []
        for i in range(num_players):
            self.player_list.append(Player('Player' + str(i + 1)))
        # Shuffle player list here

        # Variable to track round; will change to 1 before the first round
        self.round = 0
        self.first_player = self.player_list[0]
        self.current_player = None

    def run(self):
        while self.game_over() is False:
            self.next_turn()

    def next_turn(self):
        # Increment self.round at appropriate time
        if self.player_list[0] is self.first_player:
            self.round += 1
            print('\nRound:', self.round)

        self.current_player = self.player_list.pop(0)
        print('Turn:', self.current_player.name)

        self.player_list.append(self.current_player)

    def game_over(self):
        if self.round == 10:
            return True
        else:
            return False

    def get_winners(self):
        pass


# Player class
class Player:
    def __init__(self, name):
        self.name = name
        self.deck = Deck()

        self.play_matrix = []
        self.buy_matrix = []

        self.hand = []

    # Buys card from center pile and moves it to Player's discard pile
    def buy_card(self, card_name):
        pass

    # Removes card from Player's draw pile and moves to hand
    def draw_card(self):
        pass


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
