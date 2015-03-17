tester() {
	local argument_one=$1
	local argument_two=$2
	local argument_three=$3
	local argument_four=$4

	echo "$argument_one$argument_two$argument_three$argument_four" | md5sum | awk '{ print $1 }'
}

tester "$@"
