import random
import string
from pprint import pprint
words_list = [
    {"word": "Yemen"  , "question": "Country?"},
    {"word": "Forg"   , "question": "Country?"},
    {"word": "yes"    , "question": "Anser?"},
    {"word":"July", "question":"The seventh month of the year"},
    {"word":"Python", "question":"A programming language"},
    {"word":"ِAlgeria", "question":"The biggest country in Africa"},
    {"word":"Happy", "question":"Opposite of sad"},
    {"word":"Manila", "question":"The capital of the Philippines"},
    {"word":"Tigris", "question":"ِA river in Iraq"},
    {"word":"Joe Biden", "question":"The president of America "},
    {"word":"Abdel Halim Hafez", "question":"An Egyptian singer"},
    {"word":" censorious", "question":"The synonym of critical"},
    {"word":"S400", "question":"Air missile system"},
    {"word": "orang", "quest": "what is orang color?"},
    {"word": "red", "quest": "what is appale color?"},
    {"word": "yallow", "quest": "what is banana color?"},
    {"word": "rose", "quest": "what is Strawberry color?"},
    {"word": "green", "quest": "what is watermelon color?"},
    {"word": "black", "quest": "what is Grape color?"},
    {"word": "blue", "quest": "what is Cranberries color?"},
    {"word": "white", "quest": "what is fig color?"},
    {"word": "browen", "quest": "what is Kiwi color?"},
    {"word": "darkgreen", "quest": "what is avocado color?"},
    {"word": "songs", "question": "which You listen everyday?"},
    {"word": "nliy", "question": "Her most important work is a movie and men.?"},
    {"word": "Om Klthom", "question": "The Lady of Arabic Singing?"},
    {"word": "pm", "question": "night time?"},
    {"word": "gta", "question": " still car  game?"},
    {"word": "china", "question": "From Southeast Asian countries?"},
    {"word": "go", "question": "form somewhere?"},
    {"word": "Sun", "question": "the biggest start in our galaxy?"},
    {"word": "okay", "question": "when everything is fain?"},
    {"word": "spong pop", "question": "Who lives in the sea and people are loved it ?"},
    {"word": "left", "question": "Which way is anti-clockwise, left or righ?"},
    {"word": "lgloo", "question": " What do you call a house made of ice?"},
    {"word": "nile", "question": " Which is the longest river on the earth?"},
    {"word": "Japan", "question": "Which country is called the land of rising sun?"},
    {"word": "mars", "question": " Which planet is known as the Red Planet?"},
    {"word": "skin", "question": " Which is the most sensitive organ in our body?"},
    {"word": "India", "question": " The largest 'Democracy' in the world?"},
    {"word": "water", "question": "What makes up (approx.) 80% of our brain's volume?"},
    {"word": "Ghana", "question": " Which African nation is famous for chocolate?"},
    {"word": "red", "question": "What is the top color in a rainbow?"},
    {"word": "lago", "question": " What is the name of the main antagonist in the Shakespeare play Othello "},
    {"word": "four", "question": "How many human players are there on each side in a polo match ?"},
    {"word": "feb", "question": " Which month of the year has the least number of days"},
    {"word": "sty", "question": " Where does a pig live?"},
    {"word": "nose", "question": " We smell with our?"},
    {"word": "tibet", "question": " Which place is known as the roof of the world?"},
    {"word": "tin", "question": " What element is denoted by the chemical symbol Sn in the periodic table?"},
    {"word": "krone", "question": " What is the currency of Denmark?"},
    {"word": "knee", "question": " In which part of your body would you find the cruciate ligament?"},
    {"word": "east", "question": " In which direction does the sun rise ?"},
    {"word":"Sky", "question":"something is starting with s \'b\'"},
    {"word":"Sedney", "question":"A capital city of Australia"},
    {"word":"Popup", "question":"Alert message"},
    {"word":"FTP", "question":"standard for File Transfer Protocol"},
    {"word":"Taxes", "question":"The position of Dallas"},
    {"word":"Islam", "question":"What your religion"},
    {"word":"Team", "question":"meaning of co-workers"},
    {"word":"Koyoto", "question":"The name of Japan anime city \'C\'"},
    {"word":"Vaccine", "question":"Synonym of medicine"},
    {"word":"Dark", "question":"The opposite of \'light\'"},
    {"word": "songs", "question": "which You listen everyday?"},
    {"word": "lion", "question": "who is the king of the jungle?"},
    {"word": "Om Klthom", "question": "The Lady of Arabic Singing?"},
    {"word": "Oval", "question": "Shape of Egg is?"},
    {"word": "Pluto", "question": " It is one of the planets of the solar system?"},
    {"word": "china", "question": "From Southeast Asian countries?"},
    {"word": "purple", "question": "it is mean I trust You?"},
    {"word": "Sun", "question": "the biggest start in our galaxy?"},
    {"word": "Roma", "question": "one of Italia country?"},
    {"word": "sponge pop", "question": "Who lives in the sea and people are loved it ?"},
    {"word":"Tokyo", "question":"Asia's largest city"},
    {"word":"Australia", "question":"The largest island in the world"},
    {"word":"Washington", "question":"What is the capital of America"},
    {"word":"Nile", "question":"The longest river in the world"},
    {"word":"Whale", "question":"The heaviest animal on earth"},
    {"word":"Jupiter", "question":"The largest planet in the solar system"},
    {"word":"Algorithm", "question":"Founder of Algebra"},
    {"word":"Asia", "question":"Largest continents"},
    {"word":"Ostrich", "question":"The fastest bird in the world"},
    {"word":"London", "question":"The city is located the famous Big Ben Watch"},
    {"word":"Friday", "question":"the last day from week?" },
    {"word":"seven", "question":"number of days in week"},
    {"word":"france", "question":"where is effil tower"},
    {"word":"sanaa", "question":"the capital of yemen"},
    {"word":"Cairo", "question":"the capital of Egypt"},
    {"word":"iraq", "question":"Baghdad is a capital of"},
    {"word":"cars", "question":"a taxi is a type of?"},
    {"word":"Egypt", "question":" where is The Nile River'"},
    {"word":"Yemen", "question":"where is Socotra Island"},
    {"word":"Amina", "question":" mother of our massenger"},
    {"word":"Bahrain", "question":"A gulf country that starts with \'b\'"},
    {"word":"Brazil", "question":"A country that hosted World Cup in 2014"},
    {"word":"Cheap", "question":"Opposite of expensive"},
    {"word":"Ready", "question":"A word describing a state"},
    {"word":"Nivada", "question":"The state where Las Vegas is located"},
    {"word":"House", "question":"Where you live"},
    {"word":"Bus", "question":"A form of public transportation"},
    {"word":"Canada", "question":"A country in South America that starts with the letter \'C\'"},
    {"word":"Need", "question":"A word similar to require"},
    {"word":"Die", "question":"The opposite of \'live\'"},
    {"word": "CPU", "question": "Brain of computer is?"},
    {"word": "Camel", "question": "Which animal has hump on its back?"},
    {"word": "Jasmine", "question": "flower is white in colour?"},
    {"word": "Oval", "question": "Shape of Egg is?"},
    {"word": "Winter", "question": " In which season we wear warm clothes?"},
    {"word": "Seven", "question": "colors are there in a rainbow?"},
    {"word": "Red", "question": "primary color?"},
    {"word": "Sun", "question": "principal source of energy for earth?"},
    {"word": "Africa", "question": "continent is known as 'Dark' continent?"},
    {"word": "Asia", "question": "the largest continent in the world?"},
    {"word": "after", "question": "Behind in place or order"},
    {"word": "draft", "question": "A current of air in an enclosed area."},
    {"word": "call", "question": "To say in a loud voice"},
    {"word": "little", "question": "Small in size"},
    {"word": "option", "question": "The act of choosing"},
    {"word": "signal", "question": "A message communicated by such means."},
    {"word": "writer", "question": "a person engaged in writing books"},
    {"word": "follow", "question": "To come or go after"},
    {"word": "camera", "question": " a hand-held photographic device"},
    {"word": "detail", "question": "An individual part or item"},
    {"word": "action", "question": "process of being active"},
    {"word": "beauty", "question": "One that is beautiful, especially a beautiful woman."},
    {"word": "center", "question": "A point or place that is equally distant from the sides "},
    {"word": "detect", "question": "To learn something hidden and"},
    {"word": "orange", "question": "Of the color orange."},
    {"word": "finish", "question": "to stop"},
    {"word": "online", "question": "Connected to a central computer or to a computer network"},
    {"word": "player", "question": "A gambler."},
    {"word": "later", "question": "afterwards"},
    {"word": "dog", "question": " A male animal of the family Canidae"},
    {"word":"Sanaa", "question":"The capital of the state of Yemen is?"},
    {"word":"Baghdad", "question":"capital of Iraq"},
    {"word":"ِWashington", "question":"the capital of america"},
    {"word":"Athena", "question":"the capital of Greece"},
    {"word":"Cairo", "question":"The capital of Egypt"},
    {"word":"Damascus", "question":"ِthe capital of Syria"},
    {"word":"Paris", "question":"the capital of France "},
    {"word":"Ottawa", "question":"Canada's capital"},
    {"word":"Beirut", "question":"the capital of Lebanon"},
    {"word":"S400", "question":"The capital of Tunisia is:"}

 ]

