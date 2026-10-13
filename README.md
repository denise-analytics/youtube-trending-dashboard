# Análise de Tendências do YouTube

Dashboard desenvolvido para apoiar o planejamento de anúncios em vídeo a partir do histórico de conteúdos em alta no YouTube. A análise permite acompanhar categorias, regiões e mudanças diárias no período de 14 de novembro de 2017 a 14 de junho de 2018.

## Dashboard

[Acessar o dashboard interativo no Tableau Public](https://public.tableau.com/app/profile/denise.duarte2886/viz/DashboarddeTendnciasdoYouTube_17914333984600/DashboarddetendnciasdoYouTube)

O painel contém:

- histórico diário do número de vídeos em alta por categoria;
- participação percentual das categorias ao longo do tempo;
- distribuição dos registros por região;
- tabela de realce para comparar categorias e regiões;
- filtros globais de data e região.

## Principais resultados

- **Entertainment** lidera com 95.008 registros, equivalentes a 27,9% do total.
- **People & Blogs** ocupa o segundo lugar, com 44.700 registros.
- Os **Estados Unidos** concentram 23,8% dos registros no período analisado.
- Nos Estados Unidos, **Music** apresenta participação 7,6 pontos percentuais maior do que nas demais regiões.
- **Howto & Style** também se destaca nos Estados Unidos, com diferença positiva de 5,7 pontos percentuais.
- O Japão representa 10,8% do período total, mas seus dados começam apenas em 07/02/2018. Na janela comum a todas as regiões, sua participação fica próxima de 17%.

## Dados

O arquivo contém registros agregados por data, região e categoria.

| Campo | Descrição |
|---|---|
| `record_id` | Identificador do registro |
| `region` | País ou região geográfica |
| `trending_date` | Data em que o conteúdo esteve em alta |
| `category_title` | Categoria do vídeo |
| `videos_count` | Número de vídeos em alta |

## Estrutura do repositório

```text
youtube-trending-dashboard/
├── analysis/
│   └── validate_metrics.py
├── data/
│   └── trending_by_time.csv
├── reports/
│   ├── Analise_Tendencias_YouTube.pdf
│   └── Analise_Tendencias_YouTube.pptx
├── README.md
└── requirements.txt
```

## Validação das métricas

O script em `analysis/validate_metrics.py` reproduz os indicadores usados na apresentação.

```bash
python -m venv .venv

# Windows
.venv\Scripts\activate

pip install -r requirements.txt
python analysis/validate_metrics.py
```

## Ferramentas

- Tableau Public para construção e publicação do dashboard
- Python e pandas para validação das métricas
- PowerPoint para apresentação executiva dos resultados

## Limitações

- A base cobre o período de novembro de 2017 a junho de 2018 e não representa o cenário atual do YouTube.
- O Japão possui uma janela de coleta menor que as demais regiões.
- Um mesmo vídeo pode aparecer na seção de tendências durante vários dias, portanto `videos_count` representa ocorrências agregadas, e não vídeos únicos.

## Autora

Denise Duarte
