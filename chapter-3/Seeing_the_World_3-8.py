##Here Description of exersice Guest_List_3-8

like_places = ['japan','italy', 'peru', 'russia', 'norway']
print(f'Original List: \n{like_places}')
##########################################################################################################
print(f'\nAlphabetical: \n{sorted(like_places)}')                       #ordenando alphabetical sin que sea permanent
#print(f'\nOriginal List: \n{like_places}')
##########################################################################################################
print(f'\nReverse-alphabetical: \n{sorted(like_places, reverse=True)}') #ordenando reverse-alphabetical sin que sea permanent
print(f'\nOriginal List: \n{like_places}')
##########################################################################################################
like_places.reverse()
print(f'\nReverse List: \n{like_places}')
##########################################################################################################
like_places.reverse()
print(f'\nReverse Reverse (so Original) List: \n{like_places}')
##########################################################################################################
like_places.sort()
print(f'\nAlphabetical: \n{like_places}')         #ordenando alphabetical con que sea permanent

like_places.sort(reverse=True)
print(f'\nReverse-alphabetical: \n{like_places}') #ordenando reverse-alphabetical con que sea permanent
#print(f'\nOriginal List: \n{like_places}')