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
	int n;
	cin >> n;
	int a[n];
	vector<int> ans(n,0);
	rep(i,n) cin >> a[i];
	rep(i,n) ans[a[i] - 1] = i + 1;
	rep(i,n) cout << ans.at(i) << " ";
	cout << endl;
	return 0;
}
