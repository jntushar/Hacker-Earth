/*

Akash and Vishal are quite fond of travelling. They mostly travel by railways. They were travelling in a train one day and they got interested in the seating arrangement of their compartment. The compartment looked something like


So they got interested to know the seat number facing them and the seat type facing them. The seats are denoted as follows :

    Window Seat : WS
    Middle Seat : MS
    Aisle Seat : AS

You will be given a seat number, find out the seat number facing you and the seat type, i.e. WS, MS or AS.

INPUT
First line of input will consist of a single integer T denoting number of test-cases. Each test-case consists of a single integer N denoting the seat-number.

OUTPUT
For each test case, print the facing seat-number and the seat-type, separated by a single space in a new line.

*/


// ---SOLUTION---

    #include<stdio.h>
    int main()
    {
        int n,i,a,b,c,t,m;
        char *s;
        scanf("%d",&t);
        for(i=1;i<=t;i++)
        {
            scanf("%d",&n);
            a=n/6;
            c=n%6;
            if(c!=0)
            b=a+1;
            else
            b=a;
            if(b%2==0)  //even,right,minus
            switch(c)
            {
            case 1: m=n-1; s="WS"; break;
            case 2: m=n-3; s="MS"; break;
            case 3: m=n-5; s="AS"; break;
            case 4: m=n-7; s="AS"; break;
            case 5: m=n-9; s="MS"; break;
            case 0: m=n-11; s="WS"; break;
            }
            
            else  //odd,left,plus
            switch(c)
            {
            case 1: m=n+11; s="WS"; break;
            case 2: m=n+9; s="MS"; break;
            case 3: m=n+7; s="AS"; break;
            case 4: m=n+5; s="AS"; break;
            case 5: m=n+3; s="MS"; break;
            case 0: m=n+1; s="WS"; break;
            }
            printf("%d %s\n",m,s);
        }
        return 0;
    }