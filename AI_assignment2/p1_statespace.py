max_jug_1 = (int(input("Enter maximum capacity of jug 1 ")))
max_jug_2 = (int(input("Enter maximum capacity of jug 2 ")))

max_list = list() # a list to store the maximum capacities of the 2 jugs

max_list.append(max_jug_1)
max_list.append(max_jug_2)

print()

s0=list() # a list to store the initial capacities of the 2 jugs
min_jug_1 = (int(input("Enter initial state of jug 1 ")))
min_jug_2 = (int(input("Enter initial state of jug 2 ")))

print()
s0.append(min_jug_1)
s0.append(min_jug_2)


def fill(state,maximum,which):

    state_copy = state.copy() #making a copy of the initial state, so as to not change the initial state in the program
    if(state_copy[which]<maximum[which]):
        state_copy[which]=maximum[which]
    return state_copy   #returning the new state after peforming fill operation

def empty(state,maximum,which):
    state_copy=state.copy() #making a copy of the initial state, so as to not change the initial state in the program
    state_copy[which]=0
    return state_copy  #returning the new state after peforming fill operation


def xfer(state,maximum,source,destination):
    state_copy = state.copy()   #making a copy of the initial state, so as to not change the initial state in the program
    source_copy=state_copy[source]
    destination_copy=state_copy[destination]
    state_copy[destination] = state_copy[destination] + source_copy
    state_copy[source]=state_copy[source]-(maximum[destination]-destination_copy)


    if(state_copy[destination]>maximum[destination]):
        state_copy[destination]=maximum[destination]


    if(state_copy[source]<0):
        state_copy[source]=0

    return state_copy

def succ(s0,maximum):

    print("state in which we do not do anything" ,s0)
    if(s0[0]<maximum[0]):
        print("fill jug 1",fill(s0,maximum,0))
    if(s0[1]<maximum[1]):
        print("fill jug 2",fill(s0,maximum,1))

    if(s0[0]>0):
        print("empty jug 1",empty(s0,maximum,0))
        print("transfer from jug 1 to jug 2",xfer(s0,maximum,0,1))

    if(s0[1]>0):
        print("empty jug 2",empty(s0,maximum,1))
        print("transfer from jug 2 to jug 1",xfer(s0,maximum,1,0))


succ(s0,max_list)

