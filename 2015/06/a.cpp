#include <bits/stdc++.h>
using namespace std;

int main() {
	int a, b, c, d;
	string xs;
	vector<bool> ys(1000000);

	while (cin >> xs) {
		if (xs == "toggle") {
			scanf("%d,%d through %d,%d", &a, &b, &c, &d);
			for (int i = a; i <= c; i++) {
				for (int j = b; j <= d; j++) {
					ys[i * 1000 + j] = !ys[i * 1000 + j];
				}
			}
		} else {
			cin >> xs;
			scanf("%d,%d through %d,%d", &a, &b, &c, &d);
			for (int i = a; i <= c; i++) {
				for (int j = b; j <= d; j++) {
					ys[i * 1000 + j] = xs == "on";
				}
			}
		}
	}

	int n = 0;
	for (bool y : ys) n += y;
	cout << n << endl;
}
