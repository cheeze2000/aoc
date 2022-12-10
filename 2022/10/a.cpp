#include <bits/stdc++.h>
using namespace std;

int main() {
	vector<int> xs(12);
	int n = 0, x = 1;

	string ys;
	while (cin >> ys) {
		if (++n % 20 == 0) xs[n / 20] = x * n;
		if (ys[0] == 'a') {
			if (++n % 20 == 0) xs[n / 20] = x * n;
			int s; cin >> s;
			x += s;
		}
	}

	cout << xs[1] + xs[3] + xs[5] + xs[7] + xs[9] + xs[11] << endl;
}
