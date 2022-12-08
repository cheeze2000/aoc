#include <bits/stdc++.h>
using namespace std;

int main() {
	vector<vector<int>> xs;
	vector<vector<bool>> ys;

	string zs;
	while (cin >> zs) {
		vector<int> as;
		vector<bool> bs(zs.length());

		for (char z : zs) as.push_back(z - '0');
		xs.push_back(as);
		ys.push_back(bs);
	}

	int r = xs.size();
	int c = xs[0].size();

	for (int i = 0; i < r; i++) {
		int p = -1, q = -1;
		for (int j = 0; j < c; j++) {
			int k = c - j - 1;
			ys[i][j] = ys[i][j] | xs[i][j] > p;
			ys[i][k] = ys[i][k] | xs[i][k] > q;
			p = max(p, xs[i][j]);
			q = max(q, xs[i][k]);
		}
	}

	for (int j = 0; j < c; j++) {
		int p = -1, q = -1;
		for (int i = 0; i < r; i++) {
			int k = r - i - 1;
			ys[i][j] = ys[i][j] | xs[i][j] > p;
			ys[k][j] = ys[k][j] | xs[k][j] > q;
			p = max(p, xs[i][j]);
			q = max(q, xs[k][j]);
		}
	}

	int n = 0;
	for (auto y : ys) for (bool b : y) n += b;
	cout << n << endl;
}
