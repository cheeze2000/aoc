#include <bits/stdc++.h>
using namespace std;

int main() {
	char a, b;
	int s = 0;

	while (cin >> a >> b) {
		int c = a - 'A';
		int d = b - 'X';

		s += d + 1;
		switch ((d - c + 3) % 3) {
			case 0: s += 3; break;
			case 1: s += 6; break;
		}
	}

	cout << s << endl;
}
