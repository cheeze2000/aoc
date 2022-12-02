#include <bits/stdc++.h>
using namespace std;

int main() {
	char a, b;
	int s = 0;

	while (cin >> a >> b) {
		int c = a - 'A';
		int d = b - 'X';
		s += (c + d + 2) % 3 + (d * 3 + 1);
	}

	cout << s << endl;
}
