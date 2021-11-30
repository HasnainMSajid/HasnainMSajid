

out = open('energy_data.out','a')
Indices = [0.0, 0.5, 1.0, 1.5, 2.0, 2.5, 3.0, 3.5, 4.0, 4.5, 5.0, 5.5, 6.0, 6.5, 7.0, 7.5, 8.0, 8.5, 9.0]
#x = [0, 5]

for value in (Indices):
	x = [0.0, 0.5, 1.0, 1.5, 2.0, 2.5, 3.0, 3.5, 4.0, 4.5, 5.0, 5.5, 6.0, 6.5, 7.0, 7.5, 8.0, 8.5, 9.0]
	for i in (x):
		#values = str(x)
		file = open('SlipAA_XY_' + str(value)+'_'+ str(i)+'/slipAA.out','r')
		data = file.readlines()
		Results=[]
		for line in data:
			if ' Start   directory: /users/' in line:
				directory_name = line
				#print(line)
				file_names = directory_name.split('/')[7] 
				Results.append(file_names)

		for linenum, line in enumerate(data):
			if 'AMS application finished' in line:
				NT = linenum + 1
				NORMAL_TERMINATION = data[NT]
		for lines in data:
			if len(lines.split())==4 and lines.split()[0] == 'Total'  and  lines.split()[1] == 'Energy' and lines.split()[2] == '(hartree)':
				Energy = (str(lines.split()[3]))
				#print(Energy)
				Results.append(Energy)
				#print(Results)
				data = str(Results)
				#print(data)
				A = data.split(',')[0]
				Name = A.split("'")[1]
				#print(Name)
				ABC = str(data.split(',')[1])
				Energy = str(ABC.split("'")[1])	
				#print(Energy)
				#out.write(str(Results)+ '\t'+ (NORMAL_TERMINATION)+'\n')	
				out.write((Name)+ '\t'+ (Energy)+'\t'+(NORMAL_TERMINATION))
