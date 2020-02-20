/*

Harry is a bright student. To prepare thoroughly for exams, he completes all the exercises in his book! Now that the exams are approaching fast, he is doing book exercises day and night. He writes down and keeps updating the remaining number of exercises on the back cover of each book.
Harry has a lot of books messed on the floor. Therefore, he wants to pile up the books that still have some remaining exercises into a single pile. He will grab the books one-by-one and add the books that still have remaining exercises to the top of the pile.
Whenever he wants to do a book exercise, he will pick the book with the minimum number of remaining exercises from the pile. In order to pick the book, he has to remove all the books above it. Therefore, if there are more than one books with the minimum number of remaining exercises, he will take the one which requires the least number of books to remove. The removed books are returned to the messy floor. After he picks the book, he will do all the remaining exercises and trash the book.
Since number of books is rather large, he needs your help to tell him the number of books he must remove, for picking the book with the minimum number of exercises.
Note that more than one book can have the same name.

Input Format
The first line contains a single integer N denoting the number of actions. Then N lines follow. Each line starts with an integer. If the integer is -1, that means Harry wants to do a book exercise. Otherwise, the integer is number of the remaining exercises in the book he grabs next. This is followed by a string denoting the name of the book.

Output Format
For each -1 in the input, output a single line containing the number of books Harry must remove, followed by the name of the book that Harry must pick.

*/

// ---SOLUTION---


#include<iostream>
#include<string>
#include<stack>
using namespace std;
 
struct book
{
int ex;
string name;
};
 
void printMin(stack<book*>& s, stack<book*>& sMin) {
int count = 0;
while(s.top() != sMin.top())
{
    s.pop();
    sMin.pop();
    count++;
}
cout << count << " " << s.top() ->name << endl;
s.pop();
sMin.pop();
}
 
int main()
{
    
    stack<book*> s, sMin;
    int n;
    cin >> n;
    while(n--){
        book *b = new book;
        cin >>b->ex;
        if(b->ex==-1){
            printMin(s,sMin);
        }
        else{
            cin >> b->name;
            if(b->ex != 0) {
                s.push(b);
                if(!sMin.empty() && sMin.top()->ex >= b->ex)
                {
                    sMin.push(b);
                }
                else if(sMin.empty()){
                    sMin.push(b);
                }
                else{
                    sMin.push(sMin.top());
                }
            }
        }
    }
    return 0;
}

