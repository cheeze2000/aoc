#include <bits/stdc++.h>
using namespace std;

struct T {
	T* t;
	unordered_map<string, T*> xs;
	int s;
};

int t = INT_MAX;

void g(T* p, int r) {
	for (auto& q: p->xs) g(q.second, r);
	if (p->s >= r) t = min(t, p->s);
}

int main() {
	T* p = new T { nullptr, unordered_map<string, T*>(), 0 };
	T* r = p;

	string xs, ys;
	while (cin >> xs >> ys) {
		if (ys == "ls") {
			continue;
		} else if (ys == "cd") {
			cin >> ys;
			if (ys == "..") p = p->t;
			else if (ys == "/") p = r;
			else p = p->xs[ys];
		} else if (xs == "dir") {
			p->xs[ys] = new T { p, unordered_map<string, T*>(), 0 };
		} else {
			T* q = p;
			int x = stoi(xs);
			do { q->s += x; q = q->t; } while (q);
		}
	}

	g(r, r->s - 40000000);
	cout << t << endl;
}
