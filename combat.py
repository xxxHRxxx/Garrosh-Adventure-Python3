#**************************************combat class***************************#
import team

#combat class
class combat:
	round = 1
	def __init__(self, team1, team2):
		self.team1_ = team1
		self.team2_ = team2

  #print out deatiled combat infomartion
	def check_combat_info(self):
		print("There is a combat between:\n")
		self.team1_.check_team_status()
		print("\nand\n")
		self.team2_.check_team_status()

  #function that control the whole combat process
	def combat_start(self):
		print (self.team1_.get_team_health_info())
		print (self.team2_.get_team_health_info())
		self.__single_team_attack(self.team1_, self.team2_)

  #want to make this function private
	def __single_team_attack(self, team1, team2):
		print (team.np.sum(self.team1_.get_team_attack_info()))
		print (team.np.sum(self.team2_.get_team_attack_info()))
#**********************************end combat class***************************#