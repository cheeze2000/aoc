const r = require("readline").createInterface({
	input: process.stdin,
	output: process.stdout,
	terminal: false,
});

let n = 0;

r.on("line", l => {
	if (!/(..).*\1/.test(l)) return;
	if (!/(.).\1/.test(l)) return;
	n++;
});

r.once("close", () => console.log(n));
