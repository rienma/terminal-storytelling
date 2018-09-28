#IMPORT
import sys, pickle, time

#FUNCTIONS
def open_pickled_list(name):
    with open(name, 'rb') as file:
         return pickle.load(file)

def jump_line(nb_line):
    jump = ["\n"]*nb_line
    return [slow_writing(line,0,0) for line in jump]

def slow_writing(str,speed,nb_line):
    for letter in str:
        sys.stdout.write(letter)
        sys.stdout.flush()
        time.sleep(speed)
    jump_line(nb_line)

def text_spliter(txt):
    return txt.split('**')

def user_question(quest,list_of_a):
    response = str(input(quest))
    while response not in list_of_a:
        print("--> {} <-- not an acceptable answer".format(response))
        response = str(input(quest))
    return response

#PARAM
narrator_speed = 0.05
draw_speed = 0.001

#TO BE DISPLAYED
intro = open_pickled_list('intro')
troll = open_pickled_list('troll_face')

intro_text = text_spliter(
" The aim of the repo is to send a simple folder to friends, on which they will just have ** \
to enter into the folder and run python message.py ! (in the next version it will an executable freezed by PyInstaller)")

#RUN THROUGH
[slow_writing(line,draw_speed,0) for line in intro]
jump_line(2)
answer = user_question(" Want to read a story ? :", ['yes','Yes','Oui','oui','Ja','ja','No','no','nein','Nein','Non','non'])
jump_line(2)
if answer in ['yes','Yes','Oui','oui','Ja','ja']:
    jump_line(2)
    slow_writing(" Write one ! ",narrator_speed,1)
    jump_line(2)
    [slow_writing(line,0.00001,0) for line in troll]
    jump_line(2)
else:
    slow_writing(" Ok too bad !! ",narrator_speed,1)
