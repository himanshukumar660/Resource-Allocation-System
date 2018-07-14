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

num_of_room = 9

original_allotment = {}

for each in range(1, num_of_room+1):
	original_allotment[each] = each

#The prefrance added by the user/students
pref = {
	1:{2,6},
	2:{3},
	3:{4},
	4:{5},
	5:{1,2},
	6:{7},
	7:{8},
	8:{9,5},
	9:{1}
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




















