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
	string s;
	char hoge = ' ';
	cin >> n;
	cin >> s;
	rep(i,s.length()) {
		if (hoge != s[i]) {
			ans += 1;		
		} 
		hoge = s[i];
	}
	cout << ans << endl;
	return 0;
}
