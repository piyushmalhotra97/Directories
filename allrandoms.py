import random
print (random.random())
print (random.randint(1000,9999))
print (random.randrange(999))
print (random.randrange(10,100,5))
print (random.choice([1,2,3,4,5,6]))
print (random.choice('Piyush Malhotra'))
print ("random float uniform(5, 10) : " , random.uniform(5, 10))

list = [20,16,10,5]
random.shuffle(list)
print (" Reshuffled List : " , (list))
