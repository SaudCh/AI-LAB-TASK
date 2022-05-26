#check queue is full or not
def isFull(data):
    if len(data)==5:
        return True
    else:
        return False

#check queue is empty or not
def isEmpty(data):
    if len(data)==0:
        return True
    else:
        return False

#entering data if queue not full
def enqueue(n, data):
    if not isFull(data):
        data.append(n)
    else:
        print("The Queue's full")

#removing data untill queue is empty
def dequeue(data):
    if not isEmpty(data):
        return data.pop(0)
    else:
        print("The Queue's already empty")

#returns length of data
def getLength(data):
    return len(data)


def pop(data):
 return data.pop(0)

def isEmptyMain(data):
    if len(data)==0:
        return True
    else:
        return False

def reduc(data):
  for j in range(0,len(processQueue)):
   processQueue[j][1] = processQueue[j][1]-1
  return processQueue

data = []
ptr = open("./content/processes2.csv","r")
data=ptr.read()
data = data.split("\n")
processQueue =[]
for i in range(0,len(data)):
  j = data[i].split(",")
  processQueue.append(j)


for i in range(0,len(data)):
 processQueue[i][1]= int(processQueue[i][1])
print(processQueue)
print("\n")
print("Processes Queued: ", len(processQueue))
print("Processing Started...")

j = 0

while len(processQueue)!=0:
  for j in range(0,len(processQueue)):
    for i in range(0,3):
      print("Processings : ", processQueue[0][0])
      processQueue[0][1] = int(processQueue[0][1])-1

    if int(processQueue[0][1])>=0:
      print("Requing:", processQueue[0][0])
      p = dequeue(processQueue)
      enqueue(p, processQueue)
    if int(processQueue[0][1])<=0:
      print(processQueue[0][0]," finished.")
      dequeue(processQueue)
      print("Processes left in queue: ", len(processQueue))