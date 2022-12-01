#include <bits/stdc++.h>
using namespace std;

int main() {
	int f = 0;

	char c;
	while (cin >> c) {
		if (c == '(') f++;
		else f--;
	}

	cout << f << endl;
}
