# Read from the file words.txt and output the word frequency list to stdout.
cat words.txt | tr '\n' ' ' | sed 's/\s\+/\n/g' | sort | uniq -c | sort -r | sed 's/\s\+\([0-9]*\) \([a-z]*\)/\2 \1/'
