import click
import os

menu = """
[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair
"""

@click.command()
def main():
    balance = 0
    number_withdrawals = 0
    limit = 500
    extract = ""
    WITHDRAWAL_LIMIT = 3

    while True:

        option = click.prompt(f"Escolha uma das opções: {menu}")

        if option == "d":
            value = click.prompt("Informe o valor do deposito", type=float)
            
            if value > 0:
                balance += value
                extract += f"Depósito: R$ {value:.2f}\n"

            else:
                click.echo("Operação falhou! O valor informado é inválido.")

        elif option == "s":
            value = click.prompt("Informe o valor do saque", type=float)

            exceeded_balance = value > balance

            exceeded_limit = value > limit

            exceeded_withdrawals = number_withdrawals >= WITHDRAWAL_LIMIT

            if exceeded_balance:
                click.echo("Operação falhou! Você não tem saldo suficiente.")
            elif exceeded_limit:
                click.echo("Operação falhou! O valor do saque excede o limite.")
            elif exceeded_withdrawals:
                click.echo("Operação falhou! Número máximo de saques excedido.")
            elif value > 0:
                balance -= value
                extract += f"Saque: R$ {value:.2f}\n"
                number_withdrawals += 1
            else:
                click.echo("Operação falhou! O valor informado é inválido.")

        elif option == "e":
            click.echo("\n============= EXTRATO =============")
            click.echo(
                "Não foram realizadas movimentações." if not extract else extract
            )
            click.echo(f"\nSaldo: R$ {balance:.2f}")
            click.echo("=====================================")
            break

        elif option == "q":
            break

        else:
            click.echo(
                "Operação inválida, por favor selecione novamente a operação desejada."
            )


if __name__ == "__main__":
    main()
