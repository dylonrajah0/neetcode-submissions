class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded = ""

        for word in strs:
            length = str(len(word))
            add = length + "#" + word
            encoded = encoded + add
            #print(encoded)

        #print(encoded)
        return encoded

    def decode(self, s: str) -> List[str]:
        #print("in decode")
        decoded = []

        increment = 0
        start = 0
        num = ""
        while increment < len(s):
            
            if s[increment] == "#":
                num = int(s[start:increment])
                #print("Num: ", num)
                decoded.append(s[increment+1:increment+num+1])
                #print(decoded)
                start = increment + num +1
                #print("start: ", start)
                increment = increment + num
                #print("increment: ", increment)
                
                
            increment+=1
        return decoded