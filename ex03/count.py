# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    count.py                                           :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: rzamolo- <rzamolo-@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2023/04/11 17:23:21 by rzamolo-          #+#    #+#              #
#    Updated: 2023/04/11 18:50:11 by rzamolo-         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import sys

punctuation = [',', '.', ':', ';', '!', '?', '"'
				, "'", '-', '(', ')', '[', ']', '{', '}']

def text_analyzer(argument = sys.argv[1:]):
	'''
	This function counts the number of upper characters, lower characters,
	punctuation and spaces in a given text.
	'''
	punct = 0
	upper = 0
	lower = 0
	space = 0

	if len(argument) == 0:
		print("What is the text to analyse?")
		argument = input()
	print(argument)
	for letter in argument:
		if letter.isupper():
			upper += 1
		elif letter.islower():
			lower += 1
		elif letter.isspace():
			space += 1
		elif letter in punctuation:
			punct += 1
		
	print("The text contains", len(argument), "character(s):")
	print("-", upper, "upper letter(s)")
	print("-", lower, "lower letter(s)")
	print("-", punct, "punctuation mark(s)")
	print("-", space, "space(s)")
	
if __name__ == "__main__":
	text_analyzer(''.join(sys.argv[1:]))