# res = key, val = random.choice(words_list)
# print("The random pair is : " + str(words_list))

words = [random.choice(words_list)\
         for _ in range(5)]
grid_size = 20
grid = [['_' for _ in range(grid_size)] for _ in range(grid_size)]
def print_grid():
     for x in range(grid_size):
       print ('\t' * 5 + ' '.join(grid[x]) )
print_grid()
orientations = ['leftright', 'updown', 'diagonalup', 'diagonaldown']
for word in words :
    word_length = len(word)
    placed = False
    while not placed:
        orientation = random.choice(orientations)
        if orientation == 'leftright':
            step_x = 1
            step_y = 0
        if orientation == 'updown':
            step_x = 0
            step_y = 1
        if orientation == 'diagonalup':
            step_x = 1
            step_y = 1
        if orientation == 'diagonaldown':
            step_x = 1
            step_y = -1
    x_position = random.randint(0, grid_size)
    y_position = random.randint(0, grid_size)

    ending_x = x_position + word_length * step_x
    ending_y = y_position + word_length * step_y
    if ending_x < 0 or ending_x >= grid_size : continue
    if ending_y < 0 or ending_y >= grid_size : continue

    failed = False

    for i in range(word_length):
        character = word[i]
        new_position_x = x_position + i * step_x
        new_position_Y = x_position + i * step_y

        character_at_new_position = grid[new_position_x][new_position_Y]
        if character_at_new_position != '_':
            if character_at_new_position == character:
             continue
        else:
            failed = True
            break
    if failed:
        continue

    else:
        '''
        jkl,;.'
        '''
        for i in range(word_length):
            character = word[i]
            new_position_x = x_position + i*step_x
            new_position_y = y_position + i * step_y

            grid[new_position_x][new_position_y] = character
        placed = True

for x in range(grid_size):
    for y in range(grid_size):
        if (grid[x][y] == '_'):
            grid[x][y] = random.choice()

print_grid()
print("words are")
pprint(words)

















