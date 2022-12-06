#include <bits/stdc++.h>
using namespace std;

int main() {
	string xs;
	cin >> xs;

	int ys[26] = {};

	int a = 0, i = 0;
	for (; i < 4; i++) {
		char c = xs[i];
		a += ys[c - 'a']++;
	}

	for (; a; i++) {
		char c = xs[i - 4];
		char d = xs[i];
		a -= --ys[c - 'a'];
		a += ys[d - 'a']++;
	}

	cout << i << endl;
}
