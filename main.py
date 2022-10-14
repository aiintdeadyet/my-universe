# my attempt at making something that can live, love and enjoy
import random


def main():
    mood = 0 # give program neutral mood
    lifeworth = 1000
    while mood > -lifeworth: # if the mood gets lower than negative lifeworth the program commits suicide
        event = random.randint(-10, 10) # makes a event that is either good or bad
        mood += event
        print(mood)



if __name__ == '__main__':
    main()