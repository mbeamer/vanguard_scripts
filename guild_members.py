import re
import sys

def update_members(members, re_sults):
	''' use a match from re to update members dictionary.  Some items are optional, so handle cases where they are missing. '''
	a_member = members[re_sults.group('name')]
	a_member['character_level'] = re_sults.group('character_level')
	a_member['class'] = re_sults.group('class')
	a_member['diplomacy_level'] = re_sults.group('diplomacy_level')
	try:
		a_member['trade_level'] = re_sults.group('trade_level')
		a_member['trade_skill'] = re_sults.group('trade_skill')
	except:
		a_member['trade_level'] = 0
		a_member['trade_skill'] = 'Undecided'

def parse_log(members, input_file):
	''' Parse the input_log and output an updated member_list '''
	
	# Vanguard's /who command reports a well semi-formatted dump.  Two formats are possible, those with Trade skills, and those without.
	# For example:
	#
	# [09:21:50] Khazull: Level 26 Rogue, 1 Diplomat (Stone & Steel) - Tursh Village
	# [09:21:50] Warfeild: Level 24 Paladin, 11 Blacksmith, 13 Diplomat (Stone & Steel) - Three Rivers Village

	# Parse the log looking for /who results.  Store in a tuple of tuples
	# members_list = [<member name>: [character_level: <level>, class: <class>, trade_level: <trade_level>, trade_skill: <trade_skill>, diplomacy_level: <diplomacy_level>], ... ]
	full_who_pattern = re.compile("^\[[0-9]{2}:[0-9]{2}:[0-9]{2}\]\s*(?P<name>\w*):\s*Level\s*(?P<character_level>[0-9]+)\s*(?P<class>\w+),\s*(?P<trade_level>[0-9]+)\s*(?P<trade>\w+),\s*(?P<diplomacy_level>[0-9]+)\s*Diplomat\s*\(Stone\s*\&\s*Steel\)")
	part_who_pattern = re.compile("^\[[0-9]{2}:[0-9]{2}:[0-9]{2}\]\s*(?P<name>\w*):\s*Level\s*(?P<character_level>[0-9]+)\s*(?P<class>\w+),\s*(?P<diplomacy_level>[0-9]+)\s*Diplomat\s*\(Stone\s*\&\s*Steel\)")

	print("\n")
	for	line in open(input_file):
		who_match =  full_who_pattern.match(line)
		if who_match != None:
			update_members(members, who_match)
		else:
			part_who_match = part_who_pattern.match(line)
			if part_who_match != None:
				update_members(members, part_who_match)

def parse_html(members, web_file):
	''' Parse html page to prime the member_list tuple '''
	members['Khazull'] = dict()
	members['Warfeild'] = dict()
	with open (os.path.join(web_file, "members.html"), "r") as webfile:
    		web_string = webfile.read()
	with optn (os.path.join(web_file, "members_parse_template.html"), "r") as templatefile:
		template_string = templatefile.read()
	for match in re.findall(template_string, web_string)
		print("Match\n %s"% re.group(0))
	
def write_html(members):
	''' Pieces back together the html page '''
	pass

def main():
	# Gather user define pieces
	input_file = input("Enter the log name: (../vanguard_log.txt): ")
	if input_file == '':
		input_file = "../vanguard_log.txt"
	output_file = input("Enter the log markup name (%s.yuku): "% input_file)
	web_file = input("web content location (members.html, member_template.txt, etc) (./data/): ")
	if web_file == '':
		web_file = "./data/"
	if output_file == '':
		output_file = "%s.yuku"% input_file

	members = dict()
	parse_html(members, web_file)
	parse_log(members, input_file)
	write_html(members)
	print(members)	
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
