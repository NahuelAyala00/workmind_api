# WorkMind – Plataforma Inteligente de Aprendizagem e Bem-Estar no Futuro do Trabalho

## 📌 Sobre o Projeto
O **WorkMind** é uma plataforma desenvolvida como parte da **Global Solution – Engenharia de Software (FIAP, 2025/2)**.  
Seu objetivo é integrar **IA, IoT, APIs e interfaces mobile** para apoiar:

- Aprendizagem contínua e personalizada  
- Monitoramento de bem-estar e ambiente  
- Inclusão produtiva  
- Preparação para carreiras emergentes do futuro  

O projeto é dividido em módulos independentes: banco de dados, API, testes, segurança, mobile e IoT.

---

## 🧠 Principais Funcionalidades
### 🔹 IA de Aprendizagem Adaptativa (conceitual)
- Recomenda cursos
- Gera trilhas personalizadas
- Calcula progresso

### 🔹 API REST (FastAPI)
- Login com bcrypt  
- Cadastro de usuário  
- Listagem de cursos  
- Trilha do usuário  
- Dados de sensores IoT  

### 🔹 IoT Simulado
- Script Python que gera leituras de:
  - Temperatura  
  - Ruído  
  - Luminosidade  
- Dados armazenados no PostgreSQL e exibidos pela API

### 🔹 Mobile (Mock HTML/CSS)
- Dashboard  
- Minha Trilha  
- Monitoramento IoT  

---

## 🗂 Estrutura do Projeto
```
workmind_api/
│
├── app/
│   ├── routers/
│   │   ├── auth.py
│   │   ├── users.py
│   │   ├── courses.py
│   │   ├── sensors.py
│   │   └── trails.py
│   ├── models.py
│   ├── schemas.py
│   └── database.py
│
├── tests/
│   ├── test_auth.py
│   ├── test_users.py
│   ├── test_courses.py
│   ├── test_sensors.py
│   └── test_trails.py
│
├── iot_simulator.py
├── requirements.txt
└── README.md
```

---

## ⚙️ Como executar a API

### 1. Instalar dependências
```bash
pip install -r requirements.txt
```

### 2. Rodar o servidor
```bash
uvicorn app.main:app --reload
```

### 3. Acessar documentação
```
http://127.0.0.1:8000/docs
```

---

## 🔧 Simulação IoT
Para gerar leituras artificiais no banco:

```bash
python iot_simulator.py
```

As leituras aparecerão em:

```
GET /sensores
```

---

## 🛡 Segurança
- Armazenamento de senha com **bcrypt**
- Validação de entrada com Pydantic
- ORM SQLAlchemy (evita SQL Injection)
- Mensagens genéricas de erro

---

## 🧪 Testes Automatizados
Executar:

```bash
pytest
```

O projeto inclui testes para:
- Login  
- Cadastro e listagem  
- Cursos  
- Trilhas  
- Sensores IoT  

---

## 👨‍💻 Integrante
- **Nahuel Isaias Ayala Molinas – RM 567887**

---

## 📄 Licença
Projeto acadêmico — FIAP 2025.  
Uso apenas para fins educacionais.
