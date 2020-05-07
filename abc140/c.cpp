#include <iostream>
#include <algorithm>
#define rep(i,n) for(int i = 0; i < (n); i++)
using namespace std;
	
int main() {
	int n;
	cin >> n;
	int b[n-1], result[n];
	rep(i,n-1) cin >> b[i];
	rep(i,n) {
		result[i] = 0;
	}
	rep(i,n) {
		if (i==0 or i==1) {
			result[i] = b[0];
		} else {
			if (b[i] >= max(result[i],result[n-1])) {
				//
			} else {
				result[i] = b[i];
			}
			if (i == n-1) {
				result[i] = b[i-1];
			}
		}
	}
	

	int ans = 0;
	rep(i,n) {
		//cout << result[i] << endl;
		ans += result[i];
	}
	cout << ans <<endl;
	return 0;
}
