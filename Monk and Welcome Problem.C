/*
Having a good previous year, Monk is back to teach algorithms and data structures. This year he welcomes the learners with a problem which he calls "Welcome Problem". The problem gives you two arrays A and B (each array of size N) and asks to print new array C such that:
;


Now, Monk will proceed further when you solve this one. So, go on and solve it :)

Input:
First line consists of an integer N, denoting the size of A and B.
Next line consists of N space separated integers denoting the array A.
Next line consists of N space separated integers denoting the array B.

Output:
Print N space separated integers denoting the array C.

*/

// ---SOLUTION---


#include<stdio.h>
     
int main()
{
        int A[100001],B[100001],C[100001],n,i;
        scanf("%d",&n);
        for(i=0;i<n;i++)
            scanf("%d",&A[i]);
        for(i=0;i<n;i++)
            scanf("%d",&B[i]);
        for(i=0;i<n;i++)
            C[i] = A[i] + B[i];
        for(i=0;i<n;i++)
            printf("%d ",C[i]);
        return 0;
}