#include <bits/stdc++.h>
using namespace std;

int main() {
	vector<deque<char>> xs(9, deque<char>());

	string ys;
	while (getline(cin, ys)) {
		if (ys.empty()) break;

		for (int i = 0; i < ys.length(); i++) {
			char y = ys[i];
			if (y < 'A' || y > 'Z') continue;
			xs[i >> 2].push_front(y);
		}
	}

	int a, b, c;
	while (scanf("move %d from %d to %d\n", &a, &b, &c) == 3) {
		while (a--) {
			xs[c - 1].push_back(xs[b - 1].back());
			xs[b - 1].pop_back();
		}
	}

	for (auto x : xs) cout << x.back();
	cout << endl;
}
