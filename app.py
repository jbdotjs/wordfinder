import requests

# API used https://rapidapi.com/twinword/api/word-dictionary

url = "https://twinword-word-graph-dictionary.p.rapidapi.com/definition/"

headers = {
    'x-rapidapi-host': "enter rapidapi host here",
    'x-rapidapi-key': "enter key here"
    }

wordfile = open(r'F:\python\WordsToLearn.txt', 'r')
word_list = wordfile.readlines()

meanings = open('meanings.txt', 'w')
length = len(word_list)

try:
	for w in range(length):
		word=word_list[w]
		
		querystring = {"entry":word}
		response = requests.request("GET", url, headers=headers, params=querystring)
		
		result_code=int(response.json()['result_code'])

		if result_code==200:
			noun=response.json()['meaning']['noun']
			verb=response.json()['meaning']['verb']
			adjective=response.json()['meaning']['adjective']
			adverb=response.json()['meaning']['adverb']


			meanings.write(f'{word}\n {noun}{verb}{adverb}{adjective}\n\n')
			

		else:
			print(f'{word} not found')

except KeyError:
	print(response.json())
	print('KeyError')

meanings.close()
wordfile.close()

