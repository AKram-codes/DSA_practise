class TwoSum:
    def find_indices(self,nums,target):
        d = {}
        for i,num in enumerate(nums):
            complement = target - num
            if complement in d:
                return [d[complement],i]
            d[num]=i
def main():
    ts = TwoSum()
    print(ts.find_indices([2,7,11,15],9))
    print(ts.find_indices([3,2,4],6))
    print(ts.find_indices([3,3],6))
if __name__ == "__main__":
    main()
