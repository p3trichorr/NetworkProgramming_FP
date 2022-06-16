class Game:
    def __init__(self, id):
        self.p1point = 0
        self.p2point = 0
        self.ready = False
        self.id = id
        self.points = [None, None]
        self.wins = [0,0]
        self.ties = 0

    def get_player_points(self, p):
        return self.points[p]

    def play(self, player, point):
        self.points[player] = int(point)

        if player == 0:
            self.p1point = self.points[player]
        else:
            self.p2point = self.points[player]

    def connected(self):
        return self.ready

    def bothPoint(self):
        return self.p1point and self.p2point

    def winner(self):

        p1 = self.points[0]
        p2 = self.points[1]

        winner = -1
        if p1 == 21:
            winner = 0
        elif p2 == 21:
            winner = 1
        elif p1-21 < p2-21:
            winner = 0
        elif p2-21 <  p1-21:
            winner = 1
            
        return winner

    def resetPoint(self):
        self.p1point = 0
        self.p2point = 0