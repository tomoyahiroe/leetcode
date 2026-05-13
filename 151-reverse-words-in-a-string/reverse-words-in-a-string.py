class Solution:
    def reverseWords(self, s: str) -> str:
        s_list = s.strip().split(" ")
        s_list.reverse()
        ans = []
        for i in range(len(s_list)):
            if s_list[i] != '':
                ans.append(s_list[i])
        return " ".join(ans)