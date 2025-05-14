import Modulo115a

# Programa principal
n = Modulo115a.menu("MENU PRINCIPAL".center(55))
o1 = Modulo115a.options("\033[33m1 - \033[34mVer pesssoas cadastradas")
o2 = Modulo115a.options("\033[33m2 - \033[34mCadastrar nova Pessoa")
o3 = Modulo115a.options("\033[33m3 - \033[34mSair do sistema\033[m")
Modulo115a.linha()

# Input
resp = Modulo115a.resp("\033[33mSua opção: \033[m")