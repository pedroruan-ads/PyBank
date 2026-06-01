# 🏦 PyBank — Sistema Bancário Digital

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.8%2B-3776AB?style=for-the-badge&logo=python&logoColor=white"/>
  <img src="https://img.shields.io/badge/HTML5-Interface-E34F26?style=for-the-badge&logo=html5&logoColor=white"/>
  <img src="https://img.shields.io/badge/Status-Concluído-4A8A24?style=for-the-badge"/>
  <img src="https://img.shields.io/badge/Licença-MIT-yellow?style=for-the-badge"/>
</p>

<p align="center">
  Sistema bancário simulado com interface web moderna, desenvolvido em Python + HTML/CSS/JS puro.
</p>

---

## ✨ Funcionalidades

| Recurso | Descrição |
|---|---|
| 💰 **Depósito** | Deposite qualquer valor e acompanhe o saldo em tempo real |
| 💸 **Saque** | Saque valores pré-definidos com validação de saldo |
| 📈 **Investimentos** | Compre cotas de empresas da bolsa simulada |
| ⚡ **Pix** | Envie transferências instantâneas via chave Pix |
| 📋 **Extrato** | Histórico completo com filtros por tipo de operação |
| 🎯 **Meta de economia** | Acompanhe seu progresso para a reserva de emergência |

---

## 🖥️ Demonstração

```
═══════════════════════════════════════
        BEM-VINDO AO PYBANK
═══════════════════════════════════════

  Digite seu nome: João Silva
  Senha (data de nascimento, ex: 070307): 150398

  ✅ Acesso autorizado!
  Olá, João Silva! Seu saldo inicial é R$ 3.412,00

────────────────────────────────────────
  🏦 PYBANK — MENU PRINCIPAL
────────────────────────────────────────
  Saldo: R$ 3.412,00

  [1] Sacar
  [2] Depositar
  [3] Investir
  [4] Extrato
  [5] Sair
```

---

## 🚀 Como executar

### 🐍 Versão Python (terminal)

**Pré-requisitos:** Python 3.8+

```bash
# Clone o repositório
git clone https://github.com/[seu-usuario]/pybank.git
cd pybank

# Execute o sistema
python pybank.py
```

### 🌐 Versão Web (interface visual)

Abra o arquivo `index.html` diretamente no navegador:

```bash
# No terminal (Linux/Mac)
open index.html

# Ou simplesmente arraste o arquivo para o browser
```

> **Nenhuma dependência externa necessária!** A interface web roda 100% no navegador, sem instalar nada.

---

## 📁 Estrutura do projeto

```
pybank/
│
├── pybank.py          # Sistema bancário em Python (terminal)
├── index.html         # Interface web completa (HTML/CSS/JS)
└── README.md          # Documentação do projeto
```

---

## 🛠️ Tecnologias

**Backend (Python):**
- Módulo `time` — simulação de tempo de processamento
- Módulo `random` — geração de saldo inicial aleatório
- Funções modulares com escopo bem definido
- Histórico de operações por sessão

**Frontend (Web):**
- HTML5 semântico
- CSS3 com variáveis customizadas (`CSS Custom Properties`)
- JavaScript Vanilla (ES6+)
- Google Fonts (Sora + DM Serif Display)
- Design responsivo e acessível

---

## 📐 Conceitos aplicados

- ✅ Funções e modularização de código
- ✅ Variáveis globais com `global`
- ✅ Tratamento de exceções com `try/except`
- ✅ Estruturas condicionais e laços de repetição
- ✅ Dicionários e listas em Python
- ✅ Formatação de strings com f-strings
- ✅ Separação de responsabilidades (cada função tem um único objetivo)
- ✅ Interface web com estado gerenciado em JS puro

---

## 🤝 Contribuindo

Contribuições são bem-vindas! Sinta-se à vontade para:

1. Fazer um `fork` do projeto
2. Criar uma branch: `git checkout -b feature/minha-feature`
3. Commitar: `git commit -m 'feat: adiciona minha feature'`
4. Push: `git push origin feature/minha-feature`
5. Abrir um Pull Request

---

## 📌 Próximas melhorias

- [ ] Autenticação com banco de dados (SQLite)
- [ ] Transferências entre contas
- [ ] Gráfico de evolução do saldo
- [ ] Exportar extrato em PDF
- [ ] Testes unitários com `pytest`

---

## 👤 Autor

**Pedro Ruan**


---

## 📄 Licença

Este projeto está sob a licença MIT. Veja o arquivo [LICENSE](LICENSE) para mais detalhes.

---

<p align="center">Feito com ☕ e Python</p>
