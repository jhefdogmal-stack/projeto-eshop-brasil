# 🚀 E-Shop Brasil - Gestão de Big Data com MongoDB

Este projeto foi desenvolvido como parte da avaliação da disciplina de Gestão de Big Data. A aplicação simula um sistema de gestão de preferências de clientes para a empresa E-Shop Brasil, utilizando tecnologias modernas de banco de dados e virtualização.

## 📚 1. Parte Teórica: Fundamentação Técnica

### Evolução dos Bancos de Dados: SQL vs NoSQL
Enquanto bancos relacionais (SQL) são excelentes para dados estruturados e transações rígidas, o cenário de Big Data da E-Shop Brasil exige flexibilidade. Optamos pelo **MongoDB (NoSQL)** por permitir o armazenamento de grandes volumes de dados não estruturados, facilitando a análise de comportamento do consumidor em tempo real.

### Big Data e Personalização
Utilizamos princípios de Big Data para capturar e processar preferências de usuários. Através do MongoDB, conseguimos escalar a infraestrutura horizontalmente e realizar consultas rápidas que permitem personalizar a experiência do usuário e otimizar a logística de estoque.

### Segurança e LGPD
A aplicação foi desenvolvida respeitando os princípios da LGPD, garantindo que apenas dados necessários sejam coletados. O uso de containers Docker assegura que o ambiente do banco de dados esteja isolado e protegido.

## 🛠️ 2. Parte Prática: Tecnologias Utilizadas

* **Docker & Docker Compose:** Virtualização do ambiente.
* **MongoDB:** Banco de dados NoSQL orientado a documentos.
* **Python & Streamlit:** Backend e interface gráfica.

## 🚀 Como Executar o Projeto

1.  **Subir o banco de dados:**
    ```bash
    docker-compose up -d
    ```
2.  **Executar a aplicação:**
    ```bash
    python -m streamlit run app.py
    ```

## 📊 Funcionalidades e Testes
- [x] Inserção de dados em tempo real no MongoDB.
- [x] Consulta e exibição de dados em interface gráfica.
- [x] Persistência de dados através de volumes Docker.

> **Evidência:** O sistema foi testado com sucesso, conforme registrado nos arquivos de imagem deste repositório.
