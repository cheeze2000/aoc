#include <bits/stdc++.h>
using namespace std;

vector<char> xs(40);

void d() {
	for (char x : xs) cout << x;
	cout << endl;
}

int main() {
	int n = 0, x = 1;

	string ys;
	while (cin >> ys) {
		xs[n++ % 40] = abs(n % 40 - x) < 2 ? '#' : '.';
		if (n % 40 == 0) d();

		if (ys[0] == 'a') {
			xs[n++ % 40] = abs(n % 40 - x) < 2 ? '#' : '.';
			if (n % 40 == 0) d();

			int s; cin >> s;
			x += s;
		}
	}
}
