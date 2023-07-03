import click
import textwrap
import re


def is_valid_date(date_str):
    pattern = r"^\d{2}-\d{2}-\d{4}$"
    match = re.match(pattern, date_str)
    return bool(match)


def display_menu():
    menu = """\n
    ============ Opções ============
    [d] Depositar
    [s] Sacar
    [e] Extrato
    [nc] Nova conta
    [lc] Listar contas
    [nu] Novo usuário
    [q] Sair
    """
    return click.prompt(textwrap.dedent(menu), type=str)


def deposit(balance, value, extract, /):
    if value > 0:
        balance += value
        extract += f"Depósito: R$ {value:.2f}\n"
    else:
        click.echo(
            click.style(
                "\nOperação falhou! O valor informado é inválido.", bg="red", fg="white"
            )
        )

    click.echo(click.style("\nValor depositado com sucesso", bg='green', fg='white'))
    return balance, extract


def withdraw(*, balance, value, extract, limit, number_withdrawals, withdrawal_limit):
    exceeded_balance = value > balance
    exceeded_limit = value > limit
    exceeded_withdrawals = number_withdrawals >= withdrawal_limit

    if exceeded_balance:
        click.echo(
            click.style(
                "\nOperação falhou! Você não tem saldo suficiente.",
                bg="red",
                fg="white",
            )
        )
    elif exceeded_limit:
        click.echo(
            click.style(
                "\nOperação falhou! O valor do saque excede o limite.",
                bg="red",
                fg="white",
            )
        )
    elif exceeded_withdrawals:
        click.echo(
            click.style(
                "\nOperação falhou! Número máximo de saques excedido.",
                bg="red",
                fg="white",
            )
        )
    elif value > 0:
        balance -= value
        extract += f"Saque: R$ {value:.2f}\n"
        number_withdrawals += 1
    else:
        click.echo(
            click.style(
                "\nOperação falhou! O valor informado é inválido.", bg="red", fg="white"
            )
        )

    click.echo(click.style("\nValor sacado com sucesso", bg='green', fg='white'))
    return balance, extract


def display_extract(balance, /, *, extract):
    click.echo("\n============= EXTRATO =============")
    click.echo("\nNão foram realizadas movimentações." if not extract else extract)
    click.echo(f"\nSaldo: R$ {balance:.2f}")
    click.echo("=====================================")


def create_user(users):
    cpf = click.prompt("Informe o CPF (somente número)", type=int)
    user = filter_user(cpf, users)

    if user:
        click.echo("\nJá existe usuário com esse CPF!")
        return

    name = click.prompt("Informe o nome completo", type=str)

    while True:
        birthday = input("Informe a data de nascimento (dd-mm-aaaa): ")
        if is_valid_date(birthday):
            break
        else:
            print("Formato de data inválido. Por favor, tente novamente.")

    address = click.prompt(
        "Informe o endereço (logradouro, nro - bairro - cidade/sigla estado)"
    )

    users.append(
        {"nome": name, "data_nascimento": birthday, "cpf": cpf, "endereço": address}
    )

    click.echo(click.style("\nUsuário criado com sucesso!", bg='green', fg='white'))


def filter_user(cpf, users):
    users_filtered = [user for user in users if user["cpf"] == cpf]
    return users_filtered[0] if users_filtered else None


def create_account(agency, account_number, users):
    cpf = click.prompt("informe o CPF do usuário", type=int)
    user = filter_user(cpf, users)

    if user:
        click.echo(click.style("\nConta criada com sucesso!", bg='green', fg='white'))
        return {"agencia": agency, "numero_conta": account_number, "usuario": user}

    click.echo("\nUsuário não encontrado, fluxo de criação de conta encerrado!")


def list_accounts(accounts):
    for account in accounts:
        line = f"""\
            \nAgency:\t{account['agencia']}
            C/C:\t{account['numero_conta']}
            Titular:\t{account['usuario']['nome']}
            """
        click.echo("=" * 100)
        click.echo(textwrap.dedent(line))


@click.command()
@click.version_option("1.0")
def main():
    balance = 0
    number_withdrawals = 0
    limit = 500
    extract = ""
    users = []
    accounts = []

    WITHDRAWAL_LIMIT = 3
    AGENCY = "0001"

    while True:
        option = display_menu()

        if option == "d":
            value = click.prompt("Informe o valor do depósito", type=float)
            balance, extract = deposit(balance, value, extract)
        elif option == "s":
            value = click.prompt("Informe o valor do saque", type=float)
            balance, extract = withdraw(
                balance=balance,
                value=value,
                extract=extract,
                limit=limit,
                number_withdrawals=number_withdrawals,
                withdrawal_limit=WITHDRAWAL_LIMIT,
            )

        elif option == "e":
            display_extract(balance, extract=extract)

        elif option == "nu":
            create_user(users)

        elif option == "nc":
            account_number = len(accounts) + 1
            account = create_account(AGENCY, account_number, users)

            if account:
                accounts.append(account)

        elif option == "lc":
            list_accounts(accounts)

        elif option == "q":
            break

        else:
            click.echo(
                click.style(
                    "\nOperação inválida, por favor selecione novamente a operação desejada.",
                    bg="red",
                    fg="white",
                )
            )


if __name__ == "__main__":
    main()
