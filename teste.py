from selenium import webdriver
import pyautogui
import time

print("=======================================\n")
print("          Inserindo favoritos          \n")
print("Prefeitura Municipal de Jaguariúna 2023\n")
print("=======================================\n\n")

agend = input("Deseja favoritar CartCid Agendamento? \nResponder com s/n: ")
# cartl = input("Deseja favoritar CartCid Login? \nResponder com s/n: ")
# pec = input("Deseja favoritar PEC? \nResponder com s/n: ")
# grp = input ("Deseja favoritar o GTP? \nResponder com s/n: ")
# cartf = input ("Deseja favoritar CartCid Farmácia? \nResponder com s/n: ")
# cartn = input ("Deseja favoritar o CartCid controle? \nResponder com s/n: ")
# siscn = input ("Deseja favoritar o Siscan? \nResponder com s/n: ")
# sgop = input ("Deseja favoritar o SGOP? \nResponder com s/n: ")
# cadsu = input ("Deseja favoritar CadSus? \nResponder com s/n: ")

if agend in ['S', 's']:
   
    chrome = webdriver.Chrome()
    chrome.get('http://cartcid.jaguariuna.sp.gov.br/saude/assist/pmj_agendamento/security_login/')
    pyautogui.hotkey('ctrl', 'd')
    pyautogui.press('delete')
    pyautogui.write('Agendamento')
    pyautogui.press('enter')
    time.sleep(100000000)
    chrome.quit()

else: 
    print('')

# if cartl in ['S', 's']:

# else: 
#     print('')

# if pec in ['S', 's']:
# else: 
#     print('')

# if grp in ['S', 's']:
# else: 
#     print('')

# if cartf in ['S', 's']:
# else: 
#     print('')

# if cartn in ['S', 's']:
# else: 
#     print('')

# if siscn in ['S', 's']:
# else: 
#     print('')

# if sgop in ['S', 's']:
# else: 
#     print('')

# if cadsu in ['S', 's']:
#     # pyperclip.copy('https://cadastro.saude.gov.br/segcartao/?contextType=external&username=string&contextValue=%2Foam&password=sercure_string&challenge_url=https%3A%2F%2Fcadastro.saude.gov.br%2Fsegcartao&request_id=-5680384401408352939&authn_try_count=0&locale=pt&resource_url=http%253A%252F%252Fcadastro.saude.gov.br%252Fnovocartao%252Frestrito%252FusuarioConsulta.jsp')
# else: 
#     print('')
