# AUTHOR : ABDUL HANAN
# STUDENT ID: 30340284
# START DATE: 17-05-2019
# LAST MODIFIED DATE: 24-05-2019


import re     # importing regular expression library

"""
%%%%%% docstring for functions %%%%%%
function preprocessLine() is defined to take a single input line as string. This functions is required to
extract body from the line and then replace certain special characters with actual words, using a dictionary.
Regular expressions help us to search for a particular string and once found the re.search returns true.
re.sub replaces parts of string with the required ones.

function splitFile() takes the .xml as inputFile, outputFile_question to store questions as txt file,
outputFile_answer to store answers as txt file. re.search is used to check the post type and each is then
preprocessed using the other method to clean its body. Finally the line is appended to a text file
"""
def preprocessLine(inputLine):
    # initialising a dictionary
    dic = {"&amp;": "&", "&quot;": "\"", "&apos;": "\'", "&gt;": ">", "&lt;": "<", "&#xA;": " ", "&#xD;": " "}
    body = re.search(r'Body="(.*)', inputLine, re.DOTALL).group(1)  # extract body from inputLine
    for key in dic.keys():
        while re.search(key, body):  # loops until it removes all key instances
            body = re.sub(key, dic[key], body)
    inputLine = re.sub(r'<.*?>|\"\s/>', "", body)  # removes tags by substituting them with empty space
    return inputLine

def splitFile(inputFile,outputFile_question,outputFile_answer):

    inputList = open(inputFile, mode='r', encoding='utf-8').readlines() # reading inputFile as text

    outputFile_question = open(outputFile_question, mode='w+', encoding='utf-8')  # output write text file for questions

    outputFile_answer = open(outputFile_answer, mode='w+', encoding='utf-8')  # output write text file for answers
    for line in range(0, len(inputList)):  # loop to read each line of the list inputList
        if re.search(r'PostTypeId="1"', inputList[line]):  # searches for PostType 1
            outputFile_question.write(preprocessLine(inputList[line]))  # writes the line to the text file

        elif re.search(r'PostTypeId="2"', inputList[line]):    # searches for PostType 2
            outputFile_answer.write(preprocessLine(inputList[line]))  # writes the line to the text file
    outputFile_question.close()  # closes the text file
    outputFile_answer.close()


if __name__ == "__main__":
    f_data = "data.xml"
    f_question = "question.txt"
    f_answer = "answer.txt"

    splitFile(f_data, f_question, f_answer)
