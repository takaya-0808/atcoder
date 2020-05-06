#include <iostream>
#define rep(i,n) for(int i = 0; i < (n); i++)
using namespace std;

int main(){
	int n; 
	cin >> n;
	int a[n],b[n],c[n-1];
	
	rep(i,n) cin >> a[i];
	rep(i,n) cin >> b[i];
	rep(i,n-1) cin >> c[i];


	int ans = 0;
	rep(i,n) {
		ans += b[i];
		if (a[i] == a[i+1] - 1) {
			ans += c[a[i]-1];
		}
	}
	cout << ans << endl;

	return 0;
}
