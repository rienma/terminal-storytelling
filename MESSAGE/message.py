#IMPORT
import sys, pickle, time

#FUNCTIONS
def slow_writing(str,speed):
    for letter in str:
        sys.stdout.write(letter)
        sys.stdout.flush()
        time.sleep(speed)

def open_pickled_list(name):
    with open(name, 'rb') as file:
         return pickle.load(file)

def jump_line(nb_line):
    jump = ["\n"]*nb_line
    return [slow_writing(line,0.001) for line in jump]

#TO BE DISPLAYED
intro_text = "Hi, my name is Jt Leroy"
troll_face = open_pickled_list('troll_face')

#RUN THROUGH
slow_writing(intro_text,0.05)
jump_line(2)
[slow_writing(line,0.0001) for line in troll_face]
