#include <bits/stdc++.h>
using namespace std;

using ll = long long;

int read_num() {
	string xs;
	char c;

	while (cin.get(c)) {
		if (isdigit(c)) {
			xs.push_back(c);
		} else {
			if (xs.empty()) continue;
			else return stoi(xs);
		}
	}
}

vector<int> read_nums() {
	string xs, ys;
	vector<int> zs;

	getline(cin, xs);
	xs.push_back(' ');
	for (char x : xs) {
		if (isdigit(x)) {
			ys.push_back(x);
		} else if (!ys.empty()) {
			zs.push_back(stoi(ys));
			ys.clear();
		}
	}

	return zs;
}

struct M {
	vector<ll> xs;
	bool p;
	int q;
	int d;
	vector<int> m;
	int n;
};

int main() {
	string xs;
	vector<M> ys;

	int D = 1;
	while (getline(cin, xs)) {
		auto ns = read_nums();
		M m { vector<ll>(ns.begin(), ns.end()), false, 0, 0, { 0, 0 } };
		string zs; char o;
		getline(cin, zs, 'd');
		cin >> o >> zs;

		m.p = o == '+';
		m.q = zs == "old" ? -1 : stoi(zs);
		m.d = read_num();
		m.m = { read_num(), read_num() };

		D *= m.d;
		getline(cin, zs);
		ys.push_back(m);
	}

	for (int i = 0; i < 10000; i++) {
		for (M& y : ys) {
			for (ll x : y.xs) {
				ll r = y.q < 0 ? x : y.q;
				if (y.p) r += x;
				else r *= x;

				int t = y.m[r % y.d > 0];
				ys[t].xs.push_back(r % D);
			}

			y.n += y.xs.size();
			y.xs.clear();
		}
	}

	sort(ys.begin(), ys.end(), [&](M a, M b) {
		return a.n > b.n;
	});

	cout << (ll) ys[0].n * ys[1].n << endl;
}
