filename = "cube.obj"
vertexArray = []
file = open(filename, "r")
lines = file.readlines()
vertexCount = 0
normalCount = 0
faceCount = 0
for line in lines:
    line = line.strip()
    if "v " in line:
        vertexCount +=1

    if "vn " in line:
        normalCount +=1
    if "f " in line:
        faceCount +=1
print(faceCount)


