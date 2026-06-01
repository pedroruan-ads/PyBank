import time
import random

# ==========================================
#   PyBank - Sistema Bancário em Python
#   Autor: [Seu Nome]
#   GitHub: github.com/[seu-usuario]/pybank
# ==========================================

saldo_banco = float(random.randint(-1000, 9000))
historico = []

def separador():
    print("─" * 40)

def cabecalho(titulo):
    print(f"\n{'─' * 40}")
    print(f"  {titulo}")
    print(f"{'─' * 40}")

def exibir_saldo():
    status = "🟢 POSITIVO" if saldo_banco >= 0 else "🔴 NEGATIVO"
    print(f"\n  Saldo atual: R$ {saldo_banco:.2f}  |  {status}")

def registrar_operacao(tipo, valor):
    """Registra cada operação no histórico da sessão."""
    historico.append({
        "tipo": tipo,
        "valor": valor,
        "saldo_apos": saldo_banco
    })

# ─────────────────────────────────────────
#  SAQUE
# ─────────────────────────────────────────
def sacar_dinheiro():
    global saldo_banco

    cabecalho("💸 SAQUE")
    exibir_saldo()

    if saldo_banco < 10:
        print("\n  ❌ Saldo insuficiente para realizar um saque.")
        return

    opcoes = {1: 10, 2: 50, 3: 100, 4: 500, 5: 1000}

    print("\n  Valores disponíveis:")
    for chave, valor in opcoes.items():
        print(f"  [{chave}] R$ {valor:.2f}")

    separador()

    try:
        escolha = int(input("  Escolha uma opção: "))
    except ValueError:
        print("\n  ❌ Entrada inválida! Digite apenas números.")
        return

    if escolha not in opcoes:
        print("\n  ❌ Opção inválida!")
        return

    valor_saque = opcoes[escolha]
    print(f"\n  ⏳ Processando saque de R$ {valor_saque:.2f}...")

    if saldo_banco < valor_saque:
        print("  ❌ Saldo insuficiente para este valor!")
        return

    time.sleep(0.8)
    saldo_banco -= valor_saque
    registrar_operacao("Saque", valor_saque)

    print(f"  ✅ Saque de R$ {valor_saque:.2f} realizado com sucesso!")
    exibir_saldo()


# ─────────────────────────────────────────
#  DEPÓSITO
# ─────────────────────────────────────────
def depositar_dinheiro():
    global saldo_banco

    cabecalho("💰 DEPÓSITO")
    exibir_saldo()

    try:
        valor_deposito = float(input("\n  Valor a depositar: R$ "))
    except ValueError:
        print("\n  ❌ Valor inválido!")
        return

    if valor_deposito <= 0:
        print("\n  ❌ O valor deve ser maior que zero.")
        return

    print(f"\n  ⏳ Processando depósito de R$ {valor_deposito:.2f}...")
    time.sleep(0.8)

    saldo_banco += valor_deposito
    registrar_operacao("Depósito", valor_deposito)

    print(f"  ✅ Depósito realizado com sucesso!")
    exibir_saldo()


