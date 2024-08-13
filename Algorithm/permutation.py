#PERMUTATIONS

# RECURSIVE PROGRAM FOR PERMUTATIONS

def permute(string, pocket=""):
    if len(string) == 0:
        print(pocket)
    else:
        for i in range(len(string)):
            letter = string[i]
            start = string[0:i]
            end = string[i+1:]
            together = start + end
            permute(together, pocket + letter)
print(permute("Xubair"))
    