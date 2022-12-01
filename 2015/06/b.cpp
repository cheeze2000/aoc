#include <bits/stdc++.h>
using namespace std;

int main() {
	int a, b, c, d;
	string xs;
	vector<int> ys(1000000);

	while (cin >> xs) {
		if (xs == "toggle") {
			scanf("%d,%d through %d,%d", &a, &b, &c, &d);
			for (int i = a; i <= c; i++) {
				for (int j = b; j <= d; j++) {
					ys[i * 1000 + j] += 2;
				}
			}
		} else {
			cin >> xs;
			scanf("%d,%d through %d,%d", &a, &b, &c, &d);
			for (int i = a; i <= c; i++) {
				for (int j = b; j <= d; j++) {
					int y = ys[i * 1000 + j];
					y += xs == "on" ? 1 : -1;
					y = max(0, y);
					ys[i * 1000 + j] = y;
				}
			}
		}
	}

	int n = 0;
	for (int y : ys) n += y;
	cout << n << endl;
}
