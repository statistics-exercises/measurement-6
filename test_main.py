import unittest
from main import *

class UnitTests(unittest.TestCase) :
    def test_code(self):
        myrad = sum(radii) / len(radii) 
        self.assertTrue( np.abs( myrad - averageRadius(radii))<1e-7, "the average radius is not computed correctly" )
        self.assertTrue( inspect.getsource(averageVolume).find("averageRadius")>0,"The averageVolume function does not call averageRadius" )
        rad = averageRadius(radii) 
        myvol = (4/3)*np.pi*rad*rad*rad
        self.assertTrue( np.abs( myvol-averageVolume(radii) )<1e-7, "The averageVolume function does not compute the average volume correctly" )
        
