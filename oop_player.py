# 플레이어 생성함수
# 그 함수가 생성한 플레이어의 팀 안에 해당 플레이어의 리스트를 추가
class player:
    def __init__(self, name, age, xp):
        # property 적을때 = 주의 : 아님
        self.name = name
        self.age = age
        self.xp = xp
        
 
    def introduce(self):
        print(f"{self.name} player is {self.age} years old")

class team:
    def __init__(self):
        # self.team_name = team_name
        self.players = []

    def add_player(self,name):
        # new_player = Player(name,self.team_name)
        self.players.append(name)

    def show_players(self):
        # for 변수 in 객체(문자열,리스트,튜플,딕셔너리)
        for player in self.players:
          #여기서 Player의 introducer 가능한 이유는???? 
          player.introduce()

    def remove_player(self,name):
        self.players.remove(name)
    
    def total_xp(self):
    # 이코드 이해 안됨
        total_xp = sum([player.xp for player in self.players])
        
        # total_xp = 0
        # for player in self.players:
        # total_xp += player.xp # 여기서 바로 Player의 xp가 접근 가능한 이유는?
    
        print(f"The total xp of all players is {total_xp}")
        
# team_blue = Team("Blue")
# team_blue.add_player("lenn")
# team_blue.show_players()
# team_blue.total_xp()

# team_red = Team("Red")
# team_red.add_player("kay")
# team_red.show_players()


# create players
lenn = player('lenn', 20, 150)
kay = player('kay', 40, 300)

# create teams
team_x = team()
team_x.add_player(lenn)
team_x.add_player(kay)

# show players and total XPs
team_x.show_players()
team_x.total_xp()

# delete MJ and show all players
team_x.remove_player(lenn)
team_x.show_players()

team_x.total_xp()

