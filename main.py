if __name__ == '__main__':
    def find_greatest_common_divisor(largeNum, smallNum):

        while largeNum % smallNum > 0:
            remainder = largeNum % smallNum
            largeNum = smallNum
            smallNum = remainder
            print(smallNum)

    print(find_greatest_common_divisor(2234, 542))

    
