#include <bits/stdc++.h>
using namespace std;

using ll = long long;

int main() {
	int a, b, c;
	char x;

	ll s = 0;
	while (cin >> a >> x >> b >> x >> c) {
		int x = a * b;
		int y = a * c;
		int z = b * c;

		s += (x + y + z) * 2 + min({ x, y, z });
	}

	cout << s << endl;
}
