#include <bits/stdc++.h>
using namespace std;

int main() {
	int f = 0;
	int p = 0;

	char c;
	while (cin >> c) {
		if (c == '(') f++;
		else f--;

		p++;
		if (f < 0) break;
	}

	cout << p << endl;
}
