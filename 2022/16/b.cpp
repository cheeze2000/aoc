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

int f(int i, int e, int a, int b, ll m, int p, int t) {
	if (t == 0) return 0;

	bool it = a > 0, et = b > 0;
	bool iv = !it && (m & ll(1) << i), ev = !et && (m & ll(1) << e);
	bool ig = !it && !(m & ll(1) << i), eg = !et && !(m & ll(1) << e);

	if (it && ev) return p + f(i, e, a - 1, b, m ^ ll(1) << e, p + ps[e], t - 1);
	if (iv && et) return p + f(i, e, a, b - 1, m ^ ll(1) << i, p + ps[i], t - 1);
	if (iv && ev) return p + f(i, e, a, b, m ^ ll(1) << i ^ ll(1) << e, p + ps[i] + ps[e], t - 1);
	if (it && et) {
		int c = min({ a, b, t });
		return p * c + f(i, e, a - c, b - c, m, p, t - c);
	}

	int r = p * t;
	if (ig && eg) {
		for (int k = 0; k < ps.size(); k++) {
			if (!(m & ll(1) << k)) continue;
			for (int l = 0; l < ps.size(); l++) {
				if (!(m & ll(1) << l) || k == l) continue;
				r = max(r, p + f(k, l, cs[i][k] - 1, cs[e][l] - 1, m, p, t - 1));
			}
		}
	} else if (ig) {
		for (int k = 0; k < ps.size(); k++) {
			if (!(m & ll(1) << k) || k == e) continue;
			if (ev) r = max(r, p + f(k, e, cs[i][k] - 1, b, m ^ ll(1) << e, p + ps[e], t - 1));
			else r = max(r, p + f(k, e, cs[i][k] - 1, b - 1, m, p, t - 1));
		}
	} else if (eg) {
		for (int l = 0; l < ps.size(); l++) {
			if (!(m & ll(1) << l) || l == i) continue;
			if (iv) r = max(r, p + f(i, l, a, cs[e][l] - 1, m ^ ll(1) << i, p + ps[i], t - 1));
			else r = max(r, p + f(i, l, a - 1, cs[e][l] - 1, m, p, t - 1));
		}
	}

	return r;
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

	cout << f(as["AA"], as["AA"], 0, 0, m, 0, 26) << endl;
}
