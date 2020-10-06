import statistics
import glob
import os

filename = input("Enter a filename: ")
valid = 0
invalid = 0
answer_key = "B,A,D,D,C,B,D,A,C,C,D,B,A,B,A,C,B,D,A,C,A,A,B,D,D"
answer_key = answer_key.replace(',','')                                                 # remove all character ',' in answer_key string
answer_key_list = list(answer_key)                                                      # convert string to list
list_score = []
file_list_print = []
os.chdir(r'E:\AI\Machine Learning\FUNiX\01_MLP301x_o1 Understanding the basics of concept Machine Learning\data-files\Data Files')              # define directory folder
myFiles = glob.glob('*.txt')                                                                                                                    # list all file .txt to list


if filename in myFiles:                                                                                                                         # check filename in list
    class_file = open("E:/AI/Machine Learning/FUNiX/01_MLP301x_o1 Understanding the basics of concept Machine Learning/data-files/Data Files/"+filename,'r')    
    print("Successfully opened " +filename, " \n")
    print("**** ANALYZING **** \n")
    
    for i in class_file:
        score = 0
        i = i.rstrip()                                                                  # method removes any trailing characters (characters at the end a string including newline), space is the default trailing character to remove.
        data = i.split(',')                                                             # convert to data list and split it by compas
        
        if len(data) ==26 and len(data[0]) == 9 and data[0][0] == 'N' and data[0][1:].isnumeric() == True:                  # length data list = 26 and StudentID = 9 and frist character of StudentID = N
            valid = valid +1

        elif len(data) != 26:
            invalid +=1
            print("Invalid line of data: does not contain exactly 26 values:", i, " \n" )

        elif len(data[0]) != 9 or data[0][0] != 'N' or data[0][1:].isnumeric() != True:
            invalid +=1
            print("Invalid line of data: N# is invalid", i, " \n")
        
        if len(data) ==26:                                                              # Neu do dai cua StudentID <26 thi khi check se bao loi out of index voi truong hop ata[step_data+1] == answer_key_list[step_data]:
            for step_data in range(len(answer_key_list)):                               # Gia su length data = 27 voi dieu kien cau lenh o tren thi step_data co gia tri [0,25]
                if data[step_data+1] == answer_key_list[step_data]:                     # khi do cau lenh if step_data+1 van thoa man
                    score = score + 4
                elif data[step_data+1] == "":
                    pass
                else:
                    score = score -1

        file_list = data[0] + "," + str(score)                                          # Create list file_list gang StudentID,score
        file_list_print.append(file_list)                                               # Append list to export StudentID, score then
        if score >0:
            list_score.append(score)                                                    # Chi in ra gia tri score >0
            
        f = open("E:/AI/Machine Learning/FUNiX/01_MLP301x_o1 Understanding the basics of concept Machine Learning/data-files/Data Files/Expected/"+filename,'w')
        for ele in file_list_print:
            f.write(ele+'\n')

        f.close()
    if invalid == 0:
        print("No errors found! \n")
    print(list_score)
    list_score.sort()                                                                   # sort list_score
    statistics.median(list_score)                                                       # Statistics median of list_score

    print("**** REPORT **** \n")
    print("Total valid lines of data: ",valid)
    print("Total invalid lines of data: ",invalid, " \n")
    print("Mean (average) score: ", round(sum(list_score)/len(list_score),2))
    print("Highest score: ",max(list_score))
    print("Lowest score: ", min(list_score))
    print("Range of scores: ",max(list_score) - min(list_score))
    print("Median score: ",round(statistics.median(list_score),2))
else:
    print ("Sorry, I can't find this filename")