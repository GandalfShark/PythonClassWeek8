"""
Create a Python script that will meet the constraints below:
I. The program should run continuously until the user chooses to “quit”:#done
II. The program must perform an HTTP GET request to a website #done
III. The program must access JSON data from the website #done
IV. The program needs to include at least 1 user-generated module #done

"""
# 	https://api.funtranslations.com/translate/dothraki.json
#   short fun program using the above API, assignment above

import usermod
# as per instructions

def pr_blue(blue):
    print("\033[94m {}\033[00m" .format(blue))

pr_blue("""

English to Dothraki 

   ,~~_
   |/\ =_ _ ~
    _( )_( )\~~
    \,\  _|\ \~~~
       \`   \\
    `    `
    
Translation Program 

""")

while True:
    to_be_translated = input('What would you like to say in Dothraki?\n> ')
    usermod.doth_trans(to_be_translated)
    # the imported module to make the api call being passed the input
    quitYN = input('Go again?\n').strip().lower()
    if quitYN in ['n', 'q', 'no', 'nope', 'quit', 'nah', 'exit', 'die']:
        break
    # check if the user wants to quit, unless no or nope program loops

pr_blue('Jinak nakho - end of program')
# Dothraki do not have a word for 'thank you'
# the above Dothraki means: this is the end

