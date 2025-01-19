import azure.functions as func
import logging
import json

app = func.FunctionApp(http_auth_level=func.AuthLevel.FUNCTION)

@app.route(route="http_trigger_cpf")
def http_trigger_cpf(req: func.HttpRequest) -> func.HttpResponse:
    logging.info("Recebida uma solicitação para validação de CPF. - Azure")

    cpf = req.params.get('cpf')
    try:
        if not cpf:
            return func.HttpResponse(
                    json.dumps({"error": "O parâmetro 'cpf' é obrigatório."}),
                    status_code=400,
                    mimetype="application/json"
                )

        valido = validar_cpf(cpf)
        return func.HttpResponse(
            json.dumps({"cpf": cpf, "valido": valido}),
            status_code=200 if valido else 400,
            mimetype="application/json"
        )
    
    except Exception as e:
        logging.error(f"Erro: {str(e)}")
        return func.HttpResponse(
            json.dumps({"error": "Erro interno no servidor."}),
            status_code=500,
            mimetype="application/json"
        )
    
def validar_cpf(cpf: str) -> bool:
    # Remove caracteres não numéricos
    cpf = ''.join(filter(str.isdigit, cpf))
    
    # Validação inicial
    if len(cpf) != 11 or cpf in (c * 11 for c in "0123456789"):
        return False

    # Cálculo dos dígitos verificadores
    for i in range(9, 11):
        soma = sum(int(cpf[num]) * ((i + 1) - num) for num in range(0, i))
        digito = (soma * 10) % 11
        if digito == 10:
            digito = 0
        if digito != int(cpf[i]):
            return False

    return True
