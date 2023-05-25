vowel_letters = ['а', 'у', 'о', 'ы', 'и', 'э', 'я', 'ю', 'ё', 'е']
#print('(если просто нажать ввод, будет использована фраза из задачи)')
entered_poems = input('Введите стих, разделяя слова тире, а фразы пробелами: ')
print('Введено: ', entered_poems)
data_let = []
list_phrases = list(entered_poems.split())
ok = True
for i in range(0, len(list_phrases)):
    data_let.append(list(filter(lambda x: x in vowel_letters, list_phrases[i])))
    if i > 0 and len(data_let[i]) != len(data_let[0]): ok = False
if ok: print('Парам пам-пам')
else: print('Пам парам')
