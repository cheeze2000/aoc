#include <bits/stdc++.h>
using namespace std;

using ii = pair<int, int>;
using ll = long long;

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

int M = 4000000;
vector<vector<int>> is;

int main() {
	char c;
	while (cin.get(c)) {
		vector<int> ys = read_nums();
		is.push_back(ys);
	}

	for (int Y = 0; Y <= M; Y++) {
		vector<ii> xs;
		for (auto i : is) {
			int a = i[0], b = i[1], c = i[2], d = i[3];
			int n = abs(a - c) + abs(b - d);
			int h = n - abs(b - Y);
			if (h < 0) continue;

			int x = max(0, a - h), y = min(a + h, M);
			xs.push_back({ x, y });
		}

		sort(xs.begin(), xs.end());
		auto [x, y] = xs[0];

		for (auto [i, j] : xs) {
			if (i == y + 2) {
				ll t = i - 1;
				cout << t * M + Y << endl;
				exit(0);
			} else {
				y = max(y, j);
			}
		}
	}
}
