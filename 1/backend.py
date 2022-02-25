"""
Created on Sun Feb 20 16:44:52 2022

@author: mcaptain79
"""
import mysql.connector
from languageTranslator import translate
from nlu import angerDetector
from speechToText import voice_recorder,speech2text
myDB = mysql.connector.connect(user = 'root',password = None,host = 'localhost',database = 'mySql')
cursor = myDB.cursor()
for i in cursor:
    print(i)
#showin user pannel in a loop
while True:
    #choosing to see or post a comment
    choice = input('1)post a comment\n2)see comments\nchoose:')
    if choice == '1':
        choice2 = input('enter movie id: ')
        choice3 = input('1)write comment\n2)record a voice\nchoose: ')
        if choice3 == '1':
            text = input('enter comment: ')
            if angerDetector(text):
                print('sorry your comment violates our terms:(')
            else:
                query1 = 'select count(*) from comment'
                cursor.execute(query1)
                commentId = 0
                for i in cursor:
                    commentId = i[0]
                query2 = 'insert into comment (comment_id,movie_id,comment_text) values (%s,%s,%s)'
                cursor.execute(query2,(int(commentId)+1,int(choice2),text))
                myDB.commit()
                print('comment posted successfuly.thanks for your comment')
        elif choice3 == '2':
            print('you just have 10 seconds:)')
            print('recording voice...')
            voice_recorder()
            print('voice recorded')
            print('converting voice to text please be patient')
            text = speech2text()
            print('your comment:',text)
            if angerDetector(text):
                print('sorry your comment violates our terms:(')
            else:
                query1 = 'select count(*) from comment'
                cursor.execute(query1)
                commentId = 0
                for i in cursor:
                    commentId = i[0]
                query2 = 'insert into comment (comment_id,movie_id,comment_text) values (%s,%s,%s)'
                cursor.execute(query2,(int(commentId)+1,int(choice2),text))
                myDB.commit()
                print('comment posted successfuly.thanks for your comment')
        else:
            print('bad input')
    else:
        comments = []
        choice2 = input('enter your movie id: ')
        query = 'select comment_text from comment where movie_id = %s'
        cursor.execute(query,(choice2,))
        for i in cursor:
            comments.append(i[0])
        choice3 = input('1)english\n2)japanese\n3)arabic\nchoose: ')
        if choice3 == '1':
            for i in comments:
                print(i)
        elif choice3 == '2':
            for i in comments:
                print(translate('en-ja', i))
        elif choice3 == '3':
            for i in comments:
                print(translate('en-ar', i))
        else:
            print('bad input')
                
