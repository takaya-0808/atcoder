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
	bool flag = true;
	rep(i,10) {
		if (i == 0) {
			continue;
		}
		if (n % i == 0) {
			if (n/i >= 10) {
				flag = false;
			} else {
				flag = true;
			}
		}
	}
	if (flag) {
		cout << "Yes" << endl;
	} else {
		cout << "No" << endl;
	}
	return 0;
}
