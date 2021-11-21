import shelve
sh = shelve.open('library.bdc')
#sh['name'] = 'itay'
#sh['detials'] = {'name': 'itay', 'phone':'1234', 'addess':'tel aviv'}
#sh['number'] = 9
#sh['tuple'] = (4, 3)
#sh['list'] = [1,2,3,4]
print(sh['name'])
print(sh['detials']['phone'])
print(sh['detials'])
sh.close()