# ─────────────────────────────────────────
#  INVESTIMENTO
# ─────────────────────────────────────────
def investir_dinheiro():
    global saldo_banco

    cabecalho("📈 INVESTIMENTOS")
    exibir_saldo()

    empresas = {
        1: {"nome": "Banco do Brasil", "ticker": "BBAS3", "preco": 32.56},
        2: {"nome": "Petrobras",       "ticker": "PETR4", "preco": 28.90},
        3: {"nome": "Vale",            "ticker": "VALE3", "preco": 55.30},
        4: {"nome": "Itaú",            "ticker": "ITUB4", "preco": 34.75},
        5: {"nome": "Ambev",           "ticker": "ABEV3", "preco": 12.40},
    }

    print("\n  Empresas disponíveis:")
    print(f"  {'#':<4} {'Empresa':<20} {'Ticker':<8} {'Preço/cota':>10}")
    separador()
    for chave, emp in empresas.items():
        print(f"  [{chave}] {emp['nome']:<20} {emp['ticker']:<8} R$ {emp['preco']:>7.2f}")
    separador()

    try:
        escolha = int(input("  Escolha a empresa: "))
    except ValueError:
        print("\n  ❌ Entrada inválida!")
        return

    if escolha not in empresas:
        print("\n  ❌ Empresa inválida!")
        return

    empresa = empresas[escolha]

    try:
        quantidade = int(input(f"  Quantas cotas de {empresa['nome']} deseja comprar? "))
    except ValueError:
        print("\n  ❌ Quantidade inválida!")
        return

    if quantidade <= 0:
        print("\n  ❌ A quantidade deve ser maior que zero.")
        return

    valor_total = quantidade * empresa['preco']
    print(f"\n  Resumo da operação:")
    print(f"  • Empresa  : {empresa['nome']} ({empresa['ticker']})")
    print(f"  • Cotas    : {quantidade}")
    print(f"  • Preço    : R$ {empresa['preco']:.2f}")
    print(f"  • Total    : R$ {valor_total:.2f}")
    separador()

    if saldo_banco < valor_total:
        print("  ❌ Saldo insuficiente para este investimento!")
        return

    confirmar = input("  Confirmar operação? (S/N): ").strip().lower()
    if confirmar not in ['s', 'sim']:
        print("  ⚠️  Operação cancelada.")
        return

    print("\n  ⏳ Processando investimento...")
    time.sleep(1)

    saldo_banco -= valor_total
    registrar_operacao(f"Investimento em {empresa['ticker']}", valor_total)

    print(f"  ✅ {quantidade} cota(s) de {empresa['nome']} comprada(s) com sucesso!")
    exibir_saldo()


# ─────────────────────────────────────────
#  EXTRATO
# ─────────────────────────────────────────
def exibir_extrato():
    cabecalho("📋 EXTRATO DA SESSÃO")

    if not historico:
        print("\n  Nenhuma operação realizada nesta sessão.")
        return

    print(f"\n  {'Operação':<35} {'Valor':>12} {'Saldo após':>12}")
    separador()
    for op in historico:
        sinal = "+" if op['tipo'] == "Depósito" else "-"
        print(f"  {op['tipo']:<35} {sinal}R${op['valor']:>9.2f}  R${op['saldo_apos']:>9.2f}")
    separador()
    print(f"  Saldo atual: R$ {saldo_banco:.2f}")


# ─────────────────────────────────────────
#  MENU PRINCIPAL
# ─────────────────────────────────────────
def menu():
    while True:
        cabecalho("🏦 PYBANK — MENU PRINCIPAL")
        print(f"  Saldo: R$ {saldo_banco:.2f}\n")
        print("  [1] Sacar")
        print("  [2] Depositar")
        print("  [3] Investir")
        print("  [4] Extrato")
        print("  [5] Sair")
        separador()

        try:
            opcao = int(input("  Escolha: "))
        except ValueError:
            print("\n  ❌ Digite apenas números!")
            continue

        if opcao == 1:
            sacar_dinheiro()
        elif opcao == 2:
            depositar_dinheiro()
        elif opcao == 3:
            investir_dinheiro()
        elif opcao == 4:
            exibir_extrato()
        elif opcao == 5:
            separador()
            print("  👋 Obrigado por usar o PyBank! Até logo.")
            separador()
            break
        else:
            print("\n  ❌ Opção inválida!")

        input("\n  Pressione Enter para continuar...")


# ─────────────────────────────────────────
#  INICIALIZAÇÃO
# ─────────────────────────────────────────
if __name__ == "__main__":
    print("\n" + "═" * 40)
    print("        BEM-VINDO AO PYBANK")
    print("═" * 40)

    nome = input("\n  Digite seu nome: ").strip()
    if not nome:
        nome = "Usuário"

    senha = input("  Senha (data de nascimento, ex: 070307): ").strip()

    print(f"\n  ✅ Acesso autorizado!")
    print(f"  Olá, {nome.title()}! Seu saldo inicial é R$ {saldo_banco:.2f}")

    menu()
