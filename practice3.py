import time 

class StopWatch:
    def __init__(self, startTime = 0, endTime = 0, elapsedTime = 0):
        self.__startTime = startTime
        self.__endTime = endTime
        self.__elapsedTime = elapsedTime

    def start(self):
        self.__startTime = time.time()

    def stop(self): 
        return self.getElapsedTime()

    def reset(self):
        self.__startTime = 0
        self.__elapsedTime = 0

    def getstarttime(self):
        return self.__startTime

    def getendtime(self):
        return self.__endTime

    def getElapsedTime(self):
        elapsedTime = self.__elapsedTime
        elapsedTime +=((time.time() - self.__startTime) * 1000)
        return elapsedTime

def main():
    x = StopWatch()
    x.start()
    a = time.time() #code only works with this line of code in place (I don't understand why?)
    sum = 0 
    for i in range(1 , 10000000):
        sum += i
    x.stop()
    print("Elapsed execution time is", x.getElapsedTime())
    print(sum)
    x.reset()

main()