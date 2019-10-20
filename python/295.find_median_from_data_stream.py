import heapq
class MedianFinder:

    def __init__(self):
        self.left = []
        self.right = []

    def addNum(self, num):
        if not self.right or num > self.right[0]:
            heapq.heappush(self.right, num)
        else:
            heapq.heappush(self.left, -num)
        # balancing
        high, low = self.left, self.right
        if len(high) < len(low):
            high, low = low, high
        while len(high) > len(low)+1:
            heapq.heappush(low, -heapq.heappop(high))

    def findMedian(self):
        if not self.left and not self.right:
        	return None
        elif not self.left:
        	return self.right[0]
        elif not self.right:
        	return self.left[0]

        maxLeft = -self.left[0]
        minRight = self.right[0]
        if len(self.left) == len(self.right):
            return (maxLeft + minRight) / 2
        elif len(self.left) > len(self.right):
            return maxLeft
        else: return minRight


if __name__ == '__main__':
	obj = MedianFinder()
	print(obj.findMedian())
	obj.addNum(1)
	print(obj.findMedian())
	obj.addNum(2)
	print(obj.findMedian())
	obj.addNum(3)
	print(obj.findMedian())
