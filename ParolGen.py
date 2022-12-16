import argparse
import string
import secrets
import random

class Password:
    def __init__(self, *args):
        self.slov = args
    def dopar(self, dlin = 3):
        par = []
        nom = 0
        for _ in range(dlin):
            if nom > len(self.slov)-1: ####Гарантирует первые - из всех, а дальше рандом
                par += "".join(str(secrets.choice(self.slov[secrets.randbelow(len(self.slov))]))) 
                #nom = 0    — для повторного прохода по словарям
            else:
                par += "".join(str(secrets.choice(self.slov[nom])))
                nom += 1
        random.shuffle(par)
        rez = "".join(par)
        return rez
    
parser = argparse.ArgumentParser(prog = 'Генератор паролей',
                                 description = 'Программа генерирует пароли (неожиданно правда?)',
                                 epilog = 'Если ни один не работает попробуйте включить клавиатуру')
parser.add_argument('-r','--record', action = 'store_true', help = 'Флаг необходимости записи паролей')
parser.add_argument('-f','--filename', default = "paroli.txt", help = 'Имя файла для записи паролей (по умолчанию — paroli.txt)')
parser.add_argument('-a', '--amount', type = int, default = 1, help = 'Количество генерируемых паролей (по умолчанию 1)') 
parser.add_argument('-l', '--len',type = int, default = 5, help = 'Длина генерируемых паролей (по умолчанию 5)') 
parser.add_argument('-p', '--alphabet',
                    default = string.ascii_letters+string.digits,
                    help = 'Алфавит генерируемых паролей(по умолчанию множества цифр, английских строчных и английских прописных)')
args = parser.parse_args()

if args.amount<1:
    print("Должен создаваться минимум 1 пароль")
    exit(0)
if args.len<5:
    print("Длина пароля должна быть больше 4 символов")
    exit(0)
h = Password(args.alphabet)
otv = []
for _ in range(args.amount):
    otv += h.dopar(args.len)+"\n"
otvs = "".join(otv)
if args.record:
    f = open(args.filename,'a', encoding = 'utf-8')
    f.write(otvs)
    f.close()
otv[len(otv)-1] = ''
print("".join(otv))
