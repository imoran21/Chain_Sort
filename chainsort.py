
print '''
This is a grouping algorithm designed to take a list of tuples and 
find the values that link together while also designating when a duplicate tuple occurs. 
tuple pairs occuring as duplicates will be writted as many times as the duplicate occurs 
this enables one to count how many times a certain tuple pair occurs in a given set of tuples.
  The second function that is after this test case shows an example where duplicates are ignored.
'''

print '''\nThis is the first function that we are testing that accounts for duplicate tupple linkages \n\n
def main(inlist):
	if len(inlist) == 1:
		return inlist



	left_tuples = [x[0] for x in inlist]
	right_tuples = [x[1] for x in inlist]
	def clusterinator(fset = [], index = 0):
	    if index == 0:
	        fset.append(set(([right_tuples[index],left_tuples[index]])))
	        index = index +1
	        #[[a,b]]
	
	    	return clusterinator(fset, index)
	    elif index > 0 and index < len(left_tuples):
	        matches = []
	        for x in fset:
	            left_list_matches = []
	            right_list_matches = []
	            inflag = 0
	            if left_tuples[index] in x:
	            	left_list_matches += (x)
	            	inflag +=1
	            if right_tuples[index] in x:
	            	right_list_matches += (x)
	            	inflag +=2
	            if inflag == 3:
	            	matches = matches + left_list_matches +right_list_matches +[right_tuples[index],left_tuples[index]]
	            elif inflag == 2: 
	            	matches = matches + right_list_matches + [left_tuples[index]]
	            elif inflag == 1:
	            	matches = matches + left_list_matches + [right_tuples[index]]
	            elif inflag == 0:
	                matches = matches + [left_tuples[index], right_tuples[index]]
	
	        matches = set(matches)
	        fset.append(matches)
	        if index == len(left_tuples) -1:
	        	return fset
	        return clusterinator(fset, index+1)
	return [list(x) for x in clusterinator()]

	'''

print '''it does this through a recursive function regulated by the length of the set'''



def main(inlist):
	if len(inlist) == 1:
		return inlist



	left_tuples = [x[0] for x in inlist]
	right_tuples = [x[1] for x in inlist]
	def clusterinator(fset = [], index = 0):
	    if index == 0:
	        fset.append(set(([right_tuples[index],left_tuples[index]])))
	        index = index +1
	        #[[a,b]]
	
	    	return clusterinator(fset, index)
	    elif index > 0 and index < len(left_tuples):
	        matches = []
	        for x in fset:
	            left_list_matches = []
	            right_list_matches = []
	            inflag = 0
	            if left_tuples[index] in x:
	            	left_list_matches += (x)
	            	inflag +=1
	            if right_tuples[index] in x:
	            	right_list_matches += (x)
	            	inflag +=2
	            if inflag == 3:
	            	matches = matches + left_list_matches +right_list_matches +[right_tuples[index],left_tuples[index]]
	            elif inflag == 2: 
	            	matches = matches + right_list_matches + [left_tuples[index]]
	            elif inflag == 1:
	            	matches = matches + left_list_matches + [right_tuples[index]]
	            elif inflag == 0:
	                matches = matches + [left_tuples[index], right_tuples[index]]
	
	        matches = set(matches)
	        fset.append(matches)
	        if index == len(left_tuples) -1:
	        	return fset
	        return clusterinator(fset, index+1)
	return [list(x) for x in clusterinator()]

	


####################
''' TESTS '''
#####################



t1 = '''Test 1'''

print '\n' + t1
print 'Control case...'	
inlist_1 = [('a','b')]
test_case_1 = main(inlist_1)
print 'In: ', inlist_1
print 'Out: ', test_case_1
 
t2 = '''Test 2'''

print '\n' + t2
print 'Control case...'	
inlist_2 = [('a','b'),('c','d')]
test_case_2 = main(inlist_2)
print 'In: ', inlist_2
print 'Out: ', test_case_2
	

