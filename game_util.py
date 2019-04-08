#**************************************game util module************************#
import math

#calculate hearth bar block number
def health_bar_block_num(current_health, full_health):
	return math.floor(current_health/full_health*20)
#**********************************end game util module************************#