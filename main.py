import importlib
import sys

argv = sys.argv
year = argv[1]
day = f"{int(argv[2][:-1]):02d}"
part = argv[2][-1]
input_type = argv[3] if len(argv) > 3 else "x"

module = importlib.import_module(f"{year}.{day}.{day}{part}")
input = open(f"{year}/{day}/{day}{input_type}.txt").read().strip()
answer = module.solve(input)

print(answer)
