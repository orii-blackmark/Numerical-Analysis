from itertools import count

#f0 = lambda x,y,z: (17-y1+2*z1)/20
#f2 = lambda x,y,z: (-18-3*x+z)/20
#f3 = lambda x,y,z: (25-2*x+3*y)/20
x= 0
y=0
z=0
n = int(input("Enter number of iterations: "))
for i in range(n):
    print("NO. Iterations ",i+1)
    x1 = (17-y+2*z)/20
    y1 = (-18-3*x+z)/20
    z1 =(25-2*x+3*y)/20

    x=x1
    y=y1
    z=z1
  
    print("X= %.4f Y= %.4f Z= %.4f"%(x,y,z))




