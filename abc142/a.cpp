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
	float ans, syo;
	cin >> n;
	if (n%2 == 0) {
		syo = n/2;
	} else {
		syo = (n/2) + 1;
	}
	ans = syo/n;
	cout << ans << endl;
	return 0;
}
