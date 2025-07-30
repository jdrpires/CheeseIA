from avaliacao_analyzer import AvaliacaoAnalyzer

# Exemplo de uso
analyzer = AvaliacaoAnalyzer()

# Dados de exemplo
avaliacoes_exemplo = [
    ("Produto chegou com defeito, muito ruim", 1),
    ("Qualidade excelente, superou expectativas", 5),
    ("Produto ok, mas embalagem amassada", 3),
    ("Atendimento péssimo, produto bom", 3),
    ("Perfeito em todos os aspectos!", 5)
]

# Processar avaliações
resultados = analyzer.processar_lote(avaliacoes_exemplo)

# Ordenar da melhor para pior
resultados_ordenados = analyzer.ordenar_por_qualidade(resultados)

# Exibir resultados
print("=== AVALIAÇÕES ORDENADAS (MELHOR → PIOR) ===\n")
for i, resultado in enumerate(resultados_ordenados, 1):
    print(f"{i}. CATEGORIA: {resultado.categoria}")
    print(f"   SENTIMENTO: {resultado.sentimento}")
    print(f"   SCORE: {resultado.score:.2f}")
    print(f"   POSITIVOS: {', '.join(resultado.pontos_positivos)}")
    print(f"   NEGATIVOS: {', '.join(resultado.pontos_negativos)}")
    print("-" * 50)