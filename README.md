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

```id="q85xk2"
Cliente
   ↓
API Gateway (Porta 5000)
   ↓
 ┌───────────────┬───────────────┬───────────────┐
 ↓               ↓               ↓
User Service   Product Service   Order Service
(5001)         (5002)           (5003)
```

---

## 🛠️ Tecnologias Utilizadas

* Python
* Flask
* Requests
* JSON (armazenamento em memória)

---

## 📂 Estrutura de Pastas

```id="8vts5e"
project/
│
├── user_service.py
├── product_service.py
├── order_service.py
└── gateway.py
```

---

## 🚀 Como Executar o Projeto

### 1. Instalar dependências

```bash id="t9b30y"
pip install flask requests
```

---

### 2. Executar os microserviços

Abrir **4 terminais diferentes** e executar:

#### User Service

```bash id="w0l1ea"
python user_service.py
```

#### Product Service

```bash id="6e53r9"
python product_service.py
```

#### Order Service

```bash id="zb6m4h"
python order_service.py
```

#### API Gateway

```bash id="b2x9mq"
python gateway.py
```

---

## 🌐 Portas Utilizadas

| Serviço         | Porta |
| --------------- | ----- |
| API Gateway     | 5000  |
| User Service    | 5001  |
| Product Service | 5002  |
| Order Service   | 5003  |

---

## 📡 Endpoints Disponíveis

### 👤 User Service

#### Listar Utilizadores

```http id="6v0bbx"
GET /users
```

#### Buscar Utilizador por ID

```http id="6j3xya"
GET /users/{id}
```

---

### 📦 Product Service

#### Listar Produtos

```http id="4mbd93"
GET /products
```

#### Editar Produto

```http id="jlwmq9"
PUT /products/{id}
```

**Body JSON:**

```json id="lvtpsh"
{
  "price": 35000
}
```

---

### 🛒 Order Service

#### Listar Pedidos

```http id="0ayvgg"
GET /orders
```

---

## 🚪 API Gateway

O API Gateway centraliza todas as requisições do cliente.

### Endpoints:

#### Utilizadores

```http id="xrz5wu"
GET http://localhost:5000/users
```

#### Produtos

```http id="rtr8pr"
GET http://localhost:5000/products
```

#### Pedidos

```http id="jlwmx6"
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
