"""
File: boggle.py
Name: Tina Tsai
----------------------------------------
TODO:
"""

import time
import numpy as np
import re

# This is the file name of the dictionary txt file
# we will be checking if a word exists by searching through it
FILE = 'dictionary.txt'



def main():
	"""
	TODO:
	"""

	row_num = 0
	# read in dictionary.txt
	word_d = {}

	# Allow user to input 4 rows of 4 characters and stack into an array
	while row_num < 4:
		row_num += 1
		row = str(input(f"{row_num} row of letters:"))
		if re.match(r'[A-Za-z]\s[A-Za-z]\s[A-Za-z]\s[A-Za-z]', row) is None:
			print("Illegal input!")
			break
		else:
			row = row.lower().split()
			if row_num == 1:
				word_array = np.array([row])
			else:
				word_array = np.vstack([word_array, row])
	#
	start = time.time()   
	read_dictionary(word_d)
	boggle(word_array, word_d)
	end = time.time()
	print('----------------------------------')
	print(f'The speed of your boggle algorithm: {end - start} seconds.')


def boggle(word_array, word_d):
	rows = word_array.shape[0]
	cols = word_array.shape[1]
	check_list=[]  # 避免重複搜尋，需設座標list
	words = []
	for row in range(rows):  # 兩組for loop需分開只有找字開始需要進入recursive
		for col in range(cols):
			boggle_helper('', word_array, word_d, words, row, col, check_list)
	print("There are", len(words), "word(s) in total.")  # 4.需print出有多少單字


def boggle_helper(cur_word, word_array, word_d, found_word, row, col, check_list):
	if len(cur_word) >= 4 and cur_word not in found_word and cur_word in word_d[cur_word[0]]:
		print(f"Found {cur_word}")
		found_word.append(cur_word)
	# else: 如room, roomy都是存在的單字，如果用if else擇一執行，roomy就不會被搜尋到
		# loop through the 8 neighbours
	for i in range(-1,2):
		for j in range(-1,2):
			# skip the neighbours that are out of boundaries
			if 0 <= row+i < 4 and 0 <= col+j < 4 and (row,col) not in check_list:   # 6. 0也需要加入
				# choose
				cur_word += word_array[row][col]
				check_list.append((row, col))  # 7.check_list與cur_word一樣需要choose與un-choose
				if has_prefix(cur_word, word_d):
					# explore
					boggle_helper(cur_word, word_array, word_d, found_word, row+i, col+j, check_list)
				# un-choose
				cur_word = cur_word[:-1]
				check_list.pop()


def read_dictionary(word_d):
	"""
	This function reads file "dictionary.txt" stored in FILE
	and appends words in each line into a Python list
	"""

	with open(FILE, 'r') as f:
		for line in f:
			word = line.strip()
			if word[0] not in word_d:
				word_d[word[0]] = [word]
			else:
				# print(word_d[word[0]])
				word_d[word[0]].append(word)


def has_prefix(sub_s, word_d):
	"""
	:param sub_s: (str) A substring that is constructed by neighboring letters on a 4x4 square grid
	:return: (bool) If there is any words with prefix stored in sub_s
	"""
	for word in word_d[sub_s[0]]:
		if word.startswith(sub_s):
			return True
	return False


if __name__ == '__main__':
	main()
