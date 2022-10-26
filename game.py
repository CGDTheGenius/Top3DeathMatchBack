class Player:
    def __init__(self, name):
        self.name = name
        self.point = 100
        self.wins = 0
        self.bettings = []
        self.betting = None

    def make_bet(self, value):
        if self.point + (self.betting or 0) - value < 0:
            raise ValueError('Point cannot be negative')
        if self.betting:
            self.point += self.betting
        self.betting = value
        self.point -= self.betting

    def make_round(self, win):
        self.bettings.append(self.betting)
        self.betting = None
        self.wins += win

    @property
    def status(self):
        return {
            'name': self.name,
            'point': self.point,
            'wins': self.wins,
            'bettings': self.bettings,
            'betting': self.betting,
        }


class Game:
    def __init__(self, name1, name2):
        self.players = [Player(name1), Player(name2)]
        self.round = 1
        self.first = 0
        self.last_winner = None

    def make_bet(self, player_index, value):
        self.players[player_index].make_bet(value)

    def make_round(self):
        b0 = self.players[0].betting
        b1 = self.players[1].betting
        if b0 is None or b1 is None:
            raise ValueError('Bettings are not completed.')
        self.players[0].make_round(b0 > b1)
        self.players[1].make_round(b0 < b1)
        self.round += 1
        if b0 > b1:
            self.first = 0
            self.last_winner = 0
        elif b0 < b1:
            self.first = 1
            self.last_winner = 1
        else:
            self.first = 1 - self.first
            self.last_winner = -1
        return self.last_winner

    @property
    def status(self):
        return {
            'players': [
                self.players[0].status,
                self.players[1].status,
            ],
            'round': self.round,
            'first': self.first,
            'last_winner': self.last_winner,
        }

    def more(self, value):
        for player in self.players:
            player.point += value
