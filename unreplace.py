### m04e/unreplace.py
import unicodedata

# REPLACE this comment with your `fix_line` function

filename = input('What text file would you like to de-emojify? ')
print()   # print a blank line between question and script's output

the_story = ''

with open('txts/' + filename) as my_open_file:
    while True:
        the_line = my_open_file.readline()

        # the_line = fix_line(the_line)
        the_story += the_line

        # Check for EOF
        if the_line == '':
            break

print("\nAnd here's the de-emojified story:\n")
print(the_story, end='')

print("\nThe End.")
