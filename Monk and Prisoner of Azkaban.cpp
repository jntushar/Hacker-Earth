/*

Monk's wizard friend Harry Potter is excited to see his Dad fight Dementors
and rescue him and his Godfather Sirius Black. Meanwhile their friend Hermoine is stuck on some silly arrays
problem. Harry does not have time for all this,
so he asked Monk to solve that problem for Hermoine, so that they can go.

*/

// ---SOLUTION---


    #include <bits/stdc++.h>
     
    using namespace std;
     
    #define mkp make_pair
    #define pb push_back
    #define scan(x) scanf("%lld", &x)
    #define ll long long int
    #define MOD 1000000007
    #define pii pair<int, int>
     
    stack <ll> st;
    ll front[1000001], back[1000001], arr[1000001];
     
    int main()
    {
    	ll n, i, x;
    	scan(n);
    	for (i = 1; i <= n; ++i) {
    	    scan(arr[i]);
    	}
    	
    	for (i = 1; i <= n; ++i) {
    	    if (st.empty() || arr[st.top()] >= arr[i]) {
    	        st.push(i);
    	    } else {
    	        while (!st.empty() && arr[st.top()] < arr[i]) {
    	            front[st.top()] = i;
    	            st.pop();
    	        }
    	        st.push(i);
    	    }
    	}
    	while (!st.empty()) {
    	    front[st.top()] = -1;
    	    st.pop();
    	}
    	
    	for (i = n; i > 0; --i) {
    	    if (st.empty() || arr[st.top()] >= arr[i]) {
    	        st.push(i);
    	    } else {
    	        while (!st.empty() && arr[st.top()] < arr[i]) {
    	            back[st.top()] = i;
    	            st.pop();
    	        }
    	        st.push(i);
    	    }
    	}
    	while (!st.empty()) {
    	    back[st.top()] = -1;
    	    st.pop();
    	}
    	
    	for (i = 1; i <= n; ++i) {
    	    printf("%lld ", front[i] + back[i]);
    	}
    	puts("");
    	
    	return 0;
    }