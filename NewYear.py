import os 
import time
from colorama import Fore, Back
os.system('cls')
filename=["file1.txt","file2.txt", "file3.txt","file4.txt", "file5.txt", "file6.txt"]
def animator(filename, delay=1, repeat=10):
	frames=[]
	for name in filename:
		with open(name, "r", encoding="utf-8") as f:
			frames.append(f.readlines())
	for i in range(repeat):
		for frame in frames:
			print(Fore.RED)
			print("".join(frame))
			# print(Back.LIGHTMAGENTA_EX)
			time.sleep(delay)
			os.system('cls')
animator(filename, delay=0.8, repeat=10)
animator(filename, delay=0.2, repeat=20)
animator(filename, delay=3, repeat=5)