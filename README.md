# Thoughts
The problem wasnt hard, conceptually, but I struggled with deciding how to properly implement the proper python syntax. The algorithm starts by finding thelen of the smallest string
in the list of strings. We then iterate using an index based approach up until the lenth of the smallest string is met. During each iterations, we add the index of each character to
a set and if the length of the set equals 1, we know that all the characters at that index are the same(set's cant have duplicate values) and append that character to a string. If the
characters are not the same or the length of the smallest string is met in our index-based iterations, we return the prefix string. 
