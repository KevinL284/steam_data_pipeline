# Steam Data Pipeline API

Pipeline ETL modular e API REST desenvolvidos com Python, FastAPI, Pandas e SQLite.

O projeto consome dados públicos da Steam, realiza extração, transformação e persistência dos dados, além de disponibilizar os dados através de uma API REST.

---

# Arquitetura do Projeto

```text
Steam API
   ↓
Camada de Extract
   ↓
Camada de Transform
   ↓
SQLite
   ↓
FastAPI REST API
```

---

# Stack Utilizada

- Python 3.13
- FastAPI
- Pandas
- SQLAlchemy
- SQLite
- Uvicorn

---

# Funcionalidades

- Consumo da API pública da Steam
- Pipeline ETL modular
- Persistência em SQLite
- API REST com FastAPI
- Paginação
- Busca textual
- Filtros por preço e plataforma
- Estatísticas gerais
- Repository Pattern
- Queries parametrizadas
- Camada de serialização

---

# Estrutura do Projeto

```text
steam-data-pipeline/
│
├── app/
│   │
│   ├── api/
│   │   └── routes.py
│   │
│   ├── core/
│   │   ├── config.py
│   │   └── pipeline.py
│   │
│   ├── extract/
│   │   └── steam_api.py
│   │
│   ├── transform/
│   │   └── clean_data.py
│   │
│   ├── load/
│   │   └── database.py
│   │
│   ├── repositories/
│   │   └── games_repository.py
│   │
│   ├── utils/
│   │   └── serializer.py
│   │
│   └── main.py
│
├── data/
├── requirements.txt
├── run.py
└── README.md
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
- Extrair os dados da Steam
- Transformar e normalizar os dados
- Persistir os dados no SQLite

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

# Endpoints Disponíveis

## Listar jogos

```http
GET /games
```

---

## Jogos abaixo de determinado preço

```http
GET /games/under/{price}
```

---

## Jogos com maiores descontos

```http
GET /games/top-discounts
```

---

## Buscar jogos por nome

```http
GET /games/search/{name}
```

---

## Jogos por plataforma

```http
GET /games/platform/{platform}
```

Plataformas disponíveis:
- windows
- mac
- linux

---

## Jogos com suporte a controle

```http
GET /games/controller-support
```

---

## Estatísticas gerais

```http
GET /stats
```

---

# Próximas Melhorias

- Docker
- PostgreSQL
- Cache com Redis
- Testes automatizados
- CI/CD
- Logging estruturado
- Pydantic models
- Deploy em nuvem

---

# Autor

Kevin Souza

Graduado em Ciência da Computação com foco em:
- Backend
- Engenharia de Dados
- Machine Learning
- Inteligência Artificial
