

# solution of simultaneous linear equation using numpy(linalg)

# problem
# 2x+4y-2z-2k = -4
# x+2y+4z-3k = 5
# -3x-3y+8z-2k = 7
# -x+y+6z-3k = -7
# x+y+z+k = 1

import numpy as np
import numpy.linalg as lin

a=([[2,4,-2,-2],[1,2,4,-3],[-3,-3,8,-2],[-1,1,6,-3]])
b=np.array([-4,5,7,-7])

print("The solution is: ",lin.solve(a,b))
