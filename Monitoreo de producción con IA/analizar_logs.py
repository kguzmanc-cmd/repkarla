from openai import OpenAI

client = OpenAI(
    api_key="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"
)

with open("app.log", "r", encoding="utf-8") as archivo:
    logs = archivo.read()


prompt = f"""
Actúa como especialista en monitoreo de aplicaciones.

Analiza los siguientes logs:

{logs}

Genera un reporte indicando:

1. Problema principal detectado.
2. Errores encontrados.
3. Patrones encontrados.
4. Posibles causas.
5. Nivel de severidad.
6. Acciones recomendadas.

Diferencia claramente entre:

- evidencia encontrada en los logs;
- hipótesis sobre la posible causa.
"""


response = client.responses.create(
    model="gpt-5.6",
    input=prompt
)


print(response.output_text)