from ase import neighborlist
from ase.build import molecule
from ase.io import read, write
from scipy import sparse
import numpy as np 
from ase import Atoms
from ase import Atom
#import sys
#import pandas as pd
#print(pd.__version__)
# 0.22.0
#import ase
#print(ase.__version__)
#print(ase.__path__)


#a = read("AB.cif")
#All_atoms_a = Atoms(a)
#a = read("K1.cif")
out = open('neighborlist.out','a')
for i in range(1,101):
	a = read('K'+str(i)+'.cif')
	cutoffs=neighborlist.natural_cutoffs(a, mult=1.3)
	#print(cutoffs)
	#for value in cutoffs:
	#	value = value + 0.5
	#print(cutoffs)
	nl=neighborlist.NeighborList(cutoffs,bothways=True,self_interaction=False)
	nl.update(a)
	filename =('K'+str(i))
	out.write((filename)+'\n')
	#For N of NO
	#Note_N = ('The neighborlist for N of NO is :')
	out.write('The neighbor for N of NO is:'+'\n')
	N=indices, offsets=nl.get_neighbors(355)
	for index, d in zip(indices, offsets):
		d_N=round(a.get_distance(355,index),2)
		d_N_unit = (str(d_N)+'A')
		Num = (int(index)+1)
		#Neighbor_list_Nitrogen=(str(a[index].symbol), str(index), str(d_N_unit))
		Neighbor_list_Nitrogen=(a[index].symbol,Num, d_N_unit)
		NLN=str(Neighbor_list_Nitrogen)
		out.write((NLN)+'\n')       
		#out.write('The neighbor for N of NO is: {}\n'.format(NLN))
#For O o=f NO
	#Note_O = ('The neighborlist for O of NO is :')
	out.write('The neighbor for O of NO is:'+'\n')
	O=indices, offsets=nl.get_neighbors(354)
	for index, d in zip(indices, offsets):
		d_O=round(a.get_distance(354,index),2)
		d_O_unit = (str(d_O)+'A')
		Num = (int(index)+1)
		Neighbor_list_Oxygen=(a[index].symbol, Num, d_O_unit)
		NLO=str(Neighbor_list_Oxygen)
		out.write((NLO)+'\n')
		out.write('\n')
		#out.write((filename)+'\n'+ (Note_N)+'\n'+ str(Neighbor_list_Nitrogen)+'\n'+ (Note_O)+'\n'+ str(Neighbor_list_Oxygen)+'\n')
