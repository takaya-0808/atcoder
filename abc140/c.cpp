#include <iostream>
#include <algorithm>
#define rep(i,n) for(int i = 0; i < (n); i++)
using namespace std;
	
int main() {
	int n;
	cin >> n;
	int b[n-1], a[n];
	rep(i,n-1) cin >> b[i];
	rep(i,n) a[i] = 0;
	rep(i,2) a[i] = b[0];
	//rep(i,n) cout << a[i] << endl;   

	rep(i,n-1) {
		//cout << i << endl;
		if (b[i] >= max(a[i],a[i+1])) {
			a[i+1] = b[i];
		} else {
			a[i] = b[i];
			a[i+1] = b[i];
		} 
	}
	

	int ans = 0;
	rep(i,n) {
		ans += a[i];
	}
	cout << ans <<endl;
	return 0;
}
