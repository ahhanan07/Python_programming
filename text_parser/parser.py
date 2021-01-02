# AUTHOR : ABDUL HANAN
# STUDENT ID: 30340284
# START DATE: 18-05-2019
# LAST MODIFIED DATE: 24-05-2019
import re
import preprocessData


class Parser:
    """
    %%%%%% docstring for class Parser() %%%%%%
    Class Parser() takes a single string as input. This class includes various methods such as getId(), getPostType(),
    getDateQuarter() and getCleanedBody(). Main function of the class is to iterate through the string and look for
    certain parameters though various methods. It includes cleaning the body, getting the type of the post,
    date and time of the post and Id of the post.
    getId() : returns ID of the post. re.search() is used to extract number. Return value is an integer.
    getPostType(): returns postType() of the string.If postType is 1 means a question and if postType is 2 an answer.
    getDateQuarter(): returns the post date and quarter of the year in the format, yyyyQn e.g 2017Q2.
    getCleanedBody(): pre processes the input string using preprocessLine function from preprocessData
                      Output of this method is a cleaned body with no html tags and special characters.
    getVocabularySize(): takes each line and after being preprocessed removes the punctuations. The string is split and
                         total count of unique words are returned.
    if_parse(): This method is used to check if the inputString can be parsed or not. If the string has a rowId we
               consider it to able for parsing.
    """

    def __init__(self, inputString):
        # Initialising instance variables for the class
        self.inputString = inputString
        self.ID = self.getID()
        self.type = self.getPostType()
        self.dateQuarter = self.getDateQuarter()
        self.cleanBody = self.getCleanedBody()

    def __str__(self):
        # print method for the class. Returns Id, PostType,dateQuarter,vocabSize and cleaned body
        return "ID: {} \nPostType: {} \nCreation Date: {} \nCleanBody: {}VocabSize: {}"\
            .format(self.ID, self.type, self.dateQuarter, self.cleanBody, self.getVocabularySize())

    def if_parse(self):
        if re.search(r'<row Id', self.inputString):  # searches for "row Id" match in the inputString
            return True  # if parsable returns True
        else:
            return False  # if not parsable returns False

    def getID(self):
        if self.if_parse() is True:
            return int(re.search(r'row Id="(\d{1,5})', self.inputString).group(1))  # .group() is used to extract Id
        else:
            return None

    def getPostType(self):
        if self.if_parse() is True:
            if int(re.search(r'PostTypeId="(\d{1,5})', self.inputString).group(1)) == 1:  # searches for post type=1
                return "Question"
            elif int(re.search(r'PostTypeId="(\d{1,5})', self.inputString).group(1)) == 2:  # searches for post type=2
                return "Answer"
            else:
                return "Others"
        else:
            return None

    def getDateQuarter(self):
        if self.if_parse() is True:  # checking the parse condition
            result = re.search(r'CreationDate="(\d{4})-(\d{2})-(\d{2})', self.inputString)  # extracts year,day & month
            if int(result.group(2)) in range(1, 4):   # if loop to check in which quarter the extracted month falls
                return '{}{}'.format(int(result.group(1)), 'Q1')  # returns year and quarter e.g 2016Q1
            elif int(result.group(2)) in range(4, 7):
                return '{}{}'.format(int(result.group(1)), 'Q2')  # returns year and quarter e.g 2016Q2
            elif int(result.group(2)) in range(7, 10):
                return '{}{}'.format(int(result.group(1)), 'Q3')  # returns year and quarter e.g 2016Q3
            elif int(result.group(2)) in range(10, 13):
                return '{}{}'.format(int(result.group(1)), 'Q4')  # returns year and quarter e.g 2016Q4
        else:
            return None

    def getCleanedBody(self):
        if self.if_parse() is True:  # checks for parse condition if true
            return preprocessData.preprocessLine(self.inputString)  # returns clean body using preprocessLine()
        else:
            return None   # returns None if string cannot be parsed

    def getVocabularySize(self):
        if self.if_parse() is True:      # checks parse condition
            # line is first preprocessed using preprocessLine() method of class Parser
            # all the punctuations are removed
            # line is stripped to remove redundant spaces, then converted to lower case and finally split into words.
            # set will consist of unique words of the line and its length  is returned
            # [^\w\s] will not consider words and whitespaces
            return len(set(re.sub(r'[^\w\s]', '', preprocessData.preprocessLine(self.inputString)).
                       strip().lower().split()))
        else:
            return None  # return none if not parsable

