from translate import Translator

translator = Translator(to_lang='en')

try:
    with open('/Users/mothilaljadhav/Desktop/Projects/Python/file_i_o/new_txt_file.txt', mode='r') as other_lang:
        text = other_lang.read()


    translation = translator.translate(text)
    print(translation)

except FileNotFoundError:
    print("File path is wrong")
except Exception as e:
    print(e)