#include <bits/stdc++.h>
using namespace std;

int f(char c) {
	if (c <= 'Z') return c - 'A' + 26;
	else return c - 'a';
}

int main() {
	string xs, ys, zs;
	int p = 0;

	while (cin >> xs >> ys >> zs) {
		char ts[52] = {};

		for (char x : xs) ts[f(x)] |= 1;
		for (char y : ys) ts[f(y)] |= 2;
		for (char z : zs) {
			if (ts[f(z)] == 3) {
				p += f(z) + 1;
				break;
			}
		}
	}

	cout << p << endl;
}
