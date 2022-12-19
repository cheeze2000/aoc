#include <bits/stdc++.h>
using namespace std;

set<int> xs;
int n = 0, a, b, c;

int e(int a, int b, int c) {
	return a * 1e6 + b * 1e3 + c;
}

int f(int a, int b, int c) {
	return xs.count(e(a, b, c));
}

int main() {
	while (scanf("%d,%d,%d", &a, &b, &c) == 3) {
		xs.insert(e(a, b, c));
		n += 6 - (f(a - 1, b, c) + f(a + 1, b, c) + f(a, b - 1, c) + f(a, b + 1, c) + f(a, b, c - 1) + f(a, b, c + 1)) * 2;
	}

	cout << n << endl;
}
