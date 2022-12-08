#include <bits/stdc++.h>
using namespace std;

struct T {
	T* t;
	unordered_map<string, T*> xs;
	int s;
};

int s = 0;

void g(T* p) {
	for (auto& q: p->xs) g(q.second);
	if (p->s <= 100000) s += p->s;
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

	g(r);
	cout << s << endl;
}
