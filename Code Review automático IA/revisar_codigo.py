from pathlib import Path

#pip install openai
from openai import OpenAI

#pip install python-dotenv
from dotenv import load_dotenv


# CARGAR VARIABLES DEL ARCHIVO .env
# ==========================================

carpeta_actual = Path(__file__).parent
ruta_env = carpeta_actual / ".env"

load_dotenv(ruta_env)



client = OpenAI()
# ==========================================
# LEER app.py
# ==========================================

ruta_app = carpeta_actual / "app.py"

with open(ruta_app, "r", encoding="utf-8") as archivo:
    codigo = archivo.read()

prompt = f"""
Actúa como revisor senior de código Python.

Analiza el siguiente código:

{codigo}

Busca:
- errores potenciales;
- validaciones faltantes;
- problemas de mantenibilidad;
- malas prácticas;
- oportunidades de refactorización.

Para cada problema indica:
1. Problema
2. Severidad: LOW, MEDIUM, HIGH o CRITICAL
3. Explicación
4. Recomendación

No modifiques el código.
"""

response = client.responses.create(
    model="gpt-5.6",
    input=prompt
)

print("\n========== REPORTE DE CODE REVIEW CON IA ==========\n")
print(response.output_text)
