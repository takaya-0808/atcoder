#include <iostream>
#include <vector>
#include <map>
#include <tuple>
#include <string>
#define rep(i,n) for(int i = 0; i < (n); i++)
using namespace std;

int main(){
	int n,k,q;
	cin >> n >> k >> q;
	int ans[n];
	 rep(i,n) {
                ans[i] = 0;
        }
	int a;
	rep(i,q) {
		cin >> a;
		ans[a-1] += 1;
	}
	rep(i,n) {
		if (0 < k + (ans[i] - q)) {
			cout << "Yes" << endl;
		} else {
			cout << "No" << endl;
		}
	}
	return 0;
}
