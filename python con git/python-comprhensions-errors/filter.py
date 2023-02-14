numbers = [1,2,3,4]
new_numbers = list(filter(lambda x: x % 2 == 0, numbers))



matches = [
  {
    'home_team': 'Bolivia',
    'away_team': 'Uruguay',
    'home_team_score': 3,
    'away_team_score': 1,
    'home_team_result': 'Win'
  },
  {
    'home_team': 'Brazil',
    'away_team': 'Mexico',
    'home_team_score': 1,
    'away_team_score': 1,
    'home_team_result': 'Draw'
  },
  {
    'home_team': 'Ecuador',
    'away_team': 'Venezuela',
    'home_team_score': 5,
    'away_team_score': 0,
    'home_team_result': 'Win'
  },
]



new_list = list(filter(lambda item: item['home_team_result'] == 'Win', matches))
#print(new_list)
#print(len(new_list))



def filter_by_length(words):
   # Escribe tu solución 👇
   new_words = list(filter(lambda word: len(word) >= 4, words))
   return new_words

words = ['amor', 'sol', 'piedra', 'día']
response = filter_by_length(words)
print(response)