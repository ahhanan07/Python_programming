# AUTHOR : ABDUL HANAN
# STUDENT ID: 30340284
# START DATE: 21-05-2019
# LAST MODIFIED DATE: 24-05-2019
import re  # import regular expressions
import matplotlib.pyplot as plt   # import matplotlib.pyplot for plotting
import parser   # importing the parser.py file to be used here

'''
%%%%%% docstring for Functions %%%%%%
visualizeWordDistribution(): function takes two arguments, a input file(xml in our case) and a .png argument as a file
to save the plot. input file is read into a list. Then vocab size of each line is calculated using getVocabulary()
method of Parser(). Vocab size is appended to a list. This list is used to create bar plot of count of lines having the
same vocab size into a range. 

visualizePostNumberTrend(): function takes two arguments, a input file(xml in our case) and a .png argument as a file
to save the plot. The function creates a Parser() class object and then calls getDateQuarter() and getPostType()
to get the date-quarter and post type for each line. This data is populated into a list and plotted. Two line graphs are 
plotted. The first one for postType 'Question' and second for postType 'Answer'. For each type the number of questions 
or answers in each date quarter is plotted
'''
def visualizeWordDistribution(inputFile,wordNumberDistribution):
    inputList = open(inputFile, mode='r', encoding='utf-8').readlines()  # reading file into a list
    vocab_size = list()   # list to store vocab size of each line
    for line in range(0, len(inputList)):
        if re.search(r'Body', inputList[line]):  # searches for the string 'Body' in the line
            v_object = parser.Parser(inputList[line])  # creating an object 'vo' for class Parser()
            vocab_size.append(v_object.getVocabularySize())   # append vocab size of line into a list
        else:
            pass
    # Initialising a dictionary to store count of occurrence of vocab_size
    # in each of the ranges
    dict_freq = {'0-10': 0, '10-20': 0, '20-30': 0, '30-40': 0, '40-50': 0, '50-60': 0, '60-70': 0, '70-80': 0,
                 '80-90': 0, '90-100': 0, 'Others(>=100)': 0}
    for i in range(0, len(vocab_size)):     # Checks each vocab_size and counts its occurrence within a particular range
        if vocab_size[i] in range(0, 10):
            dict_freq['0-10'] += 1     # Increment at each occurrence
        elif vocab_size[i] in range(10, 20):
            dict_freq['10-20'] += 1
        elif vocab_size[i] in range(20, 30):
            dict_freq['20-30'] += 1
        elif vocab_size[i] in range(30, 40):
            dict_freq['30-40'] += 1
        elif vocab_size[i] in range(40, 50):
            dict_freq['40-50'] += 1
        elif vocab_size[i] in range(50, 60):
            dict_freq['50-60'] += 1
        elif vocab_size[i] in range(60, 70):
            dict_freq['60-70'] += 1
        elif vocab_size[i] in range(70, 80):
            dict_freq['70-80'] += 1
        elif vocab_size[i] in range(80, 90):
            dict_freq['80-90'] += 1
        elif vocab_size[i] in range(90, 100):
            dict_freq['90-100'] += 1
        elif vocab_size[i] >= 100:
            dict_freq['Others(>=100)'] += 1
    plt.bar(dict_freq.keys(), dict_freq.values(), width=0.8, align='center', color='ygb')  # Plot bar graph
    plt.grid()  # Display grids in the graph
    plt.xlabel('Vocabulary Size Range of inputLines')  # Naming x and y axis
    plt.ylabel('Number of inputLines in each range')
    plt.xticks(rotation=30, horizontalalignment='right')  # Rotating x ticks to avoid overlapping
    plt.title('Word Count Distribution')  # title for the graph
    # Saves the figure, bbox_inches used to fit the image size and face color and frame-on used for visuals
    plt.savefig(wordNumberDistribution, bbox_inches='tight', facecolor='w', transparent=True, frameon=True)
    plt.close()
    return 0


def visualizePostNumberTrend(inputFile,postNumberTrend):
    # you should ﬁrst get the number of questions and answers in each quarter
    inputList = open(inputFile, mode='r', encoding='utf-8').readlines()
    dict_trend_ques = {}  # store yearQuarter(e.g 2016Q1) as key & their count as values for postType Question
    dict_trend_ans = {}   # store yearQuarter(e.g 2016Q1) as key & their count as values for postType Answer

    for line in range(0, len(inputList)):   # loop to read each line of the list inputList
        if re.search(r'Body', inputList[line]):
            trend_object = parser_30340284.Parser(inputList[line])  # creating object for Parser() class
            year_quarter = trend_object.getDateQuarter()            # stores date&quarter returned from getDateQuarter()
            post_type = trend_object.getPostType()                  # stores post type returned from getPostType()
            if post_type is 'Question':
                if year_quarter not in dict_trend_ques:    # populating the dictionary for post type = 'Question'
                    dict_trend_ques[year_quarter] = 0
                dict_trend_ques[year_quarter] += 1

            elif post_type is 'Answer':
                if year_quarter not in dict_trend_ans:   # populating the dictionary for post type = 'Answers'
                    dict_trend_ans[year_quarter] = 0
                dict_trend_ans[year_quarter] += 1
        else:
            pass
    plt.plot(dict_trend_ques.keys(), dict_trend_ques.values(), label='Question', marker='o')
    plt.plot(dict_trend_ans.keys(), dict_trend_ans.values(), label='Answer', marker='o')
    plt.xticks(rotation=60, horizontalalignment='right')  # Rotating x ticks to avoid overlapping
    plt.xlabel('Year-Quarter')     # Naming x and y axis
    plt.ylabel('Q&A count for each Year-Quarter')
    plt.title('Post Number Trend')  # title for the graph
    plt.grid()  # shows grids on graph
    plt.legend()  # shows legends given as label in plt.plot()
    # Saves the figure, bbox_inches used to fit the image size and face color and frame-on used for visuals
    plt.savefig(postNumberTrend, bbox_inches='tight', facecolor='w', transparent=True, frameon=True)
    plt.close()
    return 0


if __name__ == "__main__":
    f_data = "data.xml"  # input xml file
    f_wordDistribution = "wordNumberDistribution.png"  # file to save plot from visualizeWordDistribution()
    f_postTrend = "postNumberTrend.png"  # file to save plot from visualizePostNumberTrend()

    visualizeWordDistribution(f_data, f_wordDistribution)  # calling function visualizeWordDistribution()
    visualizePostNumberTrend(f_data, f_postTrend)   # calling function visualizePostNumberTrend()
