import os

# ioreg -l |grep \"PerformanceStatistics\" | cut -d '{' -f 2 | tr '|' ',' | tr -d '}' | tr ',' '\n'|grep 'Temp\|Fan\|Clock'; done


def CPU_Temp():
	cpu_temp = [each.strip() for each in (os.popen('sudo powermetrics --samplers smc -i1 -n1')).read().split('\n') if each != '']
	for line in cpu_temp:
		if 'CPU die temperature' in line:
			return line.strip('CPU die temperature: ').rstrip(' C')
	return 'CPU Temperature not found'


def GPU_Temp():
	# Will not work with Integrated Intel GPU
	gpu_temp = [each.strip() for each in (os.popen('sudo powermetrics --samplers smc -i1 -n1')).read().split('\n') if each != '']
	for line in gpu_temp:
		if 'GPU die temperature' in line:
			return line.strip('GPU die temperature: ').rstrip(' C')
	return 'GPU Temperature not found'


def all():
	return CPU_Temp() + '\n' + GPU_Temp()


def run():
	import argparse
	parser = argparse.ArgumentParser(description='Get CPU and GPU Temperature')
	parser.add_argument('-c', '--cpu', action='store_true', help='Get CPU Temperature')
	parser.add_argument('-g', '--gpu', action='store_true', help='Get GPU Temperature')
	parser.add_argument('-a', '--all', action='store_true', help='Get CPU and GPU Temperature')
	args = parser.parse_args()
	if args.cpu:
		print(CPU_Temp())
	elif args.gpu:
		print(GPU_Temp())
	elif args.all:
		print(all())
	else:
		print(all())


if __name__ == '__main__':
	print(CPU_Temp())
	print(GPU_Temp())
