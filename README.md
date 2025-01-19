# Microsserviço Serverless para Validação de CPF

Este é um microsserviço desenvolvido em Python utilizando o **Azure Functions** para realizar a validação de CPF. Ele utiliza uma arquitetura **serverless**, garantindo escalabilidade e eficiência no processamento de requisições.

---

## **Fluxo Geral do Microsserviço**

A imagem abaixo apresenta uma visão geral da arquitetura e funcionamento do microsserviço:

![Visão Geral](print/imagem-geral.png)

---

## **Exemplo de Uso**

O microsserviço valida se um CPF é válido ou inválido, retornando as respostas adequadas. Veja os exemplos abaixo:

### CPF Válido
![CPF Válido](print/cpf-valido.png)

### CPF Inválido
![CPF Inválido](print/cpf-invalido.png)

---

## **Criando a Função no Azure**

Para criar a função no Azure, utilizamos o Azure Portal. A imagem a seguir mostra o painel com a função configurada:

![Função no Azure](print/function-azure.png)

---

## **Endpoints Disponíveis**

### URL Base
A URL base do microsserviço será gerada automaticamente após a publicação no Azure Functions. Exemplo:
