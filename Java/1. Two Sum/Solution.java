import java.util.*;

public class Solution{
    public int[] twoSum(int[] nums, int target) {
        Map<Integer,Integer> map = new HashMap<>();
        for(int i=0; i<nums.length; i++){
            int find = target - nums[i];
            if(map.containsKey(find) && i!=map.get(find)){
                return new int[]{i, map.get(find)};
            }else{
                map.put(nums[i],i);
            }
        }
        throw new IllegalArgumentException("no result");
    }
}