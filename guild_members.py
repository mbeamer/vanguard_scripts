import re
import sys


def parse_log(member_list, input_file):
	''' Parse the input_log and output an updated member_list '''
	
	# Vanguard's /who command reports a well semi-formatted dump.  Two formats are possible, those with Trade skills, and those without.
	# For example:
	#
	# [09:21:50] Khazull: Level 26 Rogue, 1 Diplomat (Stone & Steel) - Tursh Village
	# [09:21:50] Warfeild: Level 24 Paladin, 11 Blacksmith, 13 Diplomat (Stone & Steel) - Three Rivers Village

	# Parse the log looking for /who results.  Store in a tuple of tuples
	# members_list = [<member name>: [character_level: <level>, class: <class>, trade_level: <trade_level>, trade_skill: <trade_skill>, diplomacy_level: <diplomacy_level>], ... ]
	full_who_pattern = re.compile("^\[[0-9]{2}:[0-9]{2}:[0-9]{2}\]\s*(?P<name>\w*):\s*Level\s*(?P<char_level>[0-9]+)\s*(?P<class>\w+),\s*(?P<trade_level>[0-9]+)\s*(?P<trade>\w+),\s*(?P<dip_level>[0-9]+)\s*Diplomat\s*\(Stone\s*\&\s*Steel\)")
	part_who_pattern = re.compile("^\[[0-9]{2}:[0-9]{2}:[0-9]{2}\]\s*(?P<name>\w*):\s*Level\s*(?P<char_level>[0-9]+)\s*(?P<class>\w+),\s*(?P<dip_level>[0-9]+)\s*Diplomat\s*\(Stone\s*\&\s*Steel\)")

	print("\n")
	for	line in open(input_file):
		who_match =  full_who_pattern.match(line)
		if who_match != None:
			print("Full match found on line: (%s)(%s)"% (who_match.group('name'), who_match.group('char_level')))
			print(who_match.groups())
		else:
			part_who_match = part_who_pattern.match(line)
			if part_who_match != None:
				print("Simple match found on line: (%s)(%s)"% (part_who_match.group('name'), part_who_match.group('char_level')))
				match_tuple = part_who_match.groups()
				
				match_tuple{'trade_level'} = 1
				print(part_who_match.groups())

def parse_html():
	''' Parse html page to prime the member_list tuple '''
	pass
	
def main():
	# Gather user define pieces
	input_file = input("Enter the log name: ")
	output_file = input("Enter the log markup name (%s.yuku)"% input_file)
	if output_file == '':
		output_file = "%s.yuku"% input_file

	member_list = []
	parse_log(member_list, input_file)
	
	print("Done parsing\n")
	
#items = input_file_handle.readline()[10:]

# Split into a list of just item names.
#item_list = items.split(',')

#print("Logging to: %s"% output_file)
#with open(output_file, 'w') as output_file_handle:
#	for item in item_list:
#		item = item.strip()
#		# Sometimes we have multples.  Strip off the count.
#		item_count = item
#		while '(' in item:
#			item = item[:-1]
#		output_file_handle.write("([link=http://vanguard.wikia.com/wiki/%s]wikia[/link] - [link=http://wiki.silkyvenom.com/index.php/%s]silky[/link]) %s\n"% (item.replace(" ", "_"), item.replace(" ", "_"), item_count))
		
if __name__ == '__main__':
	main()