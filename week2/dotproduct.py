import sys

v = [int(sys.argv[1]), int(sys.argv[2]), int(sys.argv[3])]
u = [int(sys.argv[4]), int(sys.argv[5]), int(sys.argv[6])]

dot = v[0]*u[0] + v[1]*u[1] + v[2]*u[2]

v1 = str(v)
v1 = v1.replace("[", "{ ")
v1 = v1.replace("]", " }")
v1 = v1.replace("'", "")

u1 = str(u)
u1 = u1.replace("[", "{ ")
u1 = u1.replace("]", " }")
u1 = u1.replace("'", "")

print("V = {}".format(v1))
print("U = {}".format(u1))
print("V . U = {}".format(dot))
