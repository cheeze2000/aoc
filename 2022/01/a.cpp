#include <bits/stdc++.h>
using namespace std;

int main() {
	string xs;

	int m = 0;
	int n = 0;
	while (getline(cin, xs)) {
		if (xs.empty()) {
			m = max(m, n);
			n = 0;
		} else {
			n += stoi(xs);
		}
	}

	cout << max(m, n) << endl;
}
