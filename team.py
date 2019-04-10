#**************************************team class*****************************#
import numpy as np 

class team():
  team_member_ = []
  is_user_team_ = 0
  def __init__(self, team_list, is_user_team):
    self.team_member_ = team_list
    self.is_user_team_ = is_user_team

  def check_team_status(self):
    print(("User " if self.is_user_team_ else "Enemy ") + 
           "Team info:----------------------------------")
    for individual in self.team_member_:
      individual.check_status()
    print("End " + ("User " if self.is_user_team_ else "Enemy ") + 
          "Team info-------------------------------")

  def get_team_member(self):
  	return self.team_member_

  def get_team_attack_info(self):
  	res = np.array([])
  	for individual in self.team_member_:
  		res = np.append(res, [individual.get_attack_info()])
  	return res

  def get_team_health_info(self):
  	res = np.array([])
  	for individual in self.team_member_:
  		res = np.append(res, [individual.get_current_health()])
  	return res

  def team_still_survive(self):
  	res = True
  	for individual in self.team_member_:
  		res = (res and (individual.get_current_health() > 0))
  	return res

  def get_team_survive_list(self):
  	res = np.array([])
  	for individual in self.team_member_:
  		res = np.append(res, [individual.get_current_health() != 0])
  	return res

#**********************************end team class*****************************#
