from src.app import obter_conselho
from unittest.mock import patch, Mock

def test_obter_conselho_sucesso():
    """Valida se a função lida corretamente com as duas APIs (Conselho e Tradução)."""
    with patch('src.app.requests.get') as mock_get:
        # 1º Mock: Simula a resposta da API em Inglês
        mock_ingles = Mock()
        mock_ingles.status_code = 200
        mock_ingles.json.return_value = {"slip": {"advice": "Always write tests."}}

        # 2º Mock: Simula a resposta da API de Tradução
        mock_ptbr = Mock()
        mock_ptbr.status_code = 200
        mock_ptbr.json.return_value = {"responseData": {"translatedText": "Sempre faça testes automatizados."}}

        # side_effect diz ao Python: "Na primeira vez que chamarem requests.get, 
        # entregue o mock_ingles. Na segunda vez, entregue o mock_ptbr."
        mock_get.side_effect = [mock_ingles, mock_ptbr]

        conselho = obter_conselho()
        assert conselho == "Sempre faça testes automatizados."

def test_obter_conselho_falha():
    """Valida o comportamento caso a API saia do ar."""
    with patch('src.app.requests.get') as mock_get:
        mock_get.return_value.status_code = 500
        conselho = obter_conselho()
        assert conselho == "Mantenha a mente limpa e focada."