t3 = '''Test 3'''
print '\n' + t3
print 'Control case...'	
inlist_3 = [('a','b'),('c','d'),('e','f')]
test_case_3 = main(inlist_3)
print 'In: ', inlist_3
print 'Out: ', test_case_3




t4 = '''Test 4'''
print 'Link between 2 tuples'
print '\n' + t4
inlist_4 = [('a','b'),('a','d')]
test_case_4 = main(inlist_4)
print 'In: ', inlist_4
print 'Out: ', test_case_4
       

t5 = '''Test 5'''
print 'Duplicate tuple gets added'
print '\n' + t5
inlist_5 = [('a','b'),('b','a')]
test_case_5 = main(inlist_5)
print 'In: ', inlist_5
print 'Out: ', test_case_5
              
t6 = '''Test 6'''
print '\n' + t6
print 'Link between 2 tuples and one non linked tuple'
inlist_6 = [('a','b'),('c','d'),('e','a')]
test_case_6 = main(inlist_6)
print 'In: ', inlist_6
print 'Out: ', test_case_6
              


t7 = '''Test 7'''
print '\n' + t7
print 'Multiple duplicates get added correctly'
inlist_7 = [('a','b'),('c','d'),('e','a'),('a','b'),('c','d'),('e','a')]
test_case_7 = main(inlist_7)
print 'In: ', inlist_7
print 'Out: ', test_case_7


t8 = '''Test 8'''
print '\n' + t8
print 'linkage between a larger set of tuples'
inlist_8 = [('a','b'),('c','d'),('e','a'),('h','i'),('j','h'),('z','a')]
test_case_8 = main(inlist_8)
print 'In: ', inlist_8
print 'Out: ', test_case_8
              

print '\n\n\n\n\n'

print ''' \nThis is the test of the second version of the function that only \n
adds unique values in the tuple linkage set'''

print '''This is the second function that ignores duplicates\n\n
def main_without_duplicates(inlist):
	if len(inlist) == 1:
		return inlist



	left_tuples = [x[0] for x in inlist]
	right_tuples = [x[1] for x in inlist]
	def clusterinator(fset = [], index = 0):
	    if index == 0:
	        fset.append(set(([right_tuples[index],left_tuples[index]])))
	        index = index +1
	        #[[a,b]]
	
	    	return clusterinator(fset, index)
	    elif index > 0 and index < len(left_tuples):
	        matches = []
	        for x in fset:
	            left_list_matches = []
	            right_list_matches = []
	            inflag = 0
	            if left_tuples[index] in x:
	            	left_list_matches += (x)
	            	inflag +=1
	            if right_tuples[index] in x:
	            	right_list_matches += (x)
	            	inflag +=2
	            if inflag == 3:
	            	matches = matches + left_list_matches +right_list_matches +[right_tuples[index],left_tuples[index]]
	            elif inflag == 2: 
	            	matches = matches + right_list_matches + [left_tuples[index]]
	            elif inflag == 1:
	            	matches = matches + left_list_matches + [right_tuples[index]]
	            elif inflag == 0:
	                matches = matches + [left_tuples[index], right_tuples[index]]
	
	        matches = set(matches)
	        fset.append(matches)
	        if index == len(left_tuples) -1:
	        	return fset
	        return clusterinator(fset, index+1)
	cluster =  [list(x) for x in clusterinator()]
	cluster_unique = []
	for x in cluster:
		if [a for a in sorted(x)] not in cluster_unique:
			cluster_unique.append([a for a in sorted(x)])
	return cluster_unique
\n\n
'''

