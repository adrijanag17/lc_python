class Solution:

    # time - O(n) space - O(1) where n = len(strs)
    def encode(self, strs: list[str]) -> str:
        res = ""

        for s in strs:
            res += str(len(s)) + "#" + s

        return res


    # time - O(m^2) space - O(1) where m = len(str)
    def decode(self, str) -> list[str]:
        
        res = []
        i = 0

        while i < len(str):
            j = i
            while str[j] != "#":
                j += 1
            length = int(str[i:j])
            res.append(str[j + 1 : j + 1 + length])
            i = j + 1 + length

        return res



def main():
    sol = Solution()
    enc = sol.encode(["leet", "code", "is", "awesome"])
    print(enc)
    print(sol.decode(enc))


main()
