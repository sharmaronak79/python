

g_name="abc"
g_movie = None
def hand_shake():
    name=input("what is your name : ")
    print(f'How are you {name} ?')
    print(f'{name} : I am doing great..... ')
    global g_name
    g_name=name
def welcome():
    print(f'How is the weather outside {g_name} !!!!')

def movie(m1,m2):
   # print(f'Have you seen the latest movie {m1} or {m2} ? ')
  # global g_movie
   g_movie = input(print(f'Have you seen the latest movie {m1} or {m2} ? '))
   if g_movie == "Pathan" :
       print("Ohh Shahrukh khan...")
   elif g_movie == "Gadar" :
       print("Ohhh Sunny Paji.....")
   else:
       print("Ohh I have no idea")