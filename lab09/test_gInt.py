#!/usr/bin/env python3
# test_gInt - Unit test for gInt class
#
# Timothy McGowan
# 6/18
# CS265 - Lab09
# Python version 3.5.2

import sys
import unittest

from gInt import gInt

class gIntTest( unittest.TestCase ) :

	def setUp( self ) :
	
		self.u1 = gInt( 1, 3)
		self.u2 = gInt( -1, 3)
		self.u3 = gInt( 1, -3)
		self.u4 = gInt( 0 , 3)
		self.u5 = gInt( 1, 0)
		self.u6 = gInt( -1, -3)
		self.u0 = gInt( 0, 0)
		

	def test_add( self ):
		#Addition Test (All numbers positive unless commented otherwise)
		r = self.u1 + self.u1
		self.assertEqual( r, gInt(2,6), 'Addition Failed') #Lhs and Rhs positive
		
		r = self.u2 + self.u1
		self.assertEqual( r, gInt(0, 6), 'Addition Failed') #Lhs positive Rhs-real negative		
	
		r = self.u2 + self.u3
		self.assertEqual( r, gInt(0, 0), 'Addition Failed') #Lhs-real negative Rhs-imag negative

		r = self.u3 + self.u4
		self.assertEqual( r, gInt(1, 0), 'Addition Failed') #Lhs-imag negative Rhs-real zero

		r = self.u0 + self.u0
		self.assertEqual( r, gInt(0, 0), 'Addition Failed') #All zero

		r = self.u6 + self.u6
		self.assertEqual( r, gInt(-2, -6), 'Addition Failed') #All negative

	def test_mul( self ):
		#Multiplication Test (All numbers positive unless commented otherwise)
		r = self.u1 * self.u1
		self.assertEqual( r, gInt(-8,6), 'Multiplication Failed') #All positive

		r = self.u1 * self.u2
		self.assertEqual( r, gInt(-10,0), 'Multiplication Failed') #Rhs-real negative	

		r = self.u1 * self.u3
		self.assertEqual( r, gInt(10,0), 'Multiplication Failed') #Rhs-imag negative

		r = self.u2 * self.u3
		self.assertEqual( r, gInt(8,6), 'Multiplication Failed') #Lhs-real negative Rhs-imag negative

		r = self.u3 * self.u2
		self.assertEqual( r, gInt(8,6), 'Multiplication Failed') #Lhs-imag negative Rhs-real negative	

		r = self.u1 * self.u6
		self.assertEqual( r, gInt(8,-6), 'Multiplication Failed') #Rhs All negative

		r = self.u6 * self.u6
		self.assertEqual( r, gInt(-8,6), 'Multiplication Failed') #All negative

		r = self.u4 * self.u5
		self.assertEqual( r, gInt(0,3), 'Multiplication Failed') #Lhs-real zero Rhs-imag zero
	
		r = self.u5 * self.u4
		self.assertEqual( r, gInt(0,3), 'Multiplication Failed') #Lhs-imag zero Rhs-real negative	
	
		r = self.u1 * self.u0
		self.assertEqual( r, gInt(0,0), 'Multiplication Failed') #Rhs All zero


		r = self.u6 * self.u0
		self.assertEqual( r, gInt(0,0), 'Multiplication Failed') #Lhs All negative Rhs All zero

		r = self.u0 * self.u0
		self.assertEqual( r, gInt(0,0), 'Multiplication Failed') #Lhs and Rhs All zero

	def test_norm( self ):
	
		r = gInt.norm(self.u1)		
		self.assertEqual( r, gInt(1,9), 'Normalization Failed') #Both positive

		r = gInt.norm(self.u2)
		self.assertEqual( r, gInt(1,9), 'Multiplication Failed') #Lhs negative

		r = gInt.norm(self.u3)
		self.assertEqual( r, gInt(1,9), 'Multiplication Failed') #Rhs negative

		r = gInt.norm(self.u4)
		self.assertEqual( r, gInt(0,9), 'Multiplication Failed') #Lhs zero
		
		r = gInt.norm(self.u5)
		self.assertEqual( r, gInt(1,0), 'Multiplication Failed') #Rhs zero

		r = gInt.norm(self.u6)
		self.assertEqual( r, gInt(1,9), 'Multiplication Failed') #Both negative

		r = gInt.norm(self.u0)
		self.assertEqual( r, gInt(0,0), 'Multiplication Failed') #Both zero

if __name__ == '__main__' :
        sys.argv.append( '-v' )
        unittest.main()


