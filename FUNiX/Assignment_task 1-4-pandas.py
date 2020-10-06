import numpy as np
import pandas as pd
import glob
import os
import statistics

filenames = input("Enter a filenames: ")
answer_key = "B,A,D,D,C,B,D,A,C,C,D,B,A,B,A,C,B,D,A,C,A,A,B,D,D"
answer_key = answer_key.replace(',','')                                                 # remove all character ',' in answer_key string
answer_key_list = list(answer_key)                                                      # convert string to list
valid = 0
invalid = 0
list_score = []
score = 0
error = 0
numpy_answer_key = np.array(answer_key_list)                                            # convert list answer key to numpy
df_answer_key = pd.DataFrame(answer_key_list)                                           # convert list answer key to dataframe pandas
df_answer_key = df_answer_key[0:].transpose()                                           # Change dataframe from column to row
export_print = []

os.chdir(r'E:\AI\Machine Learning\FUNiX\01_MLP301x_o1 Understanding the basics of concept Machine Learning\data-files\Data Files')              # define directory folder
myFiles = glob.glob('*.txt')                                                                                                                    # list all file .txt to list

if filenames in myFiles:
    for f in filenames:
        #df_filename = pd.read_csv("E:/AI/Machine Learning/FUNiX/""01_MLP301x_o1 Understanding the basics of concept Machine Learning""/data-files/""Data Files""/"+filenames,header=None, error_bad_lines=False, warn_bad_lines =False).iloc[:,0:26]
        df_filename = pd.read_csv("E:/AI/Machine Learning/FUNiX/""01_MLP301x_o1 Understanding the basics of concept Machine Learning""/data-files/""Data Files""/"+filenames,header=None, sep='\n')
        
    print("Successfully opened " + filenames, " \n")
    print("**** ANALYZING **** \n")
    
    
    df = df_filename[0].str.split(',', expand=True)    
    
    for i in range (len(df)):
        space = 0
        
        if len(df.loc[i][0]) == 9 and df.loc[i][0][0] == "N" and df.loc[i][0][1:].isnumeric() == True and df.count(axis= 1).loc[i] == 26:
            valid += 1

        elif df.count(axis= 1).loc[i] != 26:
            invalid += 1
            print("Invalid line of data: does not contain exactly 26 values:", df.loc[[i]])                             # Muon luc in ra bo header??????????????????
            #print("Invalid line of data: does not contain exactly 26 values:", df.iloc[i,1:])                             # Muon luc in ra bo header??????????????????

        elif len(df.loc[i][0]) == 9 or df.loc[i][0][0] == "N" or df.loc[i][0][1:].isnumeric() == True:
            invalid += 1
            print("Invalid line of data: N# is invalid", df.loc[[i]], " \n")
    

        if len(df.loc[i][0]) == 9 and df.loc[i][0][0] == "N" and df.loc[i][0][1:].isnumeric() == True and df.count(axis= 1).loc[i] == 26:
        #if df.count(axis= 1).loc[i] == 26:
            
            df_compare = df_answer_key.loc[[0]].values == df.loc[[i],1:25].values
            space = (df.loc[[i],1:25] == '').sum(True).values                                      # count so cau hoi khong tra loi (space) dang frame -- chuyen thanh values bang cach them .values
            error = len(answer_key_list) - df_compare.sum() - space[0]                        # error (tra loi sai) = 25 - so cau tra loi dung - so cau khong tra loi (space)            
                                  
            score = (df_compare.sum())*4 - error                                            # score = so cau tra loi dung*4 - so cau tra loi sai
   
            if score > 0:                                                                  # se bao loi do score khong phai kieu value ma la kieu dataframe???????????????????
                list_score.append(score)
                export_list = df.loc[i][0] + ',' + str(list_score[i])
                export_print.append(export_list)
                f = open("E:/AI/Machine Learning/FUNiX/01_MLP301x_o1 Understanding the basics of concept Machine Learning/data-files/Data Files/Expected/"+filenames,'w')               # Export to file .txt
                for ele in export_print:
                    f.write(ele+'\n')
    export_list = df.loc[2][0] + ',' + str(list_score[2])

    print(df.loc[2][0])
    print(list_score[2])   
    list_score.sort()                                                                       # sap xem list theo thu tu tu be den lon de tinh median
    print("**** REPORT ****")
    print("Total valid lines of data: ",valid)
    print("Total invalid lines of data: ",invalid)
    print("Mean (average) score: ", round(sum(list_score)/len(list_score),2))
    print("Highest score: ",max(list_score))
    print("Lowest score: ", min(list_score))
    print("Range of scores: ",max(list_score) - min(list_score))
    print("Median score: ",statistics.median(list_score))
else:
     print ("Sorry, I can't find this filename")            
            
