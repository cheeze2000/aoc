#include <bits/stdc++.h>
using namespace std;

int main() {
	int a, b, c, d, n = 0;
	while (scanf("%d-%d,%d-%d", &a, &b, &c, &d) == 4) {
		n += a <= c & b >= d | c <= a & d >= b;
	}

	cout << n << endl;
}
