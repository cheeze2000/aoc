#include <bits/stdc++.h>
using namespace std;

set<int> xs, ys;
int M = 0, n = 0, a, b, c;

struct C {
	int x, y, z;
};

int e(int a, int b, int c) {
	return a * 1e6 + b * 1e3 + c;
}

int f(int a, int b, int c) {
	return xs.count(e(a, b, c));
}

int main() {
	while (scanf("%d,%d,%d", &a, &b, &c) == 3) {
		int h = e(a, b, c);
		xs.insert(h);
		n += 6 - (f(a - 1, b, c) + f(a + 1, b, c) + f(a, b - 1, c) + f(a, b + 1, c) + f(a, b, c - 1) + f(a, b, c + 1)) * 2;

		ys.insert(h);
		M = max({ M, a, b, c });
	}

	queue<C> q;
	q.push(C { 0, 0, 0 });
	while (!q.empty()) {
		auto [x, y, z] = q.front();
		q.pop();

		int h = e(x, y, z);
		if (ys.count(h)) continue;
		ys.insert(h);

		if (x >= 1) q.push(C { x - 1, y, z });
		if (x < M) q.push(C { x + 1, y, z });
		if (y >= 1) q.push(C { x, y - 1, z });
		if (y < M) q.push(C { x, y + 1, z });
		if (z >= 1) q.push(C { x, y, z - 1 });
		if (z < M) q.push(C { x, y, z + 1 });
	}

	for (int i = 0; i <= M; i++) {
		for (int j = 0; j <= M; j++) {
			for (int k = 0; k <= M; k++) {
				int h = e(i, j, k);
				if (ys.count(h)) continue;

				xs.insert(h);
				n += 6 - (f(i - 1, j, k) + f(i + 1, j, k) + f(i, j - 1, k) + f(i, j + 1, k) + f(i, j, k - 1) + f(i, j, k + 1)) * 2;
			}
		}
	}

	cout << n << endl;
}
