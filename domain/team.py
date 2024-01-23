class Team():
    def __init__(self, name) -> None:
        #  Initialize some values
        self.name = name
        self.rbs = []
        self.wrs = []
        self.points_for = 0
        self.projected_points = 0
        self.wins = 0
        self.losses = 0
        self.ties = 0

    # Helper methods for filling out roster
    def set_qb(self, qb):
        self.qb = qb
        self.projected_points += qb.get_points()
    def add_rb(self, rb):
        self.rbs.append(rb)
        self.projected_points += rb.get_points()
    def add_wr(self, wr):
        self.wrs.append(wr)
        self.projected_points += wr.get_points()
    def set_flex(self, flex):
        self.flex = flex
        self.projected_points += flex.get_points()
    
    def get_weekly_score(self):
        return self.projected_points // 15
        
    # Could store head to head for tie breaking, but in fantasy we do points for.

    def win(self, points):
        self.wins+=1
        self.points_for += points
    def lose(self, points):
        self.losses+=1
        self.points_for += points
    def tie(self, points):
        self.ties+=1
        self.points_for += points
    def get_record(self):
        return [self.wins, self.losses, self.ties, self.points_for]
    
    def print_roster(self):
        return ("Team " + str(self.name) + "\nQB: " + self.qb.name + "\n"
        + "RBs: " + self.rbs[0].name + " & " + self.rbs[1].name + "\n"
        + "WRs: " + self.wrs[0].name + " & " + self.wrs[1].name + "\n"
        + "Flex: " + self.flex.name)