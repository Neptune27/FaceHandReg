from collections import deque


class AverageStat:
    def __init__(self, buffer=1):
        self._buffer = deque(maxlen=buffer)

    def add(self, name):
        self._buffer.append(name)

    def getNamedAvg(self, name):
        count = 0
        for i in self._buffer:
            if i == name:
                count += 1
        return count/len(self._buffer)
