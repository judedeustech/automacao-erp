# 🤖 Automação de Cadastro de Produtos em ERP com PyAutoGUI

Script de automação desktop que abre o sistema ERP **Fakturama**, lê uma planilha Excel com dados de produtos e realiza o cadastro completo de cada item automaticamente — sem nenhuma interação manual.

---

## 📁 Estrutura do Projeto

```
📦 automacao-erp/
├── ERP.py                    # Script principal de automação
├── Produtos.xlsx             # Planilha com os dados dos produtos a cadastrar
└── imagens/                  # Screenshots dos elementos da interface (usados pelo PyAutoGUI)
    ├── logoaberto.png        # Tela inicial do Fakturama (confirma que o programa abriu)
    ├── new.png               # Botão "New"
    ├── newproduct.png        # Opção "New Product"
    ├── item_number.png       # Campo Item Number
    ├── name.png              # Campo Name
    ├── category.png          # Campo Category
    ├── gtin.png              # Campo GTIN
    ├── supp.png              # Campo Supplier Code
    ├── description.png       # Campo Description
    ├── gross.png             # Campo Price Gross
    ├── price_net.png         # Campo Price Net
    ├── stock.png             # Campo Stock
    ├── select_image.png      # Botão de seleção de imagem
    ├── nomearquivo.png       # Campo "Nome do arquivo" no seletor de imagem
    └── save.png              # Botão Save
```

---

## ⚙️ Tecnologias Utilizadas

| Tecnologia | Descrição |
|---|---|
| Python 3.x | Linguagem principal |
| PyAutoGUI | Automação de mouse, teclado e reconhecimento de imagem na tela |
| Pyperclip | Cópia e colagem de texto via clipboard |
| Pandas | Leitura da planilha Excel com os dados dos produtos |
| Subprocess | Abertura do executável do ERP |

---

## 📋 Pré-requisitos

- Python 3.8 ou superior
- Sistema operacional Windows
- Fakturama 2 instalado em `C:\Program Files\Fakturama2\Fakturama.exe`
- Imagens dos produtos salvas localmente

---

## 🚀 Instalação

**1. Clone o repositório**
```bash
git clone https://github.com/seu-usuario/automacao-erp.git
cd automacao-erp
```

**2. Instale as dependências**
```bash
pip install pyautogui pyperclip pandas openpyxl
```

---

## 🖥️ Como Usar

**1.** Preencha a planilha `Produtos.xlsx` com os dados dos produtos (veja o formato abaixo)

**2.** Certifique-se de que as imagens dos produtos estão na pasta correta:
```
C:\Users\seu-usuario\Desktop\codigos\ImagensProdutos\
```

**3.** Execute o script:
```bash
python ERP.py
```

**4.** Um alerta vai aparecer avisando que a automação vai começar — confirme e **não mexa no mouse**.

O script irá:
1. Abrir o Fakturama automaticamente
2. Aguardar a tela inicial carregar (reconhecimento de imagem)
3. Para cada produto na planilha: clicar em **New → New Product**, preencher todos os campos, selecionar a imagem e salvar

---

## 📊 Formato da Planilha (`Produtos.xlsx`)

| Coluna | Descrição |
|---|---|
| `Nome` | Nome do produto |
| `ID` | Número do item (Item Number) |
| `Categoria` | Categoria do produto |
| `GTIN` | Código GTIN/EAN |
| `Supplier` | Código do fornecedor |
| `Descrição` | Descrição detalhada |
| `Imagem` | Nome do arquivo de imagem (ex: `produto1.jpg`) |
| `Preço` | Preço de venda (gross) |
| `Custo` | Preço de custo (net) |
| `Estoque` | Quantidade em estoque |

---

## 🧠 Como Funciona o Reconhecimento de Imagem

O PyAutoGUI localiza os elementos na tela comparando screenshots salvos com o que está sendo exibido no monitor. A função `encontrar_imagem()` fica em loop até localizar o elemento, com **90% de confiança** e suporte a **grayscale** para melhor performance:

```python
def encontrar_imagem(imagem):
    while not pyautogui.locateOnScreen(imagem, grayscale=True, confidence=0.9):
        time.sleep(1)
    return pyautogui.locateOnScreen(imagem, grayscale=True, confidence=0.9)
```

Já a função `direita()` calcula a posição logo à direita do elemento encontrado — útil para clicar no campo de input ao lado do label:

```python
def direita(posicoes_imagem):
    return posicoes_imagem[0] + posicoes_imagem[2], posicoes_imagem[1] + posicoes_imagem[3] / 2
```

---

## ⚠️ Observações

- **Não mova o mouse** durante a execução — o PyAutoGUI controla o cursor. Mover o mouse para os cantos da tela aciona o **FAILSAFE** e interrompe o script imediatamente (comportamento intencional de segurança).
- As imagens de referência (`*.png`) devem ser capturadas na **mesma resolução e escala de tela** onde o script vai rodar, caso contrário o reconhecimento pode falhar.
- O texto com vírgula decimal é tratado com `.replace(".", ",")` para compatibilidade com o formato esperado pelo Fakturama.
- O campo de imagem usa `pyperclip` + `Ctrl+V` ao invés de `pyautogui.write()` para evitar problemas com caracteres especiais e barras no caminho do arquivo.


---

## 👤 Autora

Desenvolvido como projeto de automação desktop com Python e PyAutoGUI.

