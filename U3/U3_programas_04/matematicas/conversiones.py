def binario(n: int) -> str:
    sign = "-" if n < 0 else ""
    return sign + format(abs(n), "b")


def hexadecimal(n: int) -> str:
    sign = "-" if n < 0 else ""
    return sign + format(abs(n), "X")


def entero(texto: str) -> int:
    return int(texto.strip())

