#include "../../io.hpp"

struct M {
	multiset<int> xs;
	bool p;
	int q;
	int d;
	vector<int> m;
	int n;
};

int main() {
	string xs;
	vector<M> ys;

	while (getline(cin, xs)) {
		auto ns = read_nums();
		M m { multiset<int>(ns.begin(), ns.end()), false, 0, 0, { 0, 0 } };
		string zs; char o;
		getline(cin, zs, 'd');
		cin >> o >> zs;

		m.p = o == '+';
		m.q = zs == "old" ? -1 : stoi(zs);
		m.d = read_num();
		m.m = { read_num(), read_num() };

		getline(cin, zs);
		ys.push_back(m);
	}

	for (int i = 0; i < 20; i++) {
		for (M& y : ys) {
			for (int x : y.xs) {
				int r = y.q < 0 ? x : y.q;
				if (y.p) r = (x + r) / 3;
				else r = x * r / 3;

				int t = y.m[r % y.d > 0];
				ys[t].xs.insert(r);
			}

			y.n += y.xs.size();
			y.xs.clear();
		}
	}

	sort(ys.begin(), ys.end(), [](M a, M b) {
		return a.n > b.n;
	});

	cout << ys[0].n * ys[1].n << endl;
}
