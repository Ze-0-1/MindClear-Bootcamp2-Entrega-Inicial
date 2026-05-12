from src.app import obter_conselho
from unittest.mock import patch

def test_obter_conselho_sucesso():
    """Valida se a função lida corretamente com uma resposta bem-sucedida da API."""
    # Simulamos (mock) a resposta da API externa para não depender da internet no CI
    with patch('src.app.requests.get') as mock_get:
        mock_get.return_value.status_code = 200
        mock_get.return_value.json.return_value = {
            "slip": {
                "advice": "Sempre faça testes automatizados."
            }
        }
        
        conselho = obter_conselho()
        assert conselho == "Sempre faça testes automatizados."

def test_obter_conselho_falha():
    """Valida se a função retorna o conselho padrão em caso de erro na API."""
    with patch('src.app.requests.get') as mock_get:
        # Simulamos um erro 500 (Internal Server Error)
        mock_get.return_value.status_code = 500
        
        conselho = obter_conselho()
        # Deve retornar a string de fallback definida no app.py
        assert conselho == "Mantenha a mente limpa e focada."