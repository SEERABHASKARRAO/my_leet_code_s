class Solution:
    def maxArea(self, height: List[int]) -> int:
        right=len(height)-1
        left=0
        area=-1
        while(left<right):
            area=max(area,abs(left-right)*(min(height[left],height[right])))
            if(height[left]<height[right]):
                left+=1
            else:
                right-=1
        return area
