
import random
def generate_random_array():
   length = random.randint(1, 10)  
   return [random.randint(1, 100) for _ in range(length)]  
def check_guess(array):
   print("Hádej čísla v poli:", array)
   guess = int(input("Uhádni délku pole: "))
   if guess == len(array):
       print("si zabil!!")
       return 1
   else:
       print("Chyba!")
       return 0
def play_game():
   rounds = random.randint(1, 15)  
   celkove_body = 0
   print("Vítej v zabryho hře!")
   print("Budeš hrát", rounds, "kol.")
   for _ in range(rounds):
       array = generate_random_array()
       celkove_body += check_guess(array)
   print("Konec hry! Celkový počet bodů:", celkove_body)
play_game()