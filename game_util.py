#**************************************game util module************************#
import math

#calculate hearth bar block number
def health_bar_block_num(current_health, full_health):
	if (current_health <= 0):
		return 0
	elif (current_health > full_health):
		return 20
	else:
		pass
	return math.floor(current_health/full_health*20)
#**********************************end game util module************************#