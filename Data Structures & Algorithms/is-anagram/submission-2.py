class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        if(len(s) != len(t)):
            return False
        
        map = {}

        for x in s:
            map[x] = map.get(x,0) + 1

        #print(map)
        
        for y in t:
            #print("Curr Char: ", y)
            if y not in map:
                return False
            #print("val of y", map[y])
            map[y] = map.get(y, 0) - 1
            #print("val of y after remove", map[y])

            if map[y] < 0:
                return False

            
        
        if not map:
            return False

        return True
