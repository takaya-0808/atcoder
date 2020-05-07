#include <iostream>
#include <vector>
#include <map>
#include <tuple>
#include <string>
#define rep(i,n) for(int i = 0; i < (n); i++)
using namespace std;

int main() {
	string s;
	char c;
	cin >> s;
	int ans = 1;
	rep(i, s.length()) {
		c = s[i];
		if (i%2 == 0) {
			if (c == 'R' or c == 'U' or c == 'D') {
				//			
			} else {
				ans = 0;
			}
		} else {
			if (c == 'L' or c == 'U' or c == 'D') {
				//
			} else {
				ans = 0;
			}
		}
		
	}
	if (ans == 1) {
		cout << "Yes" << endl;
	} else {
		cout << "No" << endl;
	} 
	return 0;
}
