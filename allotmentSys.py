#We assume that num_of_room and students are the same

#Returns all the cyclic paths from each node
def findCyclePath(visitedNodes ,source, currNode, prevPath):
	
	if visitedNodes[currNode-1]==1 and currNode!=source:
		return -1
	
	elif visitedNodes[currNode-1]==1 and currNode==source:
		if source in cyclePath:
			cyclePath[source].append(prevPath)
		else:
			cyclePath[source] = [prevPath]
		return 1	
	
	elif visitedNodes[currNode-1]==0:
		visitedNodes[currNode-1] = 1
		partPath = prevPath[:]
		for room in pref[currNode]:
			visitedNodes = [0 for a in range(0,num_of_room)]
			for each in prevPath:
				visitedNodes[each-1] = 1
			partPath.append(room)
			findCyclePath(visitedNodes, source, room, partPath)
			partPath = prevPath[:]

#Objective : To maximize the matching of the room allotment list with the user prefrance

num_of_room = 10

original_allotment = {}

for each in range(1, num_of_room+1):
	original_allotment[each] = each

print "Initial Allotments"
for each in original_allotment:
	print each, " : " ,original_allotment[each]


#The prefrance added by the user/students
pref = {
	1:{4,3},
	3:{7,8,6},
	4:{10},
	6:{7},
	7:{8},
	8:{7},
	10:{1}
}

#[in_deg, out_deg]
deg = [[0,0] for a in range(0,num_of_room)]
notChnagingSet = set()

for each in pref:
	deg[each-1][1] += len(pref[each])
	for room in pref[each]:
		deg[room-1][0] += 1

for x,a in enumerate(deg):
	if a[0]>=1 and a[1]>=1:
		continue
	else:
		notChnagingSet.add(x+1)

#delete all those entries whose in_deg or out_deg = 0
for each in notChnagingSet:
	if each in pref:
		del pref[each]

#delete all those entries too
for each in pref:	
	for room in notChnagingSet:
		if room in pref[each]:
			pref[each].remove(room)

cyclePath = {}

for each in pref:
	prevPath = []
	prevPath.append(each)
	for room in pref[each]:
		visitedNodes = [0 for a in range(0, num_of_room)]
		visitedNodes[each-1] = 1 
		prevPath.append(room)
		findCyclePath(visitedNodes, each, room, prevPath)
		prevPath.remove(room)

array_all_path = []

#print cyclePath

for each in cyclePath:
	for each_path in cyclePath[each]:
		array_all_path.append(each_path)


def compSort(a,b):
	if len(a)>len(b):
		return -1
	return 1

array_all_path.sort(cmp=compSort)


set_of_final_path = []

for i,each in enumerate(array_all_path):
	
	partialPath = []

	occupied_rooms = [0 for p in range(0,num_of_room)]

	for room in each:
		occupied_rooms[int(room)-1] = 1

	partialPath.append(each)
	
	for rooms in array_all_path[i:]:

		fg=1
		for room in rooms[:-1]:
			if occupied_rooms[int(room)-1]==1:
				fg=0
				break
			
		if fg==1:
			for room in rooms:
				occupied_rooms[int(room)-1] = 1
			partialPath.append(rooms)

		elif fg==0:
			continue

	set_of_final_path.append(partialPath)

def len_comp(a,b):
	len_a = 0
	len_b = 0
	for each in a:
		len_a = len_a + len(each)
	for each in b:
		len_b = len_b + len(each)

	if len_a>len_b:
		return -1
	return 1

set_of_final_path.sort(cmp=len_comp)


final_allotments = {}

for each in range(1,num_of_room+1):
	final_allotments[each] = each

for each in set_of_final_path[0]:
	for i,room in enumerate(each[:-1]):
		final_allotments[int(room)] = each[i+1] 

for each in pref:
	print each, " : " , pref[each]


satisfaction = 0
print "Final Allotments"
for each in final_allotments:
	print each, " : " ,final_allotments[each]
	if each in pref and final_allotments[each] in pref[each]:
		satisfaction = satisfaction+1
	
print "Satisfaction : ",
print satisfaction*1.0*100/len(pref)