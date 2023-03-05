'''
Given an array of strings words (without duplicates), return all the concatenated words in the given list of words.
A concatenated word is defined as a string that is comprised entirely of at least two shorter words in the given array.

Example 1:
Input: words = ["cat","cats","catsdogcats","dog","dogcatsdog","hippopotamuses","rat","ratcatdogcat"]
Output: ["catsdogcats","dogcatsdog","ratcatdogcat"]
Explanation: "catsdogcats" can be concatenated by "cats", "dog" and "cats"; 
"dogcatsdog" can be concatenated by "dog", "cats" and "dog"; 
"ratcatdogcat" can be concatenated by "rat", "cat", "dog" and "cat".

Example 2:
Input: words = ["cat","dog","catdog"]
Output: ["catdog"]
'''

class Solution:
    def findAllConcatenatedWordsInADict(self, words: List[str]) -> List[str]:
        d = set(words)

        def dfs(word):
            for i in range(1, len(word)):
                p = word[:i]
                s = word[i:]
                if p in d and s in d:
                    return True
					
                if p in d and dfs(s):
                    return True
            return False
        
        l = []
        for i in words:
            if dfs(i):
                l.append(i)

        return l
