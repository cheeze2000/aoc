#include <bits/stdc++.h>
using namespace std;

using ii = pair<int, int>;

int main() {
	vector<vector<int>> xs;
	vector<vector<int>> ys;

	string zs;
	while (cin >> zs) {
		vector<int> as;
		vector<int> bs(zs.length(), 1);

		for (char z : zs) as.push_back(z - '0');
		xs.push_back(as);
		ys.push_back(bs);
	}

	int r = xs.size();
	int c = xs[0].size();

	for (int i = 1; i < r - 1; i++) {
		vector<ii> as, bs;
		as.push_back({ xs[i][0], -1 });
		bs.push_back({ xs[i][c - 1], -1 });

		for (int j = 1; j < c - 1; j++) {
			int a = 0, b = 0, k = c - j - 1;

			while (!as.empty() && as.back().first < xs[i][j]) {
				a += as.back().second + 1;
				as.pop_back();
			}

			while (!bs.empty() && bs.back().first < xs[i][k]) {
				b += bs.back().second + 1;
				bs.pop_back();
			}

			as.push_back({ xs[i][j], a });
			bs.push_back({ xs[i][k], b });
			ys[i][j] *= a + 1;
			ys[i][k] *= b + 1;
		}
	}

	for (int j = 1; j < c - 1; j++) {
		vector<ii> as, bs;
		as.push_back({ xs[0][j], -1 });
		bs.push_back({ xs[r - 1][j], -1 });

		for (int i = 1; i < r - 1; i++) {
			int a = 0, b = 0, k = r - i - 1;

			while (!as.empty() && as.back().first < xs[i][j]) {
				a += as.back().second + 1;
				as.pop_back();
			}

			while (!bs.empty() && bs.back().first < xs[k][j]) {
				b += bs.back().second + 1;
				bs.pop_back();
			}

			as.push_back({ xs[i][j], a });
			bs.push_back({ xs[k][j], b });
			ys[i][j] *= a + 1;
			ys[k][j] *= b + 1;
		}
	}

	int n = 0;
	for (int i = 0; i < r; i++)
		for (int j = 0; j < c; j++)
			n = max(n, ys[i][j]);

	cout << n << endl;
}
