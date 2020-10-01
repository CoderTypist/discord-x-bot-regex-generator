#!/usr/bin/env python3

# english characters and possible subsitutions people may use
subs = { 'a' : '[aA@]',
         'b' : '[bB8]',
         'c' : '[cC]',
         'd' : '[dD]',
         'e' : '[eE3]',
         'f' : '[fF]',
         'g' : '[g69]',
         'h' : '[hH]',
         'i' : '[iI1!\\|l]',
         'j' : '[jJ]',
         'k' : '[kK]',
         'l' : '[lL]',
         'm' : '[mM]',
         'n' : '[nN]',
         'o' : '[oO0]',
         'p' : '[pP]',
         'q' : '[qQ]',
         'r' : '[rR]',
         's' : '[sS$5]',
         't' : '[tT7]',
         'u' : '[uU]',
         'v' : '[vV]',
         'w' : '[wW]',
         'x' : '[xX]',
         'y' : '[yY]',
         'z' : '[zZ]' }

with open ('words.txt', 'r') as infile:
    
    # list of regular expressions used to ban specific words
    rules = []
    
    # word to be banned
    word = infile.readline().strip()

    # read each word in words.txt
    while word:
        
        # match with anything before the word
        regex = '.*'

        for i in range(len(word)):
            
            # make the current letter lowercase
            c = word[i].lower()

            # if the letter is in the hash map, add a list of similar characters to the regular expression
            # match with one or more occurencies of the character found
            if subs.get(c):
                regex = regex + subs[c] + '+'
            
            # if the letter is not in the hash, append it to the regular expression as is
            else:
                regex = regex + c + '+'
        
        # match with anything after the word
        regex = regex + '.*'

        # add the newly constructed regular expression to the list of regular expressions
        rules.append(regex)

        # read the next line
        word = infile.readline().strip()

    # the x.regex command for x-bot with a leading \b
    command = 'x.regex \\b'

    # how to match with any word from a list of words in regex
    command = command + '\\b|\\b'.join(rules)

    # the trailing \b
    command = command + '\\b'

    # output the newly created regular expression
    print(command)
