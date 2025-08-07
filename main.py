from dominio import cuenta_banco


if __name__ == "__main__":
    mi_cuenta = cuenta_banco.CuentaBanco(1, 10000, 'Javier')
    print(f"Mi cuenta tiene codigo {mi_cuenta.get_codigo()}")
