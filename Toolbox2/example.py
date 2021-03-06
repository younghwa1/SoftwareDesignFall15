# ToolBox2
# created on Tue Nov 03 20:20:20 2015
# @author: YeongHwa Kim
""" Analyzes the word frequencies in a book downloaded from
	Project Gutenberg """

import string

#Open the file
file_name = 'pg32325.txt'
f = open(file_name, 'r')

#Make the file to list composed of sentencese
lines = f.readlines()
curr_line = 0
while lines[curr_line].find('START OF THIS PROJECT GUTENBERG EBOOK') == -1:
    curr_line += 1
lines = lines[curr_line+1:]

#Definition of function that makes list composed of words
#Input: list(composed of sentences)
#Output: list(composed of words without puctuation)
def get_word_list(lines):    
    lines1 = []
    lines2 = []
    for i in range(len(lines)):
        lines1.append(lines[i].split()) #Split the sentences to words
    for j in range(len(lines1)):
        lines2 = lines2 + lines1[j] #Put the words in one list(lines2)
    for k in range(len(lines2)):
        lines2[k] = lines2[k].strip(string.punctuation) #Remove punctuation
        if lines2[k] != 'I':
            lines2[k] = lines2[k].lower() #Make words lowercase
    return lines2


#Definition of function that gets top n words
#Input: int(n), list(lines)
#Output: list
def get_top_n_words(n, lines):
    word_counts = {}  #Count the words
    for i in lines:
        if i in word_counts:
            word_counts[i] += 1
        else:
            word_counts[i] = 1
    #Ordering by the frequency
    ordered_by_frequency = sorted(word_counts, key=word_counts.get, reverse=True) 
    #Choose the top n words
    num = 0
    top_n_words_list = []
    while num != n:
        top_n_words_list.append(ordered_by_frequency[num])
        num += 1
    return top_n_words_list

print get_top_n_words(100, get_word_list(lines))
