#include <bits/stdc++.h>
using namespace std;

struct P {
	int i;
	int j;
	int k;
};

int dx[] = { -1, 0, 0, 1 };
int dy[] = { 0, -1, 1, 0 };

int main() {
	vector<vector<char>> xs;
	queue<P> q;

	string ys;
	pair<int, int> e;

	int r = 0;
	while (cin >> ys) {
		vector<char> zs;
		for (int i = 0; i < ys.length(); i++) {
			char c = ys[i];
			if (c == 'S' || c == 'a') {
				q.push({ r, i, 0 });
				zs.push_back('a');
			} else if (c == 'E') {
				e = { r, i };
				zs.push_back('z');
			} else {
				zs.push_back(c);
			}
		}

		xs.push_back(zs);
		r++;
	}

	while (!q.empty()) {
		auto [i, j, k] = q.front();
		q.pop();

		if (e.first == i && e.second == j) {
			cout << k << endl;
			break;
		}

		for (int n = 0; n < 4; n++) {
			int a = i + dx[n], b = j + dy[n];
			if (a < 0 || b < 0 || a >= r || b >= ys.length()) continue;
			if (!xs[i][j] || xs[a][b] - xs[i][j] > 1) continue;
			q.push({ a, b, k + 1 });
		}

		xs[i][j] = 0;
	}
}
