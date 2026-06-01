# Steam Data Pipeline API

Pipeline ETL modular e API REST desenvolvidos com Python, FastAPI, Pandas e PostgreSQL.

O projeto consome dados públicos da Steam, realiza extração, transformação e persistência dos dados, além de disponibilizar os dados através de uma API REST organizada, tipada e containerizada.

Mais do que apenas consumir uma API pública, o objetivo do projeto é funcionar como um laboratório prático de engenharia de software e engenharia de dados, simulando workflows, arquitetura e práticas utilizadas em ambientes profissionais reais.

O foco do projeto é:

* aprendizado prático;
* engenharia de dados;
* backend moderno;
* arquitetura limpa;
* automação;
* qualidade de software;
* construção de portfólio profissional.

---

# Arquitetura do Projeto

```text
Steam API
   ↓
Extract Layer
   ↓
Transform Layer
   ↓
Load Layer
   ↓
PostgreSQL
   ↓
Repository Layer
   ↓
FastAPI
   ↓
Pydantic Schemas
```

---

# Stack Utilizada

## Backend

* Python 3.13
* FastAPI
* SQLAlchemy
* Pydantic

## Dados

* PostgreSQL
* Pandas
* ETL / ELT

## Qualidade e DevOps

* Docker
* Docker Compose
* Pytest
* GitHub Actions
* CI/CD
* Black
* Flake8
* Isort
* pytest-cov

## Infraestrutura

* psycopg2-binary
* Uvicorn
* python-dotenv

---

# Funcionalidades Implementadas

## Pipeline ETL

* Consumo da API pública da Steam
* Extração de dados via HTTP
* Transformação e normalização de dados
* Conversão JSON → DataFrame
* Persistência em PostgreSQL
* Recriação automática da tabela `games`

---

## API REST

Endpoints disponíveis:

```http
GET /games
GET /games/under/{price}
GET /games/top-discounts
GET /games/search/{name}
GET /games/platform/{platform}
GET /games/controller-support
GET /stats
```

Funcionalidades:

* paginação;
* busca textual;
* filtros por preço;
* filtros por plataforma;
* estatísticas gerais;
* suporte a controle.

---

# Qualidade e Arquitetura

O projeto atualmente implementa:

* Repository Pattern
* Logging estruturado
* Queries SQL parametrizadas
* Configuração centralizada via `.env`
* Separação de responsabilidades
* Pydantic Schemas
* Estrutura modular
* Docker Compose
* Containerização da aplicação
* PostgreSQL via Docker
* Versionamento por feature branches
* Integração contínua com GitHub Actions

---

# Logging Estruturado

A aplicação possui logs organizados por camada:

* extract
* transform
* load
* repository
* routes
* pipeline
* main

Tipos de log utilizados:

* `INFO`
* `WARNING`
* `ERROR`

Objetivos:

* observabilidade;
* rastreabilidade;
* debugging;
* preparação para monitoramento futuro.

---

# Testes Automatizados

O projeto possui testes utilizando `pytest`.

Cobertura atual:

* transformação de dados;
* serialização;
* rotas FastAPI;
* validação de status code;
* validação de payload;
* validação de erros HTTP.

Executar testes:

```bash
pytest
```

Executar cobertura:

```bash
pytest --cov=app --cov-report=term-missing
```

---

# CI/CD e Qualidade de Código

O projeto utiliza GitHub Actions para execução automatizada de:

* testes automatizados;
* validação de imports;
* linting;
* formatação;
* coverage.

Ferramentas utilizadas:

* `flake8`
* `black`
* `isort`
* `pytest-cov`

O workflow é executado automaticamente em:

* push na `main`;
* pull requests.

---

# Configuração da Aplicação

Variáveis de ambiente:

```env
DATABASE_URL=postgresql+psycopg2://steam_user:steam_password@db:5432/steam_data
STEAM_API_URL=https://store.steampowered.com/api/featuredcategories/
REQUEST_TIMEOUT=10
```

---

# Como Executar o Projeto

## Clonar repositório

```bash
git clone https://github.com/KevinL284/steam_data_pipeline.git
```

---

## Criar ambiente virtual

```bash
python -m venv venv
```

---

## Ativar ambiente virtual

### Windows

```bash
.\venv\Scripts\Activate.ps1
```

### Linux / MacOS

```bash
source venv/bin/activate
```

---

## Instalar dependências

```bash
pip install -r requirements.txt
```

---

# Executando com Docker

## Subir containers

```bash
docker compose up --build
```

---

## Executar pipeline ETL

```bash
docker compose exec api python run.py
```

O pipeline irá:

* extrair os dados da Steam;
* transformar e normalizar os dados;
* persistir os dados no PostgreSQL.

---

# Executando a API

Swagger disponível em:

```text
http://localhost:8000/docs
```

---

# Fluxo de Desenvolvimento

O projeto utiliza workflow baseado em:

* feature branches;
* commits segmentados;
* pull requests;
* merge incremental na `main`;
* roadmap técnico com GitHub Projects;
* organização de issues por tarefas e melhorias.

---

# Próximas Melhorias

## Engenharia de Software

* Cobertura avançada de testes
* Fixtures e mocks
* Service Layer
* Alembic migrations
* Refatoração da camada de configuração

---

## Infraestrutura

* Deploy em nuvem
* Reverse proxy com Nginx
* Healthchecks Docker
* Persistência externa

---

## Backend e Dados

* Cache com Redis
* Async requests
* Observabilidade avançada
* Métricas e monitoramento
* Expansão do pipeline de dados

---

# Objetivo Técnico do Projeto

O projeto busca consolidar conhecimentos em:

* backend com Python;
* engenharia de dados;
* APIs REST;
* arquitetura modular;
* testes automatizados;
* CI/CD;
* observabilidade;
* Docker;
* workflows modernos de engenharia de software.

Além da parte técnica, o projeto também funciona como:

* portfólio profissional;
* laboratório de experimentação;
* ambiente de prática de engenharia real;
* documentação da evolução técnica do desenvolvimento.

---

# Autor

Kevin Souza

Bacharel em Ciência da Computação com foco em:

* Backend
* Engenharia de Dados
* Machine Learning
* Inteligência Artificial
