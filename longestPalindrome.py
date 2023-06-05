""" 409. Longest Palindrome: Given a string s which consists of lowercase or uppercase letters, return the length of the longest palindrome that can be built with those letters.
Letters are case sensitive, for example, "Aa" is not considered a palindrome here.

Input: s = "abccccdd"
Output: 7
Explanation: One longest palindrome that can be built is "dccaccd", whose length is 7.
"""

class Solution:
    def longestPalindrome(self, s: str) -> int:
        """return the length of the longest palindrome(reads the same backward as forward)
        pseudocode:
        1. create an empty set to hold letters
        2. create variable to hold res, which represents the length of the palindrome.
        3. loop over s. if letter in the set-remove it and increase res by 2. else, add letter to set
        4. if the len of set is larger than 0, add one to res (1 letter can go in the middle)
        4. return res
        """

        unpairedLetters = set({}) #set with a dict inside to hold unpaired letters
        palindromeLen = 0 # assign the res to 0

        for letter in s: #loop over the string
            #if the letter is in the set of dict, it means we have a pair!
            if letter in unpairedLetters:
                palindromeLen += 2 #update res (the length of the palindrom)
                unpairedLetters.remove(letter) #remove the letter for dict.
            #if the letter not in the dict, add
            else:
                unpairedLetters.add(letter)

        if len(unpairedLetters) > 0:
                # can use one unpaired letter, in the middle of the palindrome
                palindromeLen += 1
        
        return palindromeLen
