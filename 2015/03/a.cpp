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
	char c;
	set<int> xs;
	xs.insert(0);

	int x = 0, y = 0;
	while (cin >> c) {
		switch (c) {
			case '<': x--; break;
			case 'v': y--; break;
			case '^': y++; break;
			case '>': x++; break;
		}

		xs.insert(e(x, y));
	}

	cout << xs.size() << endl;
}
