import pyautogui
import subprocess
import time
import pandas as pd
import pyperclip

pyautogui.alert('O código vai começar a rodar, não mexa mais o mouse')

# 1. Configura para não dar erro se não achar a imagem de forma rapida
pyautogui.useImageNotFoundException(False)
pyautogui.FAILSAFE = True  # se colocar o mouse nas extremidades da tela o código para de executar


# DEFININDO UMA FUNÇÃO PARA ENCONTRAR IMAGEM
def encontrar_imagem(imagem):
    while not pyautogui.locateOnScreen(imagem, grayscale=True, confidence=0.9):  # Reconhecimento de imagem
        time.sleep(1)
    encontrou = pyautogui.locateOnScreen(imagem, grayscale=True, confidence=0.9)  # vai mostrar o que encontrou
    return encontrou


def escrever_texto(texto):
    pyperclip.copy(texto)
    pyautogui.hotkey("ctrl", "v")
    pyautogui.hotkey('enter')


def direita(posicoes_imagem):
    return posicoes_imagem[0] + posicoes_imagem[2], posicoes_imagem[1] + posicoes_imagem[3] / 2


# ABRIR O PROGRAMA
subprocess.Popen([r"C:\Program Files\Fakturama2\Fakturama.exe"])
encontrou = encontrar_imagem('logoaberto.png')
print('abriu o programa')

# PROGRAMA ESTA ABERTO

# Como fazer para ler varios produtos
tabela_produtos = pd.read_excel('Produtos.xlsx')

for linha in tabela_produtos.index:
    nome = tabela_produtos.loc[linha, 'Nome']
    id = tabela_produtos.loc[linha, 'ID']
    categoria = tabela_produtos.loc[linha, 'Categoria']
    gtin = tabela_produtos.loc[linha, 'GTIN']
    supplier = tabela_produtos.loc[linha, 'Supplier']
    descricao = tabela_produtos.loc[linha, 'Descrição']
    imagem = tabela_produtos.loc[linha, 'Imagem']
    preco = tabela_produtos.loc[linha, 'Preço']
    custo = tabela_produtos.loc[linha, 'Custo']
    estoque = tabela_produtos.loc[linha, 'Estoque']

    # ABRIR O MENU NEW
    encontrou = encontrar_imagem("new.png")
    pyautogui.click(pyautogui.center(encontrou))  # vai clicar no centro do que encontrou
    print('abriu o new')

    time.sleep(3)

    # CLICOU EM NEW PRODUCT
    encontrou = encontrar_imagem("newproduct.png")
    pyautogui.click(pyautogui.center(encontrou))

    time.sleep(3)

    # PREENCHER ITEM NUMBER
    encontrou = encontrar_imagem("item_number.png")
    pyautogui.click(direita(encontrou))
    pyautogui.write(str(id))

    # PREENCHER NAME
    encontrou = encontrar_imagem("name.png")
    pyautogui.click(direita(encontrou))
    pyautogui.write(str(nome))

    # PREENCHER CATEGORY
    encontrou = encontrar_imagem("category.png")
    pyautogui.click(direita(encontrou))
    pyautogui.write(str(categoria))

    # PREENCHER GTIN
    encontrou = encontrar_imagem("gtin.png")
    pyautogui.click(direita(encontrou))
    pyautogui.write(str(gtin))

    # PREENCHER SUPPLIER CODE
    encontrou = encontrar_imagem("supp.png")
    pyautogui.click(direita(encontrou))
    pyautogui.write(str(supplier))

    # PREENCHER DESCRIPTION
    encontrou = encontrar_imagem("description.png")
    pyautogui.click(direita(encontrou))
    pyautogui.write(str(descricao))

    # PREENCHER PRICE GROSS
    encontrou = encontrar_imagem("gross.png")
    pyautogui.click(direita(encontrou))
    preco_texto = f"{preco}:2f".replace(".", ",")  # DEIXAR COM DUAS CASAS DECIMAIS, TROCAR O PONTO PELA VIRCULA
    pyautogui.write(str(preco_texto))

    # PREENCHER PRICE NET
    encontrou = encontrar_imagem("price_net.png")
    pyautogui.click(direita(encontrou))
    custo_texto = f"{custo}:2f".replace(".", ",")  # DEIXAR COM DUAS CASAS DECIMAIS, TROCAR O PONTO PELA VIRCULA
    pyautogui.write(str(custo_texto))

    # PREENCHER PRICE NET
    encontrou = encontrar_imagem("stock.png")
    pyautogui.click(direita(encontrou))
    estoque_texto = f"{estoque}:2f".replace(".", ",")  # DEIXAR COM DUAS CASAS DECIMAIS, TROCAR O PONTO PELA VIRCULA
    pyautogui.write(str(estoque_texto))

    # ABRIR SELECAO DE IMAGEM
    encontrou = encontrar_imagem('select_image.png')
    pyautogui.click(pyautogui.center(encontrou))  # vai clicar no centro do que encontrou

    time.sleep(3)

    encontrou = encontrar_imagem('nomearquivo.png')
    pyautogui.click(direita(encontrou))
    escrever_texto(rf'"C:\Users\juliana.deus\Desktop\codigos\ImagensProdutos\{str(imagem)}"')

    # CLICAR EM SALVAR
    encontrou = encontrar_imagem("save.png")
    pyautogui.click(pyautogui.center(encontrou))
