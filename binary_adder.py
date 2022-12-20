# Binary Adder by Briana Nevarez

class Solution:
  def binary_adder(self, a, b):                                                           # Add a and b using bit wise operations
    mask  = 1                                                                             # A mask to select the bits to be added
    carry = 0                                                                             # Sum carrier
    sum   = 0                                                                             # Sum of a and b
    for i in range(32):                                                                   # Loop through each bit of the operands
      a1 = a & mask                                                                       # Get the ith right-most bit for a
      b1 = b & mask                                                                       # Get the ith right most bit for b
      if(a1 != 0):                                                                        # Normalize the bit                                                                
        a1 = 1
      if(b1 != 0):                                                                        # Normalize the bit  
        b1 = 1
      if(a1 == 1 and b1 == 1 and carry == 1):                                             # Combine the bits and the carry for each possible scenario
        sum |= mask; carry = 1
      elif(a1 == 1 and b1 == 1 and carry == 0):
        carry = 1
      elif(a1 == 1 and b1 == 0 and carry == 1):
        carry = 1
      elif(a1 == 1 and b1 == 0 and carry == 0):
        sum |= mask; carry = 0
      elif(a1 == 0 and b1 == 1 and carry == 1):
        carry = 1
      elif(a1 == 0 and b1 == 1 and carry == 0):
        sum |= mask; carry = 0
      elif(a1 == 0 and b1 == 0 and carry == 1):
        sum |= mask; carry = 0 
      else:                                                                               # a1 == 0 and b1 == 0 and carry == 0
        carry = 0              
      mask <<= 1  
    if(carry == 1):                                                                       # If carry == 1 at the end of the loop, add carry to sum
      sum |= mask
    # print("{:032b}".format(sum))
    return sum                                                                            # Returns sum between a and b

sol = Solution()
assert(sol.binary_adder(0b1001, 0b1101) == 0b10110)
assert(sol.binary_adder(0b1001, 0b0010) == 0b1011)
