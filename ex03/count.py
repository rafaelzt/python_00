# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    count.py                                           :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: rzamolo- <rzamolo-@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2023/04/11 17:23:21 by rzamolo-          #+#    #+#              #
#    Updated: 2023/04/18 10:52:37 by rzamolo-         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import sys

punctuation = "!#$%&'()\"*+,-./:;<=>?@[\\]^_`{|}~"

def text_analyzer(argument = None):
    '''
    This function counts the number of upper characters, lower characters,
    punctuation and spaces in a given text.
    '''
    try:
        punct = 0
        upper = 0
        lower = 0
        space = 0

        if argument == None:
            print("What is the text to analyse?")
            argument = input()

        if not(isinstance(argument, str)):
            print("The argument is not a string.")
            return
            
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
    except TypeError as te:
        print("You should enter only one argument.")
        
    
if __name__ == "__main__":
    if (len(sys.argv) == 2):
        text_analyzer(''.join(sys.argv[1]))
    else:
        print("Error")
        

