#!/usr/bin/python3
#
# japanese_tokenizer.py - adding space between Japanese words
# Author: <Ines Simbi>(inessimbi@bennington.edu)
# Date: <03.13.2019>
#

import sys
#from tokenize import tokenize
input_file = sys.argv[1]
output_file = sys.argv[2]


def tokenize(line, japanese_text_dict):
	the_list = [] # list to save items when word boundary is found
	#while loop to go through the line and check if word found in line exists in japanese dictionary
	i = 0
	while (i < len(line)): # gets item from line
		if line[i] in japanese_text_dict: # statement to check if item in line is in japanese_text_dict
			the_list.append(line[i]) # adds item in list by appending it to the_list
			#print(the_list)

		else:
			start_index = i # holds the value of the current index that wasn't found in the dictionary
			current_char = line[i] # holds value of the current character not found in dictionary
			found = False
			while (i < (len (line)-1) and (not found)): #loop to add next character to the previous character if not found in the dictionary
				current_char = current_char + line[i+1]
				if current_char in japanese_text_dict:
					the_list.append(current_char) #appends group of characters when found to be a word and appends to the list
					found = True
				else:
					i = i+1
			if not found: # if the index is not found in the dictionary
				i= start_index
				the_list.append(line[i]) # the character at index i is going to be treated as its own word
				i = i + 1 # increments index i to the next index and start going in the while loop
	the_string = ' '.join(the_list) # joins items in a list by space
	return the_string



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
			#print(line)
			the_line = tokenize(line, japanese_text_dict)
			open_out.write(the_line) # prints results in out_file





