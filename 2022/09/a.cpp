#include <bits/stdc++.h>
using namespace std;

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

	int i = 0, j = 0, k = 0, l = 0;
	while (cin >> c >> d) {
		int dx = (c == 'R') - (c == 'L');
		int dy = (c == 'U') - (c == 'D');

		while (d--) {
			i += dx;
			j += dy;

			int p = i - k, q = j - l;
			if (max(abs(p), abs(q)) < 2) continue;

			k += (p + (p > 0) - (p < 0)) / 2;
			l += (q + (q > 0) - (q < 0)) / 2;

			xs.insert(e(k, l));
		}
	}

	cout << xs.size() << endl;
}
