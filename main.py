from colorama import Fore, Back, Style
from tqdm import tqdm
from time import sleep

AccountsDone = {}
Words = ['@hotmail','@outlook','@live']

class Main():
    def CutMailStart(self):
        try:
            with open('accs.txt','r+',encoding='utf-8') as AccountFile:
                Reading = AccountFile.read().split('\n')
                
                for i in Reading:
                    AccDone = i.split(':')
                    AccountsUpdate = str(AccDone[1]).split(' ')

                    for a in Words:
                        FindText = AccDone[0].find(a)
                        if FindText != -1: AccountsDone[AccDone[0]] = AccountsUpdate[0]
                        continue


            if AccountsDone.__len__() >= 1: pass
            else: return print(Fore.RED + 'NORMAL MAILS NOT FOUND' + '\n')
            with open('Done.txt','w',encoding='utf-8') as File:
                pbar = tqdm(AccountsDone.items(),ncols=80)
                for i,o in pbar:
                    pbar.colour = 'GREEN'
                    if self.Mode == 'boltfn': File.write(f'{i}:{o}' + '\n')
                    elif self.Mode == 'home': File.write(f'{i} {o}' + '\n')
                    pbar.set_description(f"CUT OFF IN PROGRESS: {i}")

                Hotmail,Outlook,Live = [],[],[]
                for Mail in AccountsDone:
                    if str(Mail).find('@hotmail') != -1: Hotmail.append(Mail)
                    if str(Mail).find('@outlook') != -1: Outlook.append(Mail)
                    if str(Mail).find('@live') != -1: Live.append(Mail)
                
                print(Fore.GREEN + f'RESULT: \n HOTMAIL: {Hotmail.__len__()} {round(Hotmail.__len__() / AccountsDone.__len__() * 100)}% \n OUTLOOK: {Outlook.__len__()} {round(Outlook.__len__() / AccountsDone.__len__() * 100)}% \n LIVE: {Live.__len__()} {round(Live.__len__() / AccountsDone.__len__() * 100)}% \n')
                print(Fore.GREEN + 'DONE, CUT OFF: ' + str(AccountsDone.__len__()) + '\n')

        except Exception as ex:
            return print(Fore.RED + 'ERR: ' + str(ex) + '\n')

class Interface():
    def ChoiceMode():
        try:
            Mods = ['BoltFN Mail Cutter','Base Mail Cutter']
            MainClass = Main()
            for i in range(Mods.__len__()): print(Fore.GREEN + f'[{i}] {Mods[i]}')
            UserAnswer = str(input('\n' + Fore.GREEN + 'Choice Mode: '))

            if UserAnswer == '0':
                MainClass.Mode = 'boltfn'
                MainClass.CutMailStart()
            elif UserAnswer == '1':
                MainClass.Mode = 'home'
                MainClass.CutMailStart()
            else:
                raise print(Fore.RED + f'Incorrect function: {UserAnswer}' + '\n')
        except: pass

while True:
    Interface.ChoiceMode()
