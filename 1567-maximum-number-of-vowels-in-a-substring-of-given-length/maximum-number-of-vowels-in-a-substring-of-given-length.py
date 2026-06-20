class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        window = s[0:k]
        nvl = len("".join([v if v in "aeiou" else "" for v in window]))
        ans = nvl

        for v in s[k:]:
            if window[0] in "aeiou":
                if v in "aeiou":
                    window = window[1:] + v
                    continue
                nvl -= 1
                window = window[1:] + v
            else:
                if v in "aeiou":
                    nvl += 1
                    ans = max(ans, nvl)
                    window = window[1:] + v
                else:
                    window = window[1:] + v
                    continue
        return ans