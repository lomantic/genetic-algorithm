import data,func,random,operator

print("TEST RESULT")
'''
print(data.distance_A["B"])

#print(func.generateGene())

print((1000/33)**2)
'''
class Route:
    def __init__(self,order,length,fitness):
        self.order = order
        self.length =length
        self.fitness = fitness
    def testPrint(self):
        print("order : "+str(self.order))
        print("length : "+str(self.length))
        print("fitness : "+str(self.fitness))
ex=[]
list=["A",2,3,5]
ex.append(Route(list,123,143))
ex.append(Route(list,123,143))
#classList.append(data.route(genList,distance,fitness)
#print(ex[0].order==ex[1].order)

#ex[0].testPrint()
#ex[1].testPrint()
#a=[1,2,3,4,5,6,7]
list=[]
list.append(data.Route([1,2],1,5))
list.append(data.Route([1,2,3],4,6))
list.append(data.Route([1,2],2,7))
list.append(data.Route([1,2,4],5,11))

#list.length.sort()

list.sort(key=operator.attrgetter('length'))
list[1].testPrint()

a=[1,2,3,4,5]
print(a[:3])
del a[:3]
print(a)

'''
print(a[:])
print(a)
'''
'''
for i in range(4):
    print("Hi")
'''

'''
a=[1,2,3]
b=[43,54,354]
n=random.randint(1,5)
if n==1:
    print("20% posbility")
print(n)

'''
'''
#print(b[a[1]])
randomlist = random.sample(range(0, 5), 5)
print(randomlist)
'''
'''
pickGene=["A","B","C","D","E"]
a=3
del pickGene[a:]

print(pickGene)
'''
'''
pickGene=["A","B","C","D","E"]
pick= random.sample(pickGene,3)
pick.sort()
print(pick)
'''

'''
print(ex[0].order)
print(ex[0].length)
print(ex[0].fitness)

'''
'''
list1=["A",2,3,5]

if ex[0].order==list1:
    print("TRUE")
else:
    print("FALSE")
'''
