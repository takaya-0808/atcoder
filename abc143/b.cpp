#include <iostream>
#include <cstring>
#include <cmath>
#include <vector>
#include <algorithm>
#include <stdio.h>
#include <math.h>
#include <stdlib.h>
#include <set>
#include <map>
#include <iterator>
#include <stack>
#include <string.h>
#include <cstdlib>
#include <queue>
#include <list>
#include <string>
#define rep(i,n) for(int i = 0; i < (n); i++) 
using namespace std;

int main() {
	int n, ans = 0;
	cin >> n;
	int d[n];
	rep(i,n) cin >> d[i];
	rep(i,n) {
		rep(j,n) {
			if (i < j) {
				ans += d[i] * d[j]; 		
			}	
		}
	}
	cout << ans << endl;
	return 0;
}
