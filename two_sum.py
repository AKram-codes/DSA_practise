class TwoSum:
    def find_indices(self,nums,target):
        d = {}
        for i,num in enumerate(nums):
            complement = target - num
            if complement in d:
                return [d[complement],i]
            d[num]=i
        return None
    def find_indices_sorted(self,nums,target):
        left = 0
        right = len(nums)-1
        while left < right:
            current_sum = nums[left] + nums[right]
            if current_sum == target:
                return [left,right]
            if current_sum < target:
                left += 1
            else:
                right -= 1
        return None
def main():
    ts = TwoSum()
    print(ts.find_indices([2,7,11,15],9))
    #print(ts.find_indices([3,2,4],6))
    #print(ts.find_indices([3,3],6))
    #print(ts.find_indices_sorted([2,7,11,15],9))
if __name__ == "__main__":
    main()
