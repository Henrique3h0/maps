# Automatizador de Captação de Clientes 🗺️

Este é um projeto composto por dois scripts em Python para extrair informações de estabelecimentos comerciais no Google Maps e criar arquivos HTML com esses dados.

## Características 🚀

### Script 1: scraper.py 📜

O script `scraper.py` contém uma classe `GoogleMapsScraper` que realiza as seguintes tarefas:

- Inicializa um navegador Chrome sem cabeçalho usando o Selenium.
- Realiza uma busca no Google Maps com um termo fornecido pelo usuário.
- **Informações Obtidas:**
    - `👥 Nome da empresa`
    - `📞 Contato da empresa`
    - `🌐 Se possui um site, ou utiliza Instagram ou Facebook em vez de site`
    - `🗺️ URL da página do Google Maps dessa empresa`
- Cria threads para lidar com múltiplos resultados de forma eficiente.
- Fecha o navegador após a conclusão da extração.

### Script 2: maps.py 🔄

O script `maps.py` interage com o capturador do Google Maps e realiza as seguintes tarefas:

- Solicita ao usuário que insira uma localização e tipo de estabelecimento.
- Utiliza o capturador para buscar e extrair informações dos estabelecimentos.
- Cria arquivos HTML com os dados obtidos.
- Abre os arquivos HTML no navegador para visualização.
- Exibe mensagens ao usuário informando sobre os resultados da busca.

## Pré-requisitos 🛠️

- Python 3.x instalado no sistema.
- As bibliotecas necessárias podem ser instaladas usando o arquivo `requirements.txt`.

## Como Usar 📋

1. Clone o repositório para o seu ambiente local:

```bash
git clone https://github.com/Henrique3h0/maps
```

2. Navegue até o diretório do projeto:

```bash
cd maps
```

3. Instale as dependências:

```bash
pip install -r requirements.txt
```

4. Execute o script `maps.py`:

```bash
python maps.py
```

5. Siga as instruções apresentadas no terminal para realizar a busca.

## Notas Adicionais ℹ️

- Certifique-se de ter uma conexão de internet ativa para que o capturador acesse o Google Maps.
- Os arquivos HTML gerados serão salvos no diretório `captações/{data_atual}` dentro do diretório do projeto.

## Perfeito para Aquisição de Clientes no Google Maps 🎯

Esta ferramenta é ideal para profissionais que realizam aquisição de clientes usando o Google Maps, facilitando a extração e organização de informações de estabelecimentos comerciais.

## Atualizações Futuras ⏳

- [✅] Threading
- [✅] Windows Fast Start
- [❌] Get Images
- [❌] Auto Whatsapp Send (com IA)
- [❌] Auto SMS Send (com IA)
- [❌] IA Copy (para criar uma copy para entrar em contato com cada empresa)

## Contribuições 🤝

Contribuições são bem-vindas! Sinta-se à vontade para abrir uma issue se encontrar algum problema ou propor melhorias.

## Autoria ✍️

Desenvolvido por [LIMA](https://github.com/Henrique3h0).
