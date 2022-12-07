#!/bin/bash

# prepare input
# replace file sizes with truncate command
sed 's/[0-9]\{1,\}/truncate -s &/' input.txt > input.txt.1
# replace dir with mkdir
sed 's/dir/mkdir/g' input.txt.1 > input.txt.2
# remove $'s
sed 's/\$ //g' input.txt.2 > input.txt.3
# introduce initial dir
sed 's|cd /|rm -rf ./fakeroot \&\& mkdir ./fakeroot \&\& cd ./fakeroot/|g' input.txt.3 > input.txt.4

bash input.txt.4

dir_size() {
	du --bytes | tail -n1 | cut -f1
}
no_directories() {
	find . -type d | wc --lines
}
file_size() {
	(
		cd $1
		ds=$(dir_size)
		nd=$(no_directories)
		echo $((ds - nd*4096))
	)
}
export -f dir_size
export -f no_directories
export -f file_size

cd fakeroot

### Part 1 ###
echo Part 1:
find . -type d -exec bash -c 'file_size "$0"' {} \; \
	|  awk '{if ($0 <= 100000) print $0}' \
	|  awk '{s+=$1} END {print s}'

### Part 2 ###
currently_used=$(file_size .)
freeup_required=$((currently_used - 70000000 + 30000000))

echo Part 2:
find . -type d -exec bash -c 'file_size "$0"' {} \; \
	|  awk -v minsize="$freeup_required" '{if ($0 > minsize) print $0}' \
	| sort --numeric-sort | head -n1
