from app_service import *
from unittest.mock import patch, MagicMock 


def test_validar_campos_completos():
    data = {
        "cpf_comprador": "123",
        "cpf_vendedor": "456",
        "ticker": "PETR4",
        "quantidade": 10
    }
    assert validar_campos(data) is None

def test_validar_campos_incompletos():
    data ={
        "cpf_vendedor": "456",
        "ticker": "PETR4",
        "quantidade": 10

    }
    assert validar_campos(data) == "Campo obrigatório 'cpf_comprador' não informado"

@patch ("app_service.requests.get")
def teste_validar_calcular_valor_ok(mock_get):
    mock_response = MagicMock()
    mock_response.status_code = 200
    mock_response.json.return_value = {"ticker":"PETR4","lastValue":10}
    mock_get.return_value = mock_response

    valor, erro = calcular_valor("PETR4",10) 

    assert valor == 100.0
    assert erro is None

    mock_get.assert_called_once_with("http://localhost:8080/stocks/PETR4",timeout= 5)


@patch ("app_service.requests.get")
def teste_validar_calcular_valor_erro(mock_get):
    mock_response = MagicMock()
    mock_response.status_code = 404
    erro,msg =  calcular_valor("AAAA",10) 
    assert erro is None
    assert msg =="Erro ao buscar ticker 'AAAA'"


    mock_get.assert_called_once_with("http://localhost:8080/stocks/AAAA",timeout= 5)


def teste_validar_criar_objeto_movimentacao():
    data = {
        "cpf_comprador": "123",
        "cpf_vendedor": "456",
        "ticker": "PETR4",
        "quantidade": 10,
        "valor_movimentacao": 20
        

    }
    assert criar_objeto_movimentacao(data,20) == data

    
