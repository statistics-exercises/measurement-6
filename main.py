import numpy as np 

def averageRadius( data ) : 
  # You should add code here to calculate the mean
  # of the data set contained in the array called data
  
def averageVolume( data ) :
  # You shoul add code here to call averageRadius.
  # You should then calculate the average volume 
  # by inserting the value of the average average
  # radius that is returned from averageRadius into
  # the formula in the description on the right
  

# You don't need to modify the code from here
radii = np.loadtxt("bubbles.dat")
print("The average volume of the bubbles is", averageVolume( radii ) )
