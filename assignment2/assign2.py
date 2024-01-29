# Question 1
# Returns all permutations of a set
# Modify this to generate the set as on slide 18 of Topic 2
def permutations(aSet):
    if len(aSet) <= 1:
        return [aSet]

    all_perms = []

    for i in range(len(aSet)):
        first_element = [aSet[i]] if isinstance(aSet[i], str) else aSet[i]
        rest_elements = aSet[:i] + aSet[i+1:]
        partial_perms = permutations(rest_elements)
        for perm in partial_perms:
            all_perms.append(first_element + perm)
    return all_perms

# Question 2
# Given 'n' as input, generate a list of numbers from 2^n-1 down to 0
def generateReverseOrder(n):
    # Base case
    if n == 0:
        return ['0']
    elif n == 1:
        return ['1', '0']
    
    else: 
        prev_list = generateReverseOrder(n - 1)  # Recursion
        result = []
        for string in prev_list:
            result.append('1' + string)
        for string in prev_list:
            result.append('0' + string)
        return result

# Question 3
# Return a 3-element integer list containing number of consonants, vowels,
# and other characters (respectively) for the given string
def countChars(s):
    vowels = "aeiouAEIOU"

    # Base case: if the string is empty, return [0, 0, 0]
    if len(s) == 0:
        return [0, 0, 0]

    # Count the first character
    consonants_count = 1 if s[0].isalpha() and s[0] not in vowels else 0
    vowels_count = 1 if s[0].isalpha() and s[0] in vowels else 0
    other_count = 1 if not s[0].isalpha() else 0

    # Recursively count the rest of the string
    counts = countChars(s[1:])
    return [consonants_count + counts[0], vowels_count + counts[1], other_count + counts[2]]


# --------------------------------------------------------
# Tester code for all questions
# Q1 tester code; do not make any changes to this block of code
print("------------------------------------------------")
print("Q1 tester\n")
print("Actual:  ", end=' ')
for permutation in permutations(["d","o","g"]):
  print(permutation, end=' ')
print("\nExpected:", end=' ')
print("['d', 'o', 'g']", end=' ')
print("['d', 'g', 'o']", end=' ')
print("['o', 'd', 'g']", end=' ')
print("['o', 'g', 'd']", end=' ')
print("['g', 'd', 'o']", end=' ')
print("['g', 'o', 'd']")


# Q2 tester code; do not make any changes to this block of code
print("------------------------------------------------")
print("Q2 tester\n")
print("Descending binary numbers:")
for i in range(1, 5):
  print(i, "bit:", *generateReverseOrder(i))

print("\nExpected:")
print("1 bit: 1 0")
print("2 bit: 11 10 01 00")
print("3 bit: 111 110 101 100 011 010 001 000")
print("4 bit: 1111 1110 1101 1100 1011 1010 1001 1000 0111 0110 0101 0100 0011 0010 0001 0000")


# Q3 tester code; you may make changes to the call to countChars(),
# to account for any extra parameters you may add
print("------------------------------------------------")
print("Q3 tester\n")
s = "abc de"
print(s)
print("Consonants, Vowels, Other:", countChars(s))
print("Expected: [3, 2, 1]")
print()
s = "To be or not to be"
print(s)
print("Consonants, Vowels, Other:", countChars(s))
print("Expected: [7, 6, 5]")

print("------------------------------------------------")