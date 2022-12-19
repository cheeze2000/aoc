#include <bits/stdc++.h>
using namespace std;

using ll = long long;
using ii = pair<ll, ll>;

vector<map<ll, bool>> ss(7, map<ll, bool> { { 0, true } });

bool m(ii dd, vector<ii>& r) {
	for (auto [r0, r1] : r) {
		auto [a, b] = ii(r0 + dd.first, r1 + dd.second);
		if (a < 0 || a > 6 || ss[a][b]) return false;
	}

	return true;
}

int main() {
	string xs;
	cin >> xs;

	ll x = 0, y = 0, s = 4;
	int h = -1, t = -1, dh = 0, dt = 0;
	for (ll i = 0; i < 1000000000000; i++) {
		vector<ii> r;
		if (y == 0) r = { { 2, s }, { 3, s }, { 4, s }, { 5, s } };
		else if (y == 1) r = { { 2, s + 1 }, { 3, s }, { 3, s + 2 }, { 4, s + 1 } };
		else if (y == 2) r = { { 2, s }, { 3, s }, { 4, s }, { 4, s + 1 }, { 4, s + 2 } };
		else if (y == 3) r = { { 2, s }, { 2, s + 1 }, { 2, s + 2 }, { 2, s + 3 } };
		else if (y == 4) r = { { 2, s }, { 2, s + 1 }, { 3, s }, { 3, s + 1 } };

		while (true) {
			char c = xs[x];
			x = (x + 1) % xs.length();
			ii dd = { (c == '>') - (c == '<'), 0 };

			if (m(dd, r)) {
				for (auto& [a, b] : r) {
					a += dd.first;
					b += dd.second;
				}
			}

			if (m({ 0, -1 }, r)) {
				for (auto& [a, b] : r) b--;
			} else {
				for (auto [a, b] : r) {
					ss[a][b] = true;
					s = max(s, ll(b) + 4);
				}

				y = (y + 1) % 5;
				bool f = true;
				for (int k = 0; k < 7; k++) f &= ss[k][s - 4];

				if (f) {
					if (h < 0) {
						h = i;
						t = s - 4;
					} else {
						dh = i - h;
						dt = s - 4 - t;

						ll g = (1000000000000 - h) / dh;
						i = g * dh + h;
						s = g * dt + t + 4;
						for (int k = 0; k < 7; k++) ss[k][s - 4] = true;
					}
				}

				break;
			}
		}
	}

	cout << s - 4 << endl;
}
