"""
You have been given a String S consisting of uppercase and lowercase English alphabets. You need to change the case of each alphabet in this String. That is, all the uppercase letters should be converted to lowercase and all the lowercase letters should be converted to uppercase. You need to then print the resultant String to output.

Input Format
The first and only line of input contains the String S

Output Format
Print the resultant String on a single line.
"""

"""---SOLUTION---"""

S = input()
N = ''
i = 0
while i < len(S):
    if ord(S[i]) >= 65 and ord(S[i]) <= 90:
        N = N + S[i].lower()
    else:
        N = N + S[i].upper()
    i += 1
print(N)