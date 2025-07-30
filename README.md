# CheeseIA - Analisador de Avaliações

Sistema para análise e categorização automática de avaliações de produtos usando IA.

## Configuração

1. Instale as dependências:
```bash
pip install -r requirements.txt
```

2. Configure sua chave da OpenAI:
```bash
cp .env.example .env
# Edite o arquivo .env com sua chave
```

## Uso Básico

```python
from avaliacao_analyzer import AvaliacaoAnalyzer

analyzer = AvaliacaoAnalyzer()

# Analisar uma avaliação
resultado = analyzer.analisar_avaliacao("Produto excelente!", 5)

# Processar várias avaliações
avaliacoes = [("texto1", nota1), ("texto2", nota2)]
resultados = analyzer.processar_lote(avaliacoes)

# Ordenar por qualidade
ordenados = analyzer.ordenar_por_qualidade(resultados)
```

## Categorias

- Qualidade do produto
- Apresentação do Produto
- Experiência geral