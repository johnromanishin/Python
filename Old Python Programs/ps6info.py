# -*- coding: utf-8 -*-
def load_subjects(fName):
    """
    Returns a SubjectList of Subjects. The subject information is read
    from the file named by the string fName. Each line of the file
    contains a string of the form "name,value,cost"

    returns: SubjectList
    """
# -*- coding: utf-8 -*-
    # The following sample code reads lines from the specified file and prints
    # each one.
    inFile = open(fName, 'r', 0)
    for line in inFile:
        print line
# TO DO: Instead of printing each line, modify the above to parse
    # the name, value, and cost of each subject and create a SubjectList.

##HINTS: You may find split() and strip() methods of strings useful when implementing this. See their documentation at the online Python Library Reference. split() is useful to split at commas, and strip() is useful to remove the linebreak at the end of each line.
##
##Update on April 2: Here is a sample output (truncated):
##
##    >>> print load_subjects(SUBJECT_FILENAME)
##
##    Course	Value	Cost
##    ======	====	=====
##    10.00	1	20
##    10.01	2	20
##    10.02	1	16
##    10.03	6	19
##    10.04	3	13
##    10.15	8	13
##
##    ... TRUNCATED ...
##
##    9.16	9	10
##    9.17	9	11
##    9.18	7	16
##    9.19	9	9
##
##    Total Value:	1804
##    Total Cost:	3442
    strip(  	[chars])
    Return a copy of the string with the leading and trailing characters removed. The chars argument is a string specifying the set of
    characters to be removed. If omitted or None, the chars argument defaults to removing whitespace. The chars argument is not a
    prefix or suffix; rather, all combinations of its values are stripped:

        >>> '   spacious   '.strip()
        'spacious'
        >>> 'www.example.com'.strip('cmowz.')
        'example'

    Changed in version 2.2.2: Support for the chars argument.
    split(  	[sep [,maxsplit]])
    Return a list of the words in the string, using sep as the delimiter string. If maxsplit is given, at most maxsplit splits are done.
    (thus, the list will have at most maxsplit+1 elements). If maxsplit is not specified, then there is no limit on the number of splits
    (all possible splits are made). Consecutive delimiters are not grouped together and are deemed to delimit empty strings (for example,
    "'1„2'.split(',')"returns "['1', '', '2']"). The sep argument may consist of multiple characters (for example, "'1, 2, 3'.split(', ')"
    returns "['1', '2', '3']"). Splitting an empty string with a specified separator returns "['']".

    If sep is not specified or is None, a different splitting algorithm is applied. First, whitespace characters (spaces, tabs, newlines,
    returns, and formfeeds) are stripped from both ends. Then, words are separated by arbitrary length strings of whitespace characters.
    Consecutive whitespace delimiters are treated as a single delimiter ("'1 2 3'.split()" returns "['1', '2', '3']"). Splitting an empty
    string or a string consisting of just whitespace returns an empty list. 
