#!/usr/bin/python
import sys
import numpy as np 

# Difference with respect to periodic boundaries
def periodic_diff(x1, x2, L):
	return ((x1 - x2 + L/2.) % L) - L/2.

# number of disks
N = int(sys.argv[1])
# packing fraction
phi = float(sys.argv[2])
# radius of disks
r = float(sys.argv[3])
# number of configurations
Nc = int(sys.argv[4])

# Calculate Length of box

# area of the disks
A_disks = (np.pi / np.sqrt(r)) * N

# area of the box
A_box = A_disks / phi

# Length of the Box
L = np.sqrt(A_box)

# number of disks thrown
n = 0

# number of tries
tries = 0

# max number of tries
# MC sampling only works phi < ~0.55
maxtries = 10000

while n < Nc:

	rs = np.random.rand(N,2) * L
	overlaps = 0
	tries = tries + 1

	# allocate memory for distance matrix
	dists = np.zeros((N,N))
	for i in range(0,N):
		for j in range(i+1,N):
			r1 = rs[i,:]
			r2 = rs[j,:]
			rij = periodic_diff(r1,r2,L)
			d = np.sqrt(rij[0]**2 + rij[1]**2)
			if d < 2 * r:
				overlaps = 1
				break

		if overlaps == 1:
			break

	if overlaps == 0:
		n = n + 1
		np.savetxt("%d.txt" % n, rs)


	if tries > maxtries:
		break























