#include <bits/stdc++.h>
using namespace std;

int main() {
	string xs;
	priority_queue<int> ys;

	int n = 0;
	while (getline(cin, xs)) {
		if (xs.empty()) {
			ys.push(n);
			n = 0;
		} else {
			n += stoi(xs);
		}
	}

	ys.push(n);
	n = 0;
	for (int i = 0; i < 3; i++) {
		n += ys.top();
		ys.pop();
	}

	cout << n << endl;
}
