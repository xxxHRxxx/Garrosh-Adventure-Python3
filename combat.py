#**************************************combat class***************************#
import team

class combat:
	round = 1
	def __init__(self, team1, team2):
		self.team1_ = team1
		self.team2_ = team2

	def check_combat_info(self):
		print("There is a combat between:\n")
		self.team1_.check_team_status()
		print("\nand\n")
		self.team2_.check_team_status()
		
#**********************************end combat class***************************#