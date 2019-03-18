#!/usr/bin/python3
#
# clean_and_count_tokens.py - Counting words i a file
# Author: <Ines Simbi>(inessimbi@bennington.edu)
# Date: <03.13.2019>
#

import sys
#from tokenize import tokenize
#input_file = sys.argv[1]
#output_file = sys.argv[2]


def tokenize (line, japanese_text_dict):
	the_list = [] # list to save words when word boundary is found
	#while loop to go through the line and check if word found in line exists in japanese dictionary
	the_string= ""
	i = 0
	while (i< len(line)):
		if line[i] in japanese_text_dict:
			the_list.append(line[i])
		else:
			current_char = line[i]
			found = False
			while (i < len (line) and (not found)):
				current_char = current_char + line[i+1]
				if current_char in japanese_text_dict:
					the_list.append(current_char)
					found = True
				else:
					i = i+1
	the_string = the_string.join(the_list)
	open_out.write(the_string)


in_file= "in.txt"
out_file = "out_file.txt"
dict_file = "japanese_wordlist.txt"



japanese_text_dict = []
with open(dict_file, 'r', encoding='utf-8') as read_in:
	japanese_text_dict = read_in.readlines()
	#print(japanese_text_dict[0])

with open(in_file, 'r', encoding='utf-8') as open_in:
	with open(out_file, 'w', encoding='utf-8') as open_out:
		for line in open_in.readlines():
			print(line)
			the_line = tokenize(line, japanese_text_dict)





