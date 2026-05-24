# Steam Data Pipeline API

Pipeline ETL modular e API REST desenvolvidos com Python, FastAPI, Pandas e SQLite.

O projeto consome dados públicos da Steam, realiza extração, transformação e persistência dos dados, além de disponibilizar os dados através de uma API REST organizada e tipada.

O foco do projeto é:
- aprendizado prático;
- engenharia de dados;
- backend moderno;
- arquitetura limpa;
- construção de portfólio profissional.

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
SQLite
   ↓
Repository Layer
   ↓
FastAPI
   ↓
Pydantic Schemas
```

---

# Stack Utilizada

- Python 3.13
- FastAPI
- Pandas
- SQLAlchemy
- SQLite
- Pydantic
- Pytest
- Uvicorn
- python-dotenv

---

# Funcionalidades Implementadas

## Pipeline ETL

- Consumo da API pública da Steam
- Extração de dados via HTTP
- Transformação e normalização dos dados
- Conversão JSON → DataFrame
- Persistência em SQLite
- Recriação automática da tabela `games`

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
- paginação;
- busca textual;
- filtros por preço;
- filtros por plataforma;
- estatísticas gerais;
- suporte a controle.

---

# Qualidade e Arquitetura

O projeto atualmente implementa:

- Repository Pattern
- Logging estruturado
- Queries SQL parametrizadas
- Configuração centralizada via `.env`
- Separação de responsabilidades
- Pydantic Schemas
- Testes automatizados
- Serializer customizado
- Estrutura modular
- Versionamento por feature branches

---

# Logging Estruturado

A aplicação possui logs organizados por camada:

- extract
- transform
- load
- repository
- routes
- pipeline
- main

Tipos de log utilizados:
- `INFO`
- `WARNING`
- `ERROR`

Objetivo:
- observabilidade;
- rastreabilidade;
- debugging;
- monitoramento futuro.

---

# Testes Automatizados

O projeto possui testes utilizando `pytest`.

Cobertura inicial:
- transformação de dados;
- serialização;
- rotas FastAPI;
- validação de status code;
- validação de payload;
- validação de erros HTTP.

Executar testes:

```bash
pytest
```

---

# Configuração da Aplicação

Variáveis de ambiente:

```env
DATABASE_URL=sqlite:///data/games.db
STEAM_API_URL=https://store.steampowered.com/api/featuredcategories/
REQUEST_TIMEOUT=10
```

---

# Como Executar o Projeto

## Clonar repositório

```bash
git clone https://github.com/SEU_USUARIO/steam-data-pipeline.git
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

# Executando o Pipeline ETL

```bash
python run.py
```

O pipeline irá:
- extrair os dados da Steam;
- transformar e normalizar os dados;
- persistir os dados no SQLite.

---

# Executando a API

```bash
uvicorn app.main:app --reload
```

---

# Documentação da API

Swagger:

```text
http://127.0.0.1:8000/docs
```

---

# Fluxo de Versionamento

O projeto utiliza workflow baseado em:
- feature branches;
- commits segmentados;
- pull requests;
- merge incremental na `main`.

Branches já utilizadas:

```text
main
feature/api-filters
feat/pydantic-schemas
feat/logging
feat/tests
docs/project-readme
chrore/config-and-quality
```

---

# Próximas Melhorias

## Infraestrutura
- Docker
- Docker Compose
- PostgreSQL
- Deploy em nuvem

---

## Engenharia de Software
- CI/CD com GitHub Actions
- Cobertura avançada de testes
- Fixtures e mocks
- Alembic migrations

---

## Backend e Dados
- Camada Service
- Cache com Redis
- Async requests
- Métricas e observabilidade avançada

---

# Possíveis Próximas Branches

```text
feat/docker
feat/postgresql
feat/github-actions
feat/service-layer
feat/cache-redis
feat/async-extract
test/integration-tests
refactor/database-layer
```

---

# Objetivo Técnico do Projeto

O projeto busca consolidar conhecimentos em:
- backend com Python;
- engenharia de dados;
- APIs REST;
- arquitetura modular;
- testes automatizados;
- observabilidade;
- boas práticas de engenharia de software.

---

# Autor

Kevin Souza

Graduado em Ciência da Computação com foco em:
- Backend
- Engenharia de Dados
- Machine Learning
- Inteligência Artificial
