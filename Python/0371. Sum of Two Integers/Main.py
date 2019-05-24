class Solution:
    
    def getSum_iterative_work(self, a, b):
            """
            :type a: int
            :type b: int
            :rtype: int
            """
            MAX = 0x7FFFFFFF
            MSK = 0xFFFFFFFF

            while b:
                sum_number = a ^ b
                # notice 0 << 1 = 0
                carry = (a & b) << 1
                # if not covert to 32bit , will timeout
                # convert to 32 bit, if not do this, will overflow lead to dead loop
                # can try to debug in test/test_bit.py
                carry &= MSK
                sum_number &= MSK
                a = sum_number
                b = carry
            if a < MAX:
                return a
            else:  # negative
                return ~(a ^ MSK)
'''  javd 代码           
public class AlgoCasts {

  public int getSumRecursive(int a, int b) {
    return b == 0 ? a : getSumRecursive(a^b, (a&b)<<1);
  }

  // Time: O(m), Space: O(1)
  public int getSumIterative(int a, int b) {
    while (b != 0) {
      int sum = a ^ b;
      int carry = (a & b) << 1;
      a = sum;
      b = carry;
    }
    return a;
  }
}
'''