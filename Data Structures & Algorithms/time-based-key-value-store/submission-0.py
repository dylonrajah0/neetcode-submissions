class TimeMap:

    def __init__(self):
        self.timeMap = {}
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        
        if key not in self.timeMap:
            self.timeMap[key] = []
        

        tuple = (timestamp, value)
        self.timeMap[key].append(tuple)


    def get(self, key: str, timestamp: int) -> str:

        if key not in self.timeMap:
            return ""

        values = self.timeMap[key]

        left = 0
        right = len(values)-1
        closest = ""

        while left <= right:

            mid = (left+right)//2

            midTime = values[mid][0]

            if midTime == timestamp:
                return values[mid][1]

            elif midTime > timestamp:
                right = mid - 1
            else:
                closest = values[mid][1]
                left = mid + 1
        return closest
