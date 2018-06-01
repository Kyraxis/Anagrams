from collections import Counter
import unittest

def bananagrams(s1, s2):
    aList = list(s2)

    pos1 = 0
    isWorking = True

    while pos1 < len(s1) and isWorking:
        pos2 = 0
        found = False
        while pos2 < len(s1) and pos2 < len(s2) and not found:
            if s1[pos1] == aList[pos2]:
                found = True
            else:
                pos2 = pos2 + 1

        if found:
            aList[pos2] = None
        else:
            isWorking = False

        pos1 = pos1 + 1

    return isWorking

def bananagrams2(s1, s2):
    aList1 = sorted(s1)
    aList2 = sorted(s2)

    position = 0
    matches = False
    'Calculate length one time - Not x number of times'
    s2length = len(s2)
    s1length = len(s1)

    while position < s1length and position < s2length:
        if aList1[position] != aList2[position]:
            matches = False
            break
        matches = True
        position = position + 1

    return matches

print(bananagrams2('silent', 'listen'))

def is_bananagram(str1, str2):
    """This is a sorting method using Hashable objects built into the Colletions library
    in Python. (Line 1)"""
    return Counter(str1) == Counter(str2)

class TestMethod(unittest.TestCase):
    """TESTING THESE BITCHES"""

    def testActualAnagramJustScrambled(self):
        anagrams = bananagrams('shart', 'hasrt')
        self.assertTrue(anagrams)

    def testCheckingForAnActualFalse(self):
        anagrams = bananagrams('dad', 'mom')
        self.assertFalse(anagrams)

    def testCheckingForAnagramInReverse(self):
        reverse = bananagrams('grandpa', 'apdanrg')
        self.assertTrue(reverse)

    def testSecondWordLongerThanFirst(self):
        length = is_bananagram('fart', 'farts')
        self.assertFalse(length)

    def testTwoWordsWithNonMatchingLengthFirstWord(self):
        length = is_bananagram('farts', 'fart')

unittest.main()