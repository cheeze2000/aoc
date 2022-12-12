#pragma once

#include <bits/stdc++.h>
using namespace std;

using ll = long long;

int read_num() {
	string xs;
	char c;

	while (cin.get(c)) {
		if (isdigit(c)) {
			xs.push_back(c);
		} else {
			if (xs.empty()) continue;
			else return stoi(xs);
		}
	}
}

vector<int> read_nums() {
	string xs, ys;
	vector<int> zs;

	getline(cin, xs);
	xs.push_back(' ');
	for (char x : xs) {
		if (isdigit(x)) {
			ys.push_back(x);
		} else if (!ys.empty()) {
			zs.push_back(stoi(ys));
			ys.clear();
		}
	}

	return zs;
}
