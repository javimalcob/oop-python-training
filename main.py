from dominio import cuenta_banco


if __name__ == "__main__":
    mi_cuenta = cuenta_banco.CuentaBanco(1, 15750.24, 'Javier')

    mi_cuenta.depositar(1000)
    mi_cuenta.extraccion(2000)


    print(f"Mi cuenta tiene Codigo {mi_cuenta.get_codigo()}")
    print(f"Mi cuenta tiene Titular : {mi_cuenta.get_titular()}")
    print(f"Mi cuenta tiene Saldo : {mi_cuenta.get_saldo()}")

    
    otra_cuenta = cuenta_banco.CuentaBanco(2, 30000, 'Florencia')

    otra_cuenta.depositar(1500)
    otra_cuenta.extraccion(20000)

    print(f"Mi cuenta tiene Codigo {otra_cuenta.get_codigo()}")
    print(f"Mi cuenta tiene Titular : {otra_cuenta.get_titular()}")
    print(f"Mi cuenta tiene Saldo : {otra_cuenta.get_saldo()}")

    

    if mi_cuenta.get_saldo() > otra_cuenta.get_saldo():
        print(f"La cuenta de mayor saldo es la de {mi_cuenta.get_titular()}")
    elif otra_cuenta.get_saldo() > mi_cuenta.get_saldo():
        print(f"La cuenta de mayor saldo es la de {otra_cuenta.get_titular()}")
    else:
        print("Las cuentas tienen el mismo saldo!")