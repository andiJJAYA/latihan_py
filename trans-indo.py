from googletrans import Translator
translator = Translator()

text_indo = input('masukan text dalam bahasa indonesia :')

hasil = translator.translate(text_indo, src='en' ,dest='id')
print('----sebelum----')
print(text_indo)
print('----sesudah----')
print('terjemahanya:', hasil.text)
