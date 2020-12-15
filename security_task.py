print("________________________AMONG ASS________________________Test 1.0 objective - security")
import random, time, sys, subprocess

f = open('txt.txt', 'w')
i = 0
b = None
m = None
g = 0
c = []
n = []
l = []
p = sys
while i != 5:
    b = str(random.randint(0, 5))
    f.write(b)
    i += 1
    c.append(b)
f.close()

pasw = int(input("Password: "))
n = str(pasw)
l = list(n)

for g in range(4):
    if c[g] != l[g]:
        print("Pasword incorect!")
        sys.exit(0)
    else:
        pass
    
print("Good, you in!")
print("")
print("Starting ...")

for n in range(100):
    print("Downloadind..." + str(n) + "%")
    time.sleep(0.2)

print("Download finished!")

subprocess.Popen("main.py 1", shell=True)
sys.exit(0)