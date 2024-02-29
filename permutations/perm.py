def permutations(s):
    if len(s) <= 1:
        return [s]  # Return the set as a list containing itself if it has 1 or fewer elements

    all_perms = []  # Initialize a list to store all permutations

    for i in range(len(s)):
        # Extract the current element and the remaining subset
        first_element = s[i]
        subset = s[:i] + s[i+1:]

        # Recursively generate permutations for the subset
        partial_perms = permutations(subset)

        # Combine the current element with each permutation of the subset
        for perm in partial_perms:
            all_perms.append([first_element] + perm)

    return all_perms


# Test the function
print(permutations(['d', 'o', 'g']))
