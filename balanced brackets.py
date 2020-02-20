"""

A bracket is considered to be any one of the following characters: (, ), {, }, [, or ].

Two brackets are considered to be a matched pair if the an opening bracket (i.e., (, [, or {) occurs to the left of a closing bracket (i.e., ), ], or }) of the exact same type. There are three types of matched pairs of brackets: [], {},and ().

A matching pair of brackets is not balanced if the set of brackets it encloses are not matched. For example, {[(])} is not balanced because the contents in between { and } are not balanced. The pair of square brackets encloses a single, unbalanced opening bracket, (, and the pair of parentheses encloses a single, unbalanced closing square bracket, ].

By this logic, we say a sequence of brackets is balanced if the following conditions are met:

It contains no unmatched brackets.
The subset of brackets enclosed within the confines of a matched pair of brackets is also a matched pair of brackets.
Given n strings of brackets, determine whether each sequence of
brackets is balanced. If a string is balanced, return YES. Otherwise, return NO.


INPUT:

The first line contains a single integer n, the number of strings.

Each of the next n lines contains a single string s, a sequence of brackets.

CONSTRAINTS:

1<=n<=10^3
1<=|s|<=10^3, where  is the length of the sequence.
All chracters in the sequences ? { {, }, (, ), [, ] }.

OUTPUT:

For each string, return YES or NO.

"""


"""---SOLUTION---"""


def check(brackets):
    stack = []
    for i in brackets:
        if i in open_list:
            stack.append(i)
        elif i in close_list:
            pos = close_list.index(i)
            if ((len(stack) > 0) and
                    (open_list[pos] == stack[len(stack) - 1])):
                stack.pop()
            else:
                return "NO"
    if len(stack) == 0:
        return "YES"
    else:
        return "NO"


if __name__ == "__main__":
    test_cases = int(input())
    open_list = ["[", "{", "("]
    close_list = ["]", "}", ")"]
    for _ in range(test_cases):
        brackets = input()
        print(check(brackets))