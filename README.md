# Análise de Tendências do YouTube

## Visão geral

Dashboard desenvolvido para apoiar o planejamento de anúncios em vídeo a partir do histórico de conteúdos em alta no YouTube. A análise permite acompanhar categorias, regiões e mudanças diárias no período de 14 de novembro de 2017 a 14 de junho de 2018.

## Objetivos

- Acompanhar o histórico diário dos vídeos em tendência.
- Identificar as categorias com maior presença no período.
- Comparar a distribuição dos registros entre as regiões.
- Avaliar quais categorias se destacam nos Estados Unidos.
- Disponibilizar filtros de data e região para apoiar análises recorrentes.
- Comunicar os resultados em um dashboard e em uma apresentação executiva.

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
├── .gitignore
├── README.md
└── requirements.txt
```

## Como executar o projeto

1. Clone o repositório:

```bash
git clone https://github.com/denise-analytics/youtube-trending-dashboard.git
```

2. Acesse a pasta:

```bash
cd youtube-trending-dashboard
```

3. Crie e ative um ambiente virtual:

```bash
python -m venv .venv

# Windows
.venv\Scripts\activate
```

4. Instale as dependências:

```bash
pip install -r requirements.txt
```

5. Execute o script de validação:

```bash
python analysis/validate_metrics.py
```

O script reproduz os principais indicadores usados no dashboard e na apresentação.

## Ferramentas

- Tableau Public para construção e publicação do dashboard
- Python e pandas para validação das métricas
- PowerPoint para apresentação executiva dos resultados

## Limitações

- A base cobre o período de novembro de 2017 a junho de 2018 e não representa o cenário atual do YouTube.
- O Japão possui uma janela de coleta menor que as demais regiões.
- Um mesmo vídeo pode aparecer na seção de tendências durante vários dias, portanto `videos_count` representa ocorrências agregadas, e não vídeos únicos.

## Arquivos principais

- [Dashboard interativo no Tableau Public](https://public.tableau.com/app/profile/denise.duarte2886/viz/DashboarddeTendnciasdoYouTube_17914333984600/DashboarddetendnciasdoYouTube)
- [Apresentação executiva em PDF](reports/Analise_Tendencias_YouTube.pdf)
- [Baixar apresentação editável em PowerPoint](https://github.com/denise-analytics/youtube-trending-dashboard/raw/refs/heads/main/reports/Analise_Tendencias_YouTube.pptx)
- [Script de validação das métricas](analysis/validate_metrics.py)

## Autora

**Denise Duarte**  
Analista de Dados Júnior | Python | SQL | Excel | Power BI
