#**************************************combat class***************************#
import team
import numpy as np

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
		while (self.team1_.team_still_survive() and self.team2_.team_still_survive()):
			self.check_combat_info()
			print ("Round: ", self.round)
			self.__user_action()
			self.round += 1

	def get_enemy_list(self):
		names = []
		for i in range(len(self.team2_.get_team_survive_list())):
			if (self.team2_.get_team_survive_list()[i] != 0):
				names.append(self.team2_.get_team_member()[i].get_name())
		print (list(zip([x + 1 for x in range((int)(np.sum(self.team2_.get_team_survive_list())))], names)))

  #private function that we do not want to use by client
	def __user_action(self):
		for individual in self.team1_.get_team_member():
			print("who will {} attack?".format(individual.get_name()))
			self.get_enemy_list()
			target = (int)(input("Enter index of enemy: ")) - 1
			self.team2_.get_team_member()[target].take_damage(1000)
			if (not self.team2_.team_still_survive()):
				print ("Enemy team is defeated!");
				return




#**********************************end combat class***************************#