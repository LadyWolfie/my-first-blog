from random import randint as ri
#path = r"C:\Users\Adam\Documents\Sophie\my-first-blog\blog"

def myrat():
	# with open(path+'\\'+"rattraits",'r') as f:
	# 	mylines = f.readlines()

	# traits = [x[-1] for x in mylines]

	# with open(path+'\\'+"ratcolours",'r') as f:
	# 	mylines = f.readlines()

	# colours = [x[-1] for x in mylines]

	# with open(path+'\\'+"ratsizes",'r') as f:
	# 	mylines = f.readlines()

	# sizes = [x[-1] for x in mylines]


	traits = ['curious','outgoing','moody','complicated','friendly','artistic','energetic','intelligent','analytical','loyal','cuddly','loving','athletic','diplomatic','ambitious','cautious','adventurous','wealthy','talented']
	colours = ['all brown','all black','berkshire','mink','silver','brown hooded','silver capped','black capped','marbled']
	sizes = ['teeny tiny','tiny','small','smol','chonky','big','large','medium','fun-sized','bite-sized','hefty']
	gender = ['boy','girl']
	traitNum = ri(0,len(traits)-1)
	trait1 = traits[traitNum]
	traits.remove(trait1)
	trait2 = traits[ri(0,len(traits)-1)]

	start = "Your random rat is a "+sizes[ri(0,len(sizes)-1)]+", "+colours[ri(1,len(colours)-1)]
	mid = " "+gender[ri(0,1)]
	end = " who is "+trait1+" and "+trait2

	myratString = start+mid+end

	return myratString

