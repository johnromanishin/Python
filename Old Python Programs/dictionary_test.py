import time
time_till_pruning = 5.0
cubes = {}
start_time = time.time()
print("--- %s seconds ---" % (time.time() - start_time))
print(cubes)

def add_cube( number ):
    cubes[number] = (time.time()-start_time) # This records the time the value was added

def prune_cubes(time_kill):
    for cube in cubes.keys():
	since_update = (time.time()-start_time-cubes[cube])
	print(since_update)
	if since_update > time_kill:
	    try:
    		del cubes[cube]
	    except KeyError:
    		pass

add_cube('aad')

while(1==1):
   add_cube(993)
   time.sleep(2)
   print(cubes.keys())
   print(type(cubes.keys()))
   prune_cubes(time_till_pruning)
   print(len(cubes.keys()))
#[hex(number)[-3:]]
