"""
Arpasland has surrounded by attackers. A truck enters the city. The driver claims the load is food and medicine from Iranians. Ali is one of the soldiers in Arpasland. He doubts about the truck, maybe it's from the siege. He knows that a tag is valid if the sum of every two consecutive digits of it is even and its letter is not a vowel. Determine if the tag of the truck is valid or not.

We consider the letters "A","E","I","O","U","Y" to be vowels for this problem.

Input Format

The first line contains a string of length 9. The format is "DDXDDD-DD", where D stands for a digit (non zero) and X is an uppercase english letter.

Output Format

Print "valid" (without quotes) if the tag is valid, print "invalid" otherwise (without quotes)

"""

"""---SOLUTION---"""

tag = input()
li = ['A', 'E', 'I', 'O', 'U', 'Y']
chk1 = int(tag[0]) + int(tag[1])
chk2 = int(tag[3]) + int(tag[4])
chk3 = int(tag[4]) + int(tag[5])
chk4 = int(tag[7]) + int(tag[8])

if tag[2] in li:
    print('invalid')
elif chk1 % 2 == 0 and chk2 % 2 == 0 and chk3 % 2 == 0 and chk4 % 2 == 0:
    print('valid')
else:
    print('invalid')