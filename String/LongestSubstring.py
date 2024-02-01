# Problem Link: https://leetcode.com/problems/longest-substring-without-repeating-characters/

class Substring:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # Empty set
        my_set = set()

        i: int = 0
        max_len: int = 0

        for j in range(len(s)):
            if s[j] in my_set:
                while s[i] != s[j]:
                    my_set.remove(s[i])
                    i += 1
                
                # Now remove the current character which are in set already
                my_set.remove(s[i])
                i += 1
        
            my_set.add(s[j])
            max_len = max(max_len, len(my_set))

        return max_len
    

if __name__ == "__main__":
    obj = Substring()
    ans: int = obj.lengthOfLongestSubstring("abcabcbb")
    print(ans)