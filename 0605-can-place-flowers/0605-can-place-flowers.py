class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        count=0
        fb=len(flowerbed)
        if(fb>=2):
            for i in range(fb):
                if(i==0):
                    if(flowerbed[0]==0 and flowerbed[1]==0):
                        count+=1
                        flowerbed[0]=1
                elif(i==fb-1):
                    if(flowerbed[i]==0 and flowerbed[i-1]==0):
                        count+=1
                        flowerbed[i]=1
                else:
                    if(flowerbed[i]==0 and flowerbed[i-1]==0 and flowerbed[i+1]==0):
                        count+=1
                        flowerbed[i]=1
            if(n<=count):
                return True
            else:
                return False
        elif(fb==1):
            if((flowerbed[0]==1 and n==0) or (flowerbed[0]==0 and (n==1 or n==0))):
                return True
            return False
        