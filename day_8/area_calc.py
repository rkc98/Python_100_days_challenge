
import math
def calc_area(height,width,cover):
    sum=height*width
    num_of_cans=math.ceil(sum/cover)
    print(sum)
    print(num_of_cans)

calc_area(8,6,5)