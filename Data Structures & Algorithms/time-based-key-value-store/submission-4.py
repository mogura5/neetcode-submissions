class TimeMap:

    def __init__(self):
        self.timeHash = {} # key: [value, timestamp]

    def set(self, key: str, value: str, timestamp: int) -> None:

        if key not in self.timeHash:
            self.timeHash[key] = [[value, timestamp]]
        else:
            self.timeHash[key].append([value, timestamp])

    def get(self, key: str, timestamp: int) -> str:

        if key not in self.timeHash:
            return ""
        else:
            opt = self.timeHash[key]
            left = 0
            right = len(opt) - 1
            res = ""

            while left <= right:
                mid = left + ((right - left) // 2)

                if opt[mid][1] <= timestamp:
                    res = opt[mid][0]
                    left = mid + 1
                else:
                    right = mid - 1
            return res
        
