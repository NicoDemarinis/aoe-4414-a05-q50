# ray_ellipsoid_intersection.py
#
# Usage: python3 ray_ellipsoid_intersection.py d_l_x d_l_y d_l_z c_l_x c_l_y c_l_z
#  
# Parameters:
#  
# d_l_x: x-component of origin-referenced ray direction
# d_l_y: y-component of origin-referenced ray direction
# d_l_z: z-component of origin-referenced ray direction
# c_l_x: x-component offset of ray origin
# c_l_y: y-component offset of ray origin
# c_l_z: z-component offset of ray origin
#  
# Output:
#  A description of the script output
#
# Written by Nicola DeMarinis
# Other contributors: None
#
# Optional license statement, e.g., See the LICENSE file for the license.

# import Python modules
import math # math module
import sys  # argv

# initialize script arguments
d_l_x = float('nan') 
d_l_y = float('nan') 
d_l_z = float('nan') 
c_l_x = float('nan') 
c_l_y = float('nan') 
c_l_z = float('nan') 

# parse script arguments
if len(sys.argv)==7:
    d_l_x = float(sys.argv[1]) 
    d_l_y = float(sys.argv[2]) 
    d_l_z = float(sys.argv[3]) 
    c_l_x = float(sys.argv[4]) 
    c_l_y = float(sys.argv[5]) 
    c_l_z = float(sys.argv[6]) 

else:
  print(\
   'Usage: '\
   'python3 ray_ellipsoid_intersection.py d_l_x d_l_y d_l_z c_l_x c_l_y c_l_z'\
  )
  exit()

# "constants"
R_E = 6378.1363
E_E = 0.081819221456

# write script below this line

a = d_l_x**2 + d_l_y**2 + (d_l_z**2)/(1 - E_E**2)
b = 2*(d_l_x*c_l_x + d_l_y*c_l_y + (d_l_z*c_l_z/(1 - E_E**2)))
c = c_l_x**2 + c_l_y**2 + (c_l_z**2)/(1 - E_E**2) - R_E**2

discrim = b**2 - (4*a*c)
if discrim > 0:
    d = (-b - math.sqrt(discrim))/(2*a)
    if d<0:
         d= (-b + math.sqrt(discrim))/(2*a)
         l_x = d*d_l_x + c_l_x
         l_y = d*d_l_y + c_l_y
         l_z = d*d_l_z + c_l_z
    if d>=0:
        l_x = d*d_l_x + c_l_x
        l_y = d*d_l_y + c_l_y
        l_z = d*d_l_z + c_l_z

l_d = [l_x, l_y, l_z]

#Print
print(l_d[0]) # x-component of intersection point
print(l_d[1]) # y-component of intersection point
print(l_d[2]) # z-component of intersection point