#include <bits/stdc++.h>
using namespace std;

int e(int x, int y) {
	int n = max(abs(x), abs(y));
	if (x == -n) {
		return 4 * n * n + n - y;
	} else if (y == -n) {
		return 4 * n * n + 3 * n + x;
	} else if (x == n) {
		return 4 * n * n - 3 * n + y;
	} else if (y == n) {
		return 4 * n * n - n - x;
	}
}

int main() {
	char c, d;
	set<int> xs;
	xs.insert(0);

	int x0 = 0, x1 = 0, y0 = 0, y1 = 0;
	while (cin >> c >> d) {
		switch (c) {
			case '<': x0--; break;
			case 'v': y0--; break;
			case '^': y0++; break;
			case '>': x0++; break;
		}

		switch (d) {
			case '<': x1--; break;
			case 'v': y1--; break;
			case '^': y1++; break;
			case '>': x1++; break;
		}

		xs.insert(e(x0, y0));
		xs.insert(e(x1, y1));
	}

	cout << xs.size() << endl;
}
