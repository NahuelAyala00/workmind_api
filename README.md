# WorkMind – Plataforma Inteligente de Aprendizagem e Bem-Estar no Futuro do Trabalho

## 📌 Sobre o Projeto
O **WorkMind** é uma plataforma desenvolvida para a Global Solution – Engenharia de Software (FIAP, 2025/2).  
Ela integra **IA, IoT, APIs e mobile** para apoiar aprendizagem personalizada, bem‑estar e preparação para carreiras do futuro.

---

## 🧠 Funcionalidades
- IA de trilhas adaptativas (conceitual)
- API REST com FastAPI
- Login seguro com bcrypt
- Cadastro e listagem de usuários
- Cursos e trilhas
- Sensores IoT simulados
- Telas mobile (mock HTML/CSS)

---

## 🗂 Estrutura do Projeto
```
workmind_api/
│
├── app/
│   ├── __init__.py
│   ├── main.py
│   ├── database.py
│   ├── models.py
│   ├── schemas.py
│   └── routers/
│       ├── __init__.py
│       ├── auth.py
│       ├── users.py
│       ├── courses.py
│       ├── sensors.py
│       └── trails.py
│
├── tests/
│   ├── __init__.py
│   ├── test_auth.py
│   ├── test_users.py
│   ├── test_courses.py
│   ├── test_sensors.py
│   └── test_trails.py
│
├── telas/
│   ├── index.html
│   └── WorkMind_Telas.pdf
│
├── docs/
│   ├── WorkMind - Final.pdf
│   └── Integrantes do grupo.txt
│
├── iot_simulator.py
├── requirements.txt
└── README.md
```

---

## ⚙️ Executando a API
```bash
pip install -r requirements.txt
uvicorn app.main:app --reload
```

Documentação:
```
http://127.0.0.1:8000/
```

---

## 🔧 Simulação IoT
```bash
python iot_simulator.py
```
As leituras ficam disponíveis em:
```
GET /sensores
```

---

## 🧪 Testes
```bash
pytest
```

---

## 👨‍💻 Integrante
- Nahuel Isaias Ayala Molinas – RM 567887

---

## 📄 Licença
Projeto acadêmico da FIAP – 2025.
