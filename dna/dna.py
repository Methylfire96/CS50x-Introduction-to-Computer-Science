import csv
import sys


def main():

    # TODO: Check for command-line usage
    if len(sys.argv) != 3:
        print("python dna.py data.csv sequence.txt")


    # TODO: Read database file into a variable
    databases = open("./" + sys.argv[1])
    sequences = open("./" + sys.argv[2])
    with open(databases, "r") as csv:
        reader = csv.DictReader(csv)
        human = list(reader)

    with open(sequences, "r") as txt:
        sequence = sequences.read()

    STRs = list(human[0].keys())[1:]
    # TODO: Read DNA sequence file into a variable


    # TODO: Find longest match of each STR in DNA sequence
    dna = {}
    for str in strs:
        dna[str] = longest_match(str, dna)
    # TODO: Check database for matching profiles
    for row in reader:
        if match(str, dna, row):
            print(f"{row["name"]}")
            return
        else:
            print("no match")

def match(str, dna, row):
    for str in strs:
        if dna[str] != int(row[str]):
            return False
    return True

def longest_match(sequence, subsequence):
    """Returns length of longest run of subsequence in sequence."""

    # Initialize variables
    longest_run = 0
    subsequence_length = len(subsequence)
    sequence_length = len(sequence)

    # Check each character in sequence for most consecutive runs of subsequence
    for i in range(sequence_length):

        # Initialize count of consecutive runs
        count = 0

        # Check for a subsequence match in a "substring" (a subset of characters) within sequence
        # If a match, move substring to next potential match in sequence
        # Continue moving substring and checking for matches until out of consecutive matches
        while True:

            # Adjust substring start and end
            start = i + count * subsequence_length
            end = start + subsequence_length

            # If there is a match in the substring
            if sequence[start:end] == subsequence:
                count += 1

            # If there is no match in the substring
            else:
                break

        # Update most consecutive matches found
        longest_run = max(longest_run, count)

    # After checking for runs at each character in seqeuence, return longest run found
    return longest_run


main()
