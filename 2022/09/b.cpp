#include <bits/stdc++.h>
using namespace std;

using ii = pair<int, int>;

int e(int x, int y) {
	int n = max(abs(x), abs(y));
	if (x == -n) return 4 * n * n + n - y;
	else if (y == -n) return 4 * n * n + 3 * n + x;
	else if (x == n) return 4 * n * n - 3 * n + y;
	else if (y == n) return 4 * n * n - n - x;
}

int main() {
	char c; int d;
	set<int> xs { 0 };

	vector<ii> ys(10);
	while (cin >> c >> d) {
		int dx = (c == 'R') - (c == 'L');
		int dy = (c == 'U') - (c == 'D');

		while (d--) {
			ys[0].first += dx;
			ys[0].second += dy;

			for (int n = 1; n < 10; n++) {
				auto& [i, j] = ys[n - 1];
				auto& [k, l] = ys[n];

				int p = i - k, q = j - l;
				if (max(abs(p), abs(q)) < 2) break;

				k += (p + (p > 0) - (p < 0)) / 2;
				l += (q + (q > 0) - (q < 0)) / 2;
			}

			xs.insert(e(ys[9].first, ys[9].second));
		}
	}

	cout << xs.size() << endl;
}
