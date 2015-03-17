from random import randrange
from subprocess import Popen, PIPE, DEVNULL

def truncate_test(times):
	sh_command = ["sh", "-s", "--", "a", "b", "c", "d"]
	expected_full = "f5ac8127b3b6b85cdc13f237c6005d80"
	expected_truncd = ""

	with open("truncate-test.sh", "r") as f:
		script = f.read()

	results = []
	for i in range(times):
		truncd = random_trunc(script)
		sh = Popen(sh_command, stdin=PIPE, stdout=PIPE, stderr=DEVNULL)
		output = sh.communicate(input=truncd.encode("utf-8"))[0].decode("utf-8")
		if len(truncd) == len(script):
			was_right = output == expected_full
		else:
			was_right = output == expected_truncd
		if not was_right:
			print("hypothesis failed(?)")
			print("\tscript:")
			print(truncd)
			print("\tscript output")
			print(output)
		results.append(was_right)
	print(all(results))

def random_trunc(script):
	return script[:randrange(0, len(script)-1)]

truncate_test(500)
