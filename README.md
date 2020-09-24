# discord-x-bot-regex-generator

x-bot is discord bot that deletes messages that match a provided regular expression. 

A complex regular expression can be used to ban a list of select words. 

regex.py generates a regular expression based on a list of words.

## How to use

Place the words you want to ban in words.txt and run the following command:

./regex.py

The output will be the command x-bot command along with the regular expression.

The regular expression accounts for common character substitutions and repeated characters within the word.

## Example

Trying to ban ['apple', 'banana', 'cherry', 'grape', 'lemon', 'orange', 'peach', 'watermelon'] results in the following x-bot command and regular expression:

x.regex \b.\*[aA@]+[pP]+[pP]+[lL]+[eE3]+.\*\b|\b.\*[bB8]+[aA@]+[nN]+[aA@]+[nN]+[aA@]+.\*\b|\b.\*[cC]+[hH]+[eE3]+[rR]+[rR]+[yY]+.\*\b|\b.\*[g69]+[rR]+[aA@]+[pP]+[eE3]+.\*\b|\b.\*[lL]+[eE3]+[mM]+[oO0]+[nN]+.\*\b|\b.\*[oO0]+[rR]+[aA@]+[nN]+[g69]+[eE3]+.\*\b|\b.\*[pP]+[eE3]+[aA@]+[cC]+[hH]+.\*\b|\b.\*[pP]+[eE3]+[aA@]+[rR]+.\*\b|\b.\*[wW]+[aA@]+[tT7]+[eE3]+[rR]+[mM]+[eE3]+[lL]+[oO0]+[nN]+.\*\b
