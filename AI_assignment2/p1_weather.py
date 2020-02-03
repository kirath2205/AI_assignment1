import math

def euclidean_distance(data_point1, data_point2):
    distance=math.sqrt((((data_point1['TMAX']-data_point2['TMAX'])**2)+((data_point1['TMIN']-data_point2['TMIN'])**2)))
    return distance

def read_dataset(filename):

    list_of_lines=list() # used to store all the lines of the rain.txt file in the form of a list of dictionaries
    list_of_words=list() # used to store a line of the rain.txt file after splitting all the words seperated with a space
    
    with open(filename,"rt") as file1:

        for eachline in file1: #iterating through the whole file

            list_of_words.append(eachline.split())


            list_of_lines.append({'DATE':list_of_words[0][0],'PRCP':float(list_of_words[0][1]),'TMAX':float(list_of_words[0][2]),'TMIN':float(list_of_words[0][3]),'RAIN':list_of_words[0][4]})
            #appending dictionaries to the list_of_lines
            list_of_words.clear()

    return list_of_lines





def majority_vote(nearest_neighbours):
    count_true=0
    count_false=0
    for dictionary in nearest_neighbours: #iterating through all the nearest_neighbours

        if(dictionary['RAIN']=='TRUE'):
            count_true=count_true+1
        else:
            count_false=count_false+1

    if(count_true>=count_false):
        return 'TRUE'
    else:
        return 'FALSE'

    count_true=0
    count_false=0

def k_nearest_neighbours(file_name,test_point,k):
    if(test_point['PRCP']==0):
        result='FALSE'

    else:
        list_of_lines_copy=read_dataset(file_name)

        list_of_distances=list()
        for dictionary in list_of_lines_copy: #iterating through all the dictionaries

            distance=euclidean_distance(dictionary,test_point)
            list_of_distances.append(distance) #creating a list of all the euclidean distances from the given test_point to all the

        for i in range(len(list_of_distances)): #performing bubble sort on the according to distances on the list of dictionaries
            for j in range(0,len(list_of_distances)-1):

                if(list_of_distances[j]>list_of_distances[j+1]):
                    t=(list_of_distances[j])
                    list_of_distances[j]=(list_of_distances[j+1])
                    list_of_distances[j+1]=t

                    copy_list=(list_of_lines_copy[j]).copy()
                    list_of_lines_copy[j]=(list_of_lines_copy[j+1]).copy()
                    list_of_lines_copy[j+1]=copy_list.copy()


        result=majority_vote(list_of_lines_copy[0:k]) #finding the k nearest neighbours and finding the majority_vote using majority_vote function

    return result




file_name=input("enter file name  ")
value_of_k=int(input("enter value of k "))
date=input("enter date ")
TMAX=float(input("enter TMAX "))
TMIN=float(input("enter TMIN "))
PRCP=float(input("enter PRCP "))
dictionary={'DATE':date,'TMAX':TMAX,'PRCP':PRCP,'TMIN':TMIN}

print(k_nearest_neighbours(file_name,dictionary,value_of_k))


