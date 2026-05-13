class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        cnt = 0
        nolz = 0 # number of left zero
        norz = 0 # number of right zero
        nomz = 0 # number of middle zero
        if max(flowerbed) == 0:
            cnt = (len(flowerbed)+1) // 2
            return True if cnt >= n else False
        if flowerbed[0] == 0:
            for i in range(len(flowerbed)):
                if flowerbed[i] == 1: 
                    nolz = i
                    break
            cnt += nolz // 2
        
        if flowerbed[-1] == 0:
            for i in range(len(flowerbed),0,-1):
                if flowerbed[i-1] == 1: 
                    norz = len(flowerbed)-i
                    break
            cnt += norz // 2
        fb = flowerbed[nolz:len(flowerbed)-norz]

        for i in fb:
            if i == 1:
                cnt += max(0,(nomz-1)) // 2
                nomz = 0
                continue
            nomz += 1

        return True if cnt >= n else False
            

        