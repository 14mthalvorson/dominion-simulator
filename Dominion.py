import pickle
import random


# Game class represents a single game of Dominion
class Game:
    card_information = {
        'Copper': {'Category':'Treasure', 'Cost': 0, 'Play Order': 0, 'Money': 1},
        'Silver': {'Category': 'Treasure', 'Cost': 3, 'Play Order': 0, 'Money': 2},
        'Gold': {'Category': 'Treasure', 'Cost': 6, 'Play Order': 0, 'Money': 3},
        'Platinum': {'Category': 'Treasure', 'Cost': 9, 'Play Order': 0, 'Money': 5},

        'Estate': {'Category': 'Victory', 'Cost': 2, 'Play Order': -1, 'VP': 1},
        'Duchy': {'Category': 'Victory', 'Cost': 5, 'Play Order': -1, 'VP': 3},
        'Province': {'Category': 'Victory', 'Cost': 8, 'Play Order': -1, 'VP': 6},
        'Colony': {'Category': 'Victory', 'Cost': 11, 'Play Order': -1, 'VP': 10},

        #'Cellar': {'Category': 'Action', 'Cost': 2, 'Play Order': -1, 'Actions': 1},
        #'Moat': {'Category': 'Action', 'Cost': 2, 'Play Order': -1, 'Cards': 2},
        #'Village': {'Category': 'Action', 'Cost': 3, 'Play Order': -1, 'Actions': 2, 'Cards': 1},
        #'Merchant': {'Category': 'Action', 'Cost': 3, 'Play Order': -1, 'Actions': 1, 'Cards': 1},
        #'Workshop': {'Category': 'Action', 'Cost': 3, 'Play Order': -1},
        #'Smithy': {'Category': 'Action', 'Cost': 4, 'Play Order': -1, 'Cards': 3},
        #'Remodel': {'Category': 'Action', 'Cost': 4, 'Play Order': -1, 'Drop': 1},
        #'Militia': {'Category': 'Action', 'Cost': 4, 'Play Order': -1, 'Money': 2},
        #'Market': {'Category': 'Action', 'Cost': 5, 'Play Order': -1, 'Actions': 1, 'Buys': 1, 'Cards': 1, 'Money': 1},
        #'Mine': {'Category': 'Action', 'Cost': 5, 'Play Order': -1}

    }
    max_round = 50

    # Initialize a game, provided a number of players
    def __init__(self, num_players=4, center_pile=None, output=False):

        # Initialize starting center pile
        if center_pile is None:
            self.center_pile = {
                'Copper': 20,
                'Silver': 20,
                'Gold': 20,
                'Platinum': 20,

                'Estate': 20,
                'Duchy': 20,
                'Province': 20,
                'Colony': 20,
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
        random.shuffle(self.player_list)

        # Variable to track round; will change to 1 before the first round
        self.round = 0
        self.first_player = self.player_list[0]
        self.current_player = None
        self.output = output

        # Initialize starting decks for players
        self.initialize_decks()

    def initialize_decks(self):

        starting_deck = {'Copper':7,
                         'Estate':3}

        for player in self.player_list:
            for card_name in starting_deck.keys():
                for i in range(starting_deck.get(card_name)):
                    self.buy_card(player, card_name)
            random.shuffle(player.deck.draw_pile)

    def run(self):
        while self.game_over() is False:
            self.next_turn()

        return self.conclude_game()

    def next_turn(self):
        # Increment self.round at appropriate time
        if self.player_list[0] is self.first_player:
            self.round += 1
            if self.output:
                print('\nRound:', self.round)

        self.current_player = self.player_list.pop(0)
        if self.output:
            print('\nTurn:', self.current_player.name)

        for i in range(5):
            self.current_player.draw_card()

        if self.output:
            print(self.current_player)

        self.action_phase(self.current_player)
        self.buy_phase(self.current_player)

        self.current_player.discard_hand()

        self.player_list.append(self.current_player)

    def game_over(self):
        if self.round == Game.max_round:
            return True
        else:
            return False

    def conclude_game(self):
        if self.output:
            print('\n\nConclusion:')
        max_vp = 0
        max_vp_player = None
        for player in self.player_list:
            total_vp = self.sum_victory_points(player)
            if total_vp > max_vp:
                max_vp = total_vp
                max_vp_player = player

        if self.output:
            print('\nWinner is ' + max_vp_player.name)
            print(max_vp_player.buy_matrix)
        return max_vp_player

    def sum_victory_points(self, player):
        victory_points = 0
        for card in player.deck.draw_pile + player.deck.discard_pile:
            victory_points += card.victory_points
        if self.output:
            print(player.name + ' has ' + str(victory_points) + ' victory points.')
        return victory_points

    def action_phase(self, player):
        for card in player.hand:
            if card.category == 'Action':
                if self.output:
                    print('Playing: ' + card.name)
                return
        if self.output:
            print('Not playing any card')

    def buy_phase(self, player):
        money = 0
        for card in player.hand:
            money += card.money
        if self.output:
            print('Total Money: ' + str(money))

        # Find eligible cards to buy
        eligible_cards = []
        for card_name in self.center_pile.keys():
            if self.center_pile[card_name] > 0 and self.card_information[card_name]['Cost'] <= money:
                eligible_cards.append(card_name)
        if len(eligible_cards) > 0:
            sum_rank = 0
            for card_name in eligible_cards:
                sum_rank += Simulator.aggregate_buy_matrix.matrix[self.round][card_name]

            for card_name in eligible_cards:
                if random.random() * sum_rank < Simulator.aggregate_buy_matrix.matrix[self.round][card_name]:
                    self.buy_card(player, card_name)
                    return
                else:
                    sum_rank -= Simulator.aggregate_buy_matrix.matrix[self.round][card_name]
        else:
            if self.output:
                print('Not buying any card')


    # Buys card from center pile and moves it to Player's discard pile
    def buy_card(self, player, card_name):
        if self.output:
            print('Buying: ' + card_name)

        # Adds tally to Player's buy_matrix
        player.buy_matrix.add_to_matrix(self.round, card_name)

        # Adds card to Player's discard pile
        player.deck.discard_pile.append(Card({card_name: self.card_information.get(card_name)}))

        # Removes one tally from the center pile
        self.center_pile[card_name] = self.center_pile.get(card_name, 1) - 1


# Card_Matrix Class
class CardMatrix:
    def __init__(self, type, player_name, filename=None):

        # type can be 'play', 'buy', or 'drop'
        self.type = type
        self.player_name = player_name

        round_dictionary = {}
        for card_name in Game.card_information.keys():
            round_dictionary[card_name] = 100

        self.matrix = []

        # Check if matrix is already stored in file
        self.matrix = [dict(round_dictionary) for i in range(Game.max_round + 1)]

        self.normalize_matrix()

    def add_to_matrix(self, round, card_name):
        self.matrix[round][card_name] = self.matrix[round].get(card_name, 0) + 1

    def add_another_matrix(self, other):
        for i in range(Game.max_round + 1):
            for card_name in self.matrix[i].keys():
                self.matrix[i][card_name] += other.matrix[i].get(card_name, 0) - (1000 / len(Game.card_information))
        self.normalize_matrix()

    def normalize_matrix(self):
        for round_dict in self.matrix:
            stat_sum = sum(round_dict.values())
            for card_name in round_dict.keys():
                round_dict[card_name] = max(10, int(round_dict[card_name] * 1000 / stat_sum))

    def __str__(self):
        string = '\n' + self.player_name + '\'s ' + self.type + ' Matrix:\n'
        for i in range(1, Game.max_round):
            string += 'Round ' + str(i) + ": " + str(self.matrix[i]) + '\n'
        return string


# Simulator class used to simulated multiple games of Dominion
class Simulator:
    try:
        aggregate_play_matrix = pickle.load(open('play.p', 'rb'))
    except:
        aggregate_play_matrix = CardMatrix('play', 'Aggregate')
    try:
        aggregate_buy_matrix = pickle.load(open('buy.p', 'rb'))
    except:
        aggregate_buy_matrix = CardMatrix('buy', 'Aggregate')
    try:
        aggregate_drop_matrix = pickle.load(open('drop.p', 'rb'))
    except:
        aggregate_drop_matrix = CardMatrix('drop', 'Aggregate')

    def __init__(self, num_players=4):
        self.num_players = num_players

    def run(self, num_games):
        print(self.aggregate_buy_matrix)
        for i in range(num_games):
            g = Game(self.num_players)
            winner = g.run()
            self.aggregate_buy_matrix.add_another_matrix(winner.buy_matrix)

            if (i+1)%100 == 0:
                print("Training Round: ", i+1)

        print(self.aggregate_buy_matrix)
        self.dump_matrices()

    def dump_matrices(self):
        pickle.dump(self.aggregate_play_matrix, open('play.p', 'wb'))
        pickle.dump(self.aggregate_buy_matrix, open('buy.p', 'wb'))
        pickle.dump(self.aggregate_drop_matrix, open('drop.p', 'wb'))

    def reset(self):
        self.aggregate_play_matrix = CardMatrix('play', 'Aggregate')
        self.aggregate_buy_matrix = CardMatrix('buy', 'Aggregate')
        self.aggregate_drop_matrix = CardMatrix('drop', 'Aggregate')

        self.dump_matrices()


# Player class
class Player:
    def __init__(self, name):
        self.name = name
        self.deck = Deck()

        self.action_matrix = CardMatrix('Action', self.name)
        self.buy_matrix = CardMatrix('Buy', self.name)

        self.hand = []

    # Removes card from Player's draw pile and moves to hand
    def draw_card(self):
        if len(self.deck.draw_pile) == 0:
            self.deck.draw_pile = self.deck.discard_pile
            self.deck.discard_pile = []
            random.shuffle(self.deck.draw_pile)
            self.draw_card()
        else:
            self.hand.append(self.deck.draw_pile.pop(0))

    def discard_hand(self):
        while len(self.hand) > 0:
            self.deck.discard_pile.append(self.hand.pop(0))

    # String method for printing Player object
    def __str__(self):
        string = 'Hand: '
        for card in self.hand:
            string += card.name + ' '
        return string


# Deck class used by each Player to represent his/her deck
class Deck:
    def __init__(self):
        self.draw_pile = []
        self.discard_pile = []

    def __str__(self):
        string = 'Deck: '
        for card in self.draw_pile + self.discard_pile:
            string += card.name + ' '


# Card class represents a playing card in Dominion
class Card:
    def __init__(self, card_information):
        self.name = list(card_information.keys())[0]
        self.category = card_information[self.name].get('Category')
        self.cost = card_information[self.name].get('Cost')
        self.play_order = card_information[self.name].get('Play Order')
        self.money = card_information[self.name].get('Money', 0)
        self.victory_points = card_information[self.name].get('VP', 0)