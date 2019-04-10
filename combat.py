#**************************************combat class***************************#
import team
import numpy as np

#combat class
class combat:
	round = 1
	def __init__(self, team1, team2):
		self.team1_ = team1
		self.team2_ = team2
		self.team1_survive_list_ = self.team1_.get_team_survive_list()
		self.team2_survive_list_ = self.team2_.get_team_survive_list()

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
			if (self.round == 2):
				break
			self.round += 1

	def get_enemy_list(self):
		names = []
		for i in range(len(self.team2_survive_list_)):
			if (self.team2_survive_list_[i] != 0):
				names.append(self.team2_.get_team_member()[i].get_name())
		print (list(zip([x + 1 for x in range((int)(np.sum(self.team2_survive_list_)))], names)))

	def __user_action(self):
		for individual in self.team1_.get_team_member():
			print("who will {} attack?".format(individual.get_name()))
			self.get_enemy_list()
			target = (int)(input("Enter index of enemy: ")) - 1
			self.team2_.get_team_member()[target].set_new_health(-50)




#**********************************end combat class***************************#