def main_without_duplicates(inlist):
	if len(inlist) == 1:
		return inlist



	left_tuples = [x[0] for x in inlist]
	right_tuples = [x[1] for x in inlist]
	def clusterinator(fset = [], index = 0):
	    if index == 0:
	        fset.append(set(([right_tuples[index],left_tuples[index]])))
	        index = index +1
	        #[[a,b]]
	
	    	return clusterinator(fset, index)
	    elif index > 0 and index < len(left_tuples):
	        matches = []
	        for x in fset:
	            left_list_matches = []
	            right_list_matches = []
	            inflag = 0
	            if left_tuples[index] in x:
	            	left_list_matches += (x)
	            	inflag +=1
	            if right_tuples[index] in x:
	            	right_list_matches += (x)
	            	inflag +=2
	            if inflag == 3:
	            	matches = matches + left_list_matches +right_list_matches +[right_tuples[index],left_tuples[index]]
	            elif inflag == 2: 
	            	matches = matches + right_list_matches + [left_tuples[index]]
	            elif inflag == 1:
	            	matches = matches + left_list_matches + [right_tuples[index]]
	            elif inflag == 0:
	                matches = matches + [left_tuples[index], right_tuples[index]]
	
	        matches = set(matches)
	        fset.append(matches)
	        if index == len(left_tuples) -1:
	        	return fset
	        return clusterinator(fset, index+1)
	cluster =  [list(x) for x in clusterinator()]
	cluster_unique = []
	for x in cluster:
		if [a for a in sorted(x)] not in cluster_unique:
			cluster_unique.append([a for a in sorted(x)])
	return cluster_unique


t1 = '''Test 1'''

print '\n' + t1
print 'Control case...'	
inlist_1 = [('a','b')]
test_case_1 = main_without_duplicates(inlist_1)
print 'In: ', inlist_1
print 'Out: ', test_case_1
 
t2 = '''Test 2'''

print '\n' + t2
print 'Control case...'	
inlist_2 = [('a','b'),('c','d')]
test_case_2 = main_without_duplicates(inlist_2)
print 'In: ', inlist_2
print 'Out: ', test_case_2
	

t3 = '''Test 3'''
print '\n' + t3
print 'Control case...'	
inlist_3 = [('a','b'),('c','d'),('e','f')]
test_case_3 = main_without_duplicates(inlist_3)
print 'In: ', inlist_3
print 'Out: ', test_case_3




t4 = '''Test 4'''
print 'Link between 2 tuples'
print '\n' + t4
inlist_4 = [('a','b'),('a','d')]
test_case_4 = main_without_duplicates(inlist_4)
print 'In: ', inlist_4
print 'Out: ', test_case_4
       

t5 = '''Test 5'''
print 'Duplicate tuple DOES NOT gets added'
print '\n' + t5
inlist_5 = [('a','b'),('b','a')]
test_case_5 = main_without_duplicates(inlist_5)
print 'In: ', inlist_5
print 'Out: ', test_case_5
              
t6 = '''Test 6'''
print '\n' + t6
print 'Link between 2 tuples and one non linked tuple'
inlist_6 = [('a','b'),('c','d'),('e','a')]
test_case_6 = main_without_duplicates(inlist_6)
print 'In: ', inlist_6
print 'Out: ', test_case_6
              


t7 = '''Test 7'''
print '\n' + t7
print 'Multiple duplicates DO NOT get added, Only unique values'
inlist_7 = [('a','b'),('c','d'),('e','a'),('a','b'),('c','d'),('e','a')]
test_case_7 = main_without_duplicates(inlist_7)
print 'In: ', inlist_7
print 'Out: ', test_case_7


t8 = '''Test 8'''
print '\n' + t8
print 'linkage between a larger set of tuples'
inlist_8 = [('a','b'),('c','d'),('e','a'),('h','i'),('j','h'),('z','a')]
test_case_8 = main_without_duplicates(inlist_8)
print 'In: ', inlist_8
print 'Out: ', test_case_8
              


t9 = '''Test 9'''
print '\n' + t9
print 'linkage between an even larger set of tuples'
inlist_9 = [('a','b'),('c','d'),('e','a'),('h','i'),('j','h'),('z','a'),('ss','aa'),('os','aa'),('g','a')]
test_case_9 = main_without_duplicates(inlist_9)
print 'In: ', inlist_9
print 'Out: ', test_case_9
              


