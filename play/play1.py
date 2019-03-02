## Ori's Python course
class First_lesson:
    def __init__(self):
        print ("\nLesson #1\n=========\n")
        self.slides()
        self.ex1_strings()

    def slides(self):
        print ("String slides")
        print ("-------------")
        print ('{0}, {1}, {2}'.format('a', 'b', 'c'))
        print ('{2}, {1}, {0}'.format('a', 'b', 'c'))
        print ('Size: {length} by width {width}'.format(length='3', width='4'))
        name = 'Gideon'
        print('My name is: {}'.format(name))
        letters = 'xyz'
        for index, letter in enumerate(letters):  ### NOT CLEAR
            print("{}: {}".format(index, letter))

    def ex1_strings(self):
        '''
        vowels = a, e, i, o, u
         - If first letter in a word is a vowel, add way
           air -> airway
           apple -> appleway
           enchilada -> enchiladaway
           - Otherwise, first letter to end, + ay
           computer -> omputer + c + ay -> omputercay
           table -> able + t + ay -> abletay
        '''
        vowels = ['a','e','i','o','u']
        sent='a a'
        #sent = input("enter sentence: ")
        sent_list = sent.split()
        #print (sent_list)
        outstr = ""
        for word in sent_list:
            if word[0] in vowels:
                outstr += word + 'ay' + ' '
            elif len(word) >1:
                outstr += word[1:] + word[0]+"ay "
            else:
                outstr += word[0] + "ay "
        print ("outstr: ",outstr)

class Second_lesson:
    def __init__(self):
        print ("\nLesson #2\n=========\n")
        self.ex1_lists()
        self.ex2_lists()

    def ex1_lists(self):
        '''
        ## LISTS
        # Ex #1:  Given a list of strings,
           return the count of the number of strings where the string length is 2 or more
           and the first and last chars of the string are the same.'''
        print ("\nEx #1 count in lists")
        strings_list = [['aba', 'xyz', 'aa', 'x', 'bbb'],
                   ['', 'x', 'xy', 'xyx', 'xx'],
                   ['aaa', 'be', 'abc', 'hello']]
        count=[0]*3
        i=0
        for str in strings_list:
            count[i]=0
            for word in str:
                if len(word)>1 and word[0]==word[-1]:
                    count[i]+=1
            i+=1
        print ("Lists ex#1 count= ",count)

    def ex2_lists(self):
        '''ex#2:
        Given two lists sorted in increasing order,
       create and return a merged list of all the elements in sorted order.
       You may modify the passed in lists.
       Ideally, the solution should work in "linear" time, making a single pass of both lists.
       example: ['aa', 'xx', 'zz'], ['bb', 'cc']  -> ['aa', 'bb', 'cc', 'xx', 'zz'] '''
        print ("\nEx #2 merge and sort lists")
        strings_list = [ [['aa', 'xx', 'zz'], ['bb', 'cc']],
                         [['aa', 'xx'],['bb', 'cc', 'zz']],
                         [['aa', 'aa'],['aa', 'bb', 'bb']]]
        count=[0]*3
        i=0
        for lst in strings_list:
            lst[0] += lst[1]
            #print ('lst_i' ,lst[0])
            lst[0].sort()
            print ("sorted ",lst[0])

class Third_lesson():
    ''' You are given a list of movies.
        Write 3 different programs to search for the required movie using 3 different data structures:
        – list of lists, list of dicts, dict of dicts
        Can you state the benefits?
    '''
    def __init__(self):
        print ("\nLesson #3\n=========\n")
        self.get_movies()
        self.read_movie()
        self.search_list_of_lists()
        self.search_list_of_dicts()
        self.search_dict_of_dicts()

    def get_movies(self):
        self.movies_list_of_lists = \
                 [  ['Captain Philips', 133, 'Paul Greengrass'],
                    ['Gravity', 90, 'Alfonso Cuaron'],
                    ['American Hustle', 138, 'David O. Russell']
                    ]

        self.movies_list_of_dicts = \
                [   {'name':'Captain Philips',
	                 'length':133,
                     'director':'Paul Greengrass'},
                    {'name':'Gravity',
                     'length':90,
                     'director':'Alfonso Cuaron',
                     'year': 2013},
	                {'name':'American Hustle',
                     'length':138,
                     'director':'David O. Russell'}
                    ]

        self.movies_dict_of_dicts = {
	            'Captain Philips' : {'length':133, 'director':'Paul Greengrass'},
                'Gravity':          {'length':90,  'director':'Alfonso Cuaron', 'year': 2013},
                'American Hustle' : {'length':138, 'director':'David O. Russell'}}

    def read_movie(self):
        self.movie = input("enter movie name: ")

    def search_list_of_lists(self):
        print("searching in list of lists:")
        for item in self.movies_list_of_lists:
            if item[0]== self.movie:
                print (item)

    def search_list_of_dicts(self):
        print("searching in list of dict:")
        for item in self.movies_list_of_dicts:
            if item['name']== self.movie:
                print (item)

    def search_dict_of_dicts(self):
        print ("searching in dict_of_dicts:")
        if self.movie in self.movies_dict_of_dicts.keys():
            print (self.movies_dict_of_dicts[self.movie])

class Forth_lesson():
    pass


if __name__ == '__main__':
    print ("Ori Python course")
    #a = First_lesson()

    #b = Second_lesson()
    #b.ex1_lists()
    #b.ex2_lists()

    c = Third_lesson()

    #d = Forth_lesson()

