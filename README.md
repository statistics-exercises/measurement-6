# Average volume from average radius

In the previous exercise, we calculated the average volume of our bubbles by transforming each of our measured radii into volumes and then averaging.  Suppose we had just been given a paper containing the sentence:

_The average radius of the bubbles was r._

and that we had not been given the raw data on the radii of all the bubbles.  Over this exercise we are thus going to investigate whether we can calculate the average volume, v, of the bubble from this average radius using:

![](https://render.githubusercontent.com/render/math?math=v=\frac{4}{3}\pi\r^3)

The programming task on the left will help to ensure that you understand what we are doing.  __To complete this task you must complete the function called `averageRadius`__. This function takes a NumPy array called `radii` in input.  This array contains the radii of all the bubbles that have been loaded from the file called `bubbles.dat`.  The `averageRadius` function should calculate the average from this input set of radii.  __You then need to complete the function called `averageVolume`.  This second function should call `averageRadius` and then calculate the average volume using the formula above.__   
