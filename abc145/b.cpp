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
	string str;
	string a_str,b_str;
	bool flag = true;	

	cin >> n;
	cin >> str;
	if (n%2 == 0) {
		if (str.substr(0,n/2) != str.substr(n/2,n)) {
			flag = false;
		}
	} else {
		flag = false;
	}
	if (flag) {
		cout << "Yes" << endl;
	} else {
		cout << "No" << endl;
	}
	return 0;
}
