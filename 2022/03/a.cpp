#include <bits/stdc++.h>
using namespace std;

int f(char c) {
	if (c <= 'Z') return c - 'A' + 26;
	else return c - 'a';
}

int main() {
	string xs;
	int p = 0;

	while (cin >> xs) {
		int n = xs.length();

		bool ys[52] = {};
		for (int i = 0; i < n >> 1; i++) ys[f(xs[i])] = true;
		for (int i = n >> 1; i < n; i++) {
			if (ys[f(xs[i])]) {
				p += f(xs[i]) + 1;
				break;
			}
		}
	}

	cout << p << endl;
}
