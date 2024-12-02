
# 💸 Previsor de Preços de Ações - API

Esse projeto tem como objetivo disponibilizar um serviço HTTP que realiza
inferências em um modelo de **LSTM** treinado para prever o próximo preço de
fechamento de uma ação da B3 específica com base em dados históricos.

![Tela inicial do APP](https://einvestidor.estadao.com.br/wp-content/uploads/2024/10/adobestock-549836029-1_171020240323.jpeg.webp)

## 🔧 Rodando localmente

Clone o projeto

```bash
  git clone https://github.com/brenobarrosm/api-stock-price-forecaster
```

Entre no diretório do projeto

```bash
  cd api-stock-price-forecaster
```

Instale as dependências

```bash
  pip install -r requirements.txt
```

Inicie o servidor

```bash
  uvicorn main:app --host 0.0.0.0 --port 8000
```


## 🌐 Deploy via Docker

Para fazer o deploy desse projeto usando o Docker, siga os passos abaixo:

**1.** Faça o build da aplicação (com o repositório já clonado e dentro
da pasta do projeto)
```bash
  sudo docker build -t api-stock-price-forecaster .
```

**2.** Execute a imagem criada
```bash
  docker run --env-file .env -p 8000:8000 api-stock-price-forecaster
```


