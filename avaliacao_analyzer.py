import os
import json
from typing import Dict, List, Tuple
from dataclasses import dataclass
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

@dataclass
class AvaliacaoResult:
    categoria: str
    sentimento: str
    score: float
    pontos_positivos: List[str]
    pontos_negativos: List[str]

class AvaliacaoAnalyzer:
    def __init__(self):
        self.client = OpenAI(api_key=os.getenv('OPENAI_API_KEY'))
        self.categorias = [
            "Qualidade do produto",
            "Apresentação do Produto", 
            "Experiência geral"
        ]
    
    def analisar_avaliacao(self, texto_avaliacao: str, nota: int) -> AvaliacaoResult:
        prompt = f"""
        Analise esta avaliação de produto:
        
        Texto: "{texto_avaliacao}"
        Nota dada: {nota}/5
        
        Categorize em uma das opções: {', '.join(self.categorias)}
        
        Retorne APENAS um JSON válido com:
        {{
            "categoria": "categoria principal",
            "sentimento": "positivo/neutro/negativo",
            "score": 0.0-1.0,
            "pontos_positivos": ["ponto1", "ponto2"],
            "pontos_negativos": ["ponto1", "ponto2"]
        }}
        """
        
        response = self.client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": prompt}],
            temperature=0.3
        )
        
        result_json = json.loads(response.choices[0].message.content)
        
        return AvaliacaoResult(
            categoria=result_json["categoria"],
            sentimento=result_json["sentimento"],
            score=result_json["score"],
            pontos_positivos=result_json["pontos_positivos"],
            pontos_negativos=result_json["pontos_negativos"]
        )
    
    def processar_lote(self, avaliacoes: List[Tuple[str, int]]) -> List[AvaliacaoResult]:
        resultados = []
        for texto, nota in avaliacoes:
            resultado = self.analisar_avaliacao(texto, nota)
            resultados.append(resultado)
        return resultados
    
    def ordenar_por_qualidade(self, resultados: List[AvaliacaoResult]) -> List[AvaliacaoResult]:
        return sorted(resultados, key=lambda x: x.score, reverse=True)