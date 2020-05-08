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
	int n,k,ans;
	cin >> n >> k;
	int h[n];
	rep(i,n) cin >> h[i];
	rep(i,n) {
		if (h[i] >= k) ans += 1;
	}
	cout << ans << endl;
	
	return 0;
}
