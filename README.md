# 📘 API Gateway Simples com Microserviços
## 📌 Descrição
Este projeto consiste na implementação de uma arquitetura distribuída baseada em **microserviços**, desenvolvida em **Python com Flask**, com integração através de um **API Gateway**.
O sistema simula uma loja simples (e-commerce), dividindo as responsabilidades em serviços independentes:
* **User Service** → Gestão de utilizadores
* **Product Service** → Gestão de produtos
* **Order Service** → Gestão de pedidos
* **API Gateway** → Ponto central de entrada das requisições

---
## 🧱 Arquitetura do Projeto
O projeto foi desenvolvido seguindo o modelo de **arquitetura distribuída**, onde cada funcionalidade do sistema é isolada em um serviço independente.
### Estrutura:
```
Cliente
   ↓
API Gateway (Porta 5000)
   ↓
 ┌───────────────┬───────────────┬───────────────┐
 ↓               ↓               ↓
User Service   Product Service   Order Service
(5001)         (5002)           (5003)
```

### Estrutura com Escalabilidade (Trabalho 02):
```
Cliente
   ↓
API Gateway (Porta 5000)
   ↓
 ┌───────────────┬─────────────────────────────┬───────────────┐
 ↓               ↓                             ↓               
User Service   Product Service (5002)     Order Service
(5001)         Product Service (5004)     (5003)
               ↑ load balancer round-robin
```

---
## 🛠️ Tecnologias Utilizadas
* Python
* Flask
* Requests
* JSON (armazenamento em memória)

---
## 📂 Estrutura de Pastas
```
project/
│
├── user_service.py
├── product_service.py
├── order_service.py
├── gateway.py
└── teste_carga.py
```

---
## 🚀 Como Executar o Projeto
### 1. Instalar dependências
```bash
pip install flask requests
```

---
### 2. Executar os microserviços
Abrir **4 terminais diferentes** e executar:
#### User Service
```bash
python user_service.py
```
#### Product Service
```bash
python product_service.py
```
#### Order Service
```bash
python order_service.py
```
#### API Gateway
```bash
python gateway.py
```

---
## 🆕 Alterações – Escalabilidade (Trabalho 02)

As seguintes alterações foram feitas para suportar escalabilidade:

**`gateway.py`** — foi adicionado um load balancer em round-robin para o `product_service`. O gateway alterna automaticamente entre as duas instâncias a cada requisição:
```
GET /products → ora responde product-service:5002, ora product-service:5004
```

**`product_service.py`** — a porta passou a ser configurável via argumento no terminal (`sys.argv`) e foi adicionado um identificador de instância (`INSTANCE`). As respostas passaram a incluir o campo `"instance"` no JSON:
```
{
  "instance": "product-service:5002",
  "data": [...]
}
```

`user_service.py` e `order_service.py` **não foram alterados** — o guião pede a replicação de apenas 1 serviço, demonstrando que nos microserviços é possível escalar apenas o serviço necessário.

### Executar com escala

```
# Terminal 1
python user_service.py

# Terminal 2 – instância 1 do product service
python product_service.py 5002

# Terminal 3 – instância 2 do product service (réplica)
python product_service.py 5004

# Terminal 4
python order_service.py

# Terminal 5
python gateway.py
```

---
## 🌐 Portas Utilizadas
| Serviço                  | Porta |
| ------------------------ | ----- |
| API Gateway              | 5000  |
| User Service             | 5001  |
| Product Service          | 5002  |
| Product Service (réplica)| 5004  |
| Order Service            | 5003  |

---
## 📡 Endpoints Disponíveis
### 👤 User Service
#### Listar Utilizadores
```http
GET /users
```
#### Buscar Utilizador por ID
```http
GET /users/{id}
```

---
### 📦 Product Service
#### Listar Produtos
```http
GET /products
```
#### Editar Produto
```http
PUT /products/{id}
```
**Body JSON:**
```json
{
  "price": 35000
}
```

---
### 🛒 Order Service
#### Listar Pedidos
```http
GET /orders
```

---
## 🚪 API Gateway
O API Gateway centraliza todas as requisições do cliente.
### Endpoints:
#### Utilizadores
```http
GET http://localhost:5000/users
```
#### Produtos
```http
GET http://localhost:5000/products
```
#### Pedidos
```http
GET http://localhost:5000/orders
```

---
## 🔄 Funcionamento do Sistema
1. O cliente envia uma requisição para o **Gateway**
2. O Gateway encaminha a requisição para o microserviço correspondente
3. O microserviço processa os dados
4. A resposta retorna ao cliente através do Gateway

No caso do **Order Service**, este também comunica com:
* User Service
* Product Service

para agregar dados relacionados aos pedidos.

---
## 🧪 Testes
A API pode ser testada utilizando:
* Postman
* Browser (requisições GET)

### Teste de carga

```
python teste_carga.py
```

O script simula 50 utilizadores em simultâneo e apresenta no final:
* Total de requisições
* Requisições com sucesso / erro
* Tempo médio de resposta
* Duração total do teste

---
## 📊 Vantagens da Arquitetura de Microserviços
* Separação de responsabilidades
* Escalabilidade independente de serviços
* Facilidade de manutenção
* Melhor organização estrutural

---
## ❌ Desvantagens
* Maior complexidade de implementação
* Necessidade de comunicação entre serviços
* Dependência de disponibilidade entre microserviços

---
## 👨‍💻 Autor
Projeto desenvolvido para fins académicos.
