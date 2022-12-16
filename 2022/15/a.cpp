#include <bits/stdc++.h>
using namespace std;

using ii = pair<int, int>;

vector<int> read_nums() {
	string xs, ys;
	vector<int> zs;

	getline(cin, xs);
	xs.push_back(' ');
	for (char x : xs) {
		if (isdigit(x) || x == '-') {
			ys.push_back(x);
		} else if (!ys.empty()) {
			zs.push_back(stoi(ys));
			ys.clear();
		}
	}

	return zs;
}

int Y = 2000000;

int main() {
	char c;
	vector<ii> xs;

	while (cin.get(c)) {
		vector<int> ys = read_nums();
		int a = ys[0], b = ys[1], c = ys[2], d = ys[3];

		int n = abs(a - c) + abs(b - d);
		int h = n - abs(b - Y);
		if (h < 0) continue;

		int x = a - h, y = a + h;
		if (d == Y) {
			if (x < c) xs.push_back({ x, c - 1 });
			if (c < y) xs.push_back({ c + 1, y });
		} else {
			xs.push_back({ x, y });
		}
	}

	sort(xs.begin(), xs.end());
	auto [x, y] = xs[0];
	int z = 0;

	for (auto [i, j] : xs) {
		if (i > y) {
			z += y - x + 1;
			x = i, y = j;
		} else {
			y = max(y, j);
		}
	}

	z += y - x + 1;
	cout << z << endl;
}
