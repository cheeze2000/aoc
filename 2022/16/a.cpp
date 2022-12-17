#include <bits/stdc++.h>
using namespace std;

using ii = pair<int, int>;
using ll = long long;

pair<vector<string>, int> read_valves() {
	string xs, ys, b;
	vector<string> zs;

	getline(cin, xs);
	xs.push_back(' ');
	for (char x : xs) {
		if (isdigit(x)) {
			b.push_back(x);
		} else if (isupper(x)) {
			ys.push_back(x);
		} else if (!ys.empty()) {
			zs.push_back(ys);
			ys.clear();
		}
	}

	return { zs, stoi(b) };
}

unordered_map<string, int> as;
vector<vector<int>> bs, cs;
vector<int> ps;

int f(int i, ll m, int p, int t) {
	if (t == 0) return 0;

	if (m & ll(1) << i) {
		return p + f(i, m ^ ll(1) << i, p + ps[i], t - 1);
	} else {
		int r = p * t;
		for (int k = 0; k < ps.size(); k++) {
			int j = cs[i][k];
			if (!(m & ll(1) << k) || t <= j) continue;
			r = max(r, p * j + f(k, m, p, t - j));
		}

		return r;
	}
}

int main() {
	vector<vector<string>> ts;

	char c;
	while (cin.get(c)) {
		auto [a, b] = read_valves();
		string n = a[0];
		as[n] = as.size();
		ts.push_back(vector<string>(a.begin() + 1, a.end()));
		ps.push_back(b);
	}

	for (auto t : ts) {
		vector<int> us;
		for (auto u : t) us.push_back(as[u]);
		bs.push_back(us);
	}

	int b = bs.size();
	cs = vector<vector<int>>(b, vector<int>(b, 1e9));
	for (int i = 0; i < b; i++) {
		cs[i][i] = 0;
		for (auto b : bs[i]) cs[i][b] = 1;
	}

	for (int k = 0; k < b; k++)
		for (int i = 0; i < b; i++)
			for (int j = 0; j < b; j++)
				cs[i][j] = min(cs[i][j], cs[i][k] + cs[k][j]);

	ll m = 0;
	for (int i = 0; i < ps.size(); i++) m |= (ll(1) << i) * (ps[i] > 0);

	cout << f(as["AA"], m, 0, 30) << endl;
}
