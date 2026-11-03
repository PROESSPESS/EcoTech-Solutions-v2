"""
seguridad.py
Módulo encargado de la autenticación segura y hashing de credenciales 
para la aplicación EcoTech Solutions.
"""

import hashlib
import os
from dotenv import load_dotenv

# Cargamos las variables definidas en el archivo .env
load_dotenv()


def calcular_hash(psw: str) -> str:

#    Recibe una contraseña en texto plano y devuelve su representación
#    en hash SHA-256 en formato hexadecimal.

    psw_bytes = psw.encode('utf-8')
    return hashlib.sha256(psw_bytes).hexdigest()


def validar_credenciales(usuario: str, contrasena: str) -> tuple[bool,str]:

#    Valída que los campos no estén vacíos y compara con las credenciales
#    definidas de forma segura en las variables de entorno.
#    Retorna (True, 'mensaje') si es correcto, o (False, 'mensaje') si falla.

    # 1. Validación de entradas
    usuario_clean = usuario.strip()

    # Se remueve el strip() en la contraseña para no descartar espacios
    # intencionales que formen parte del password original.
    if not usuario_clean or not contrasena:
        return False, "El usuario y la contraseña no pueden estar vacíos."

    # 2. Obtenemos las credenciales esperadas desde el archivo .env
    admin_esperado = os.getenv("ADMIN_USER")
    hash_esperado = os.getenv("ADMIN_HASH")

    if not admin_esperado or not hash_esperado:
        return False, "Error: no se encontraron las credenciales en .env."

    # 3. Calculamos el hash de la contraseña ingresada por el usuario
    hash_input = calcular_hash(contrasena)

    if usuario_clean == admin_esperado and hash_input == hash_esperado:
        return True, "Usuario correcto"
    else:
        return False, "Usuario o contraseña incorrectos"



