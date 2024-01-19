class Player():
    def __init__(self, name, team, position, points) -> None:
        self.name = name
        self.team = team
        self.position = position
        if points:
            self.points = int(points)
        else:
            self.points = 0

    def add_points(self, points):
        self.points = points

    def get_points(self):
        return self.points
    
    def is_qb(self):
        return self.position == 'QB'
    def is_rb(self):
        return self.position == 'RB'
    def is_wr(self):
        return self.position == 'WR'
    def is_flex(self):
        return self.position == 'FLEX'
