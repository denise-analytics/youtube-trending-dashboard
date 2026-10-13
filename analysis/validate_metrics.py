"""Valida os principais indicadores usados no dashboard e na apresentação."""

from pathlib import Path

import pandas as pd


DATA_PATH = Path(__file__).resolve().parents[1] / "data" / "trending_by_time.csv"


def format_percent(value: float) -> str:
    """Formata uma proporção como percentual com uma casa decimal."""
    return f"{value:.1%}".replace(".", ",")


def main() -> None:
    """Carrega a base e imprime os indicadores de validação."""
    data = pd.read_csv(DATA_PATH, parse_dates=["trending_date"])

    total_videos = data["videos_count"].sum()

    category_totals = (
        data.groupby("category_title", as_index=False)["videos_count"]
        .sum()
        .sort_values("videos_count", ascending=False)
    )
    category_totals["share"] = category_totals["videos_count"] / total_videos

    region_totals = (
        data.groupby("region", as_index=False)["videos_count"]
        .sum()
        .sort_values("videos_count", ascending=False)
    )
    region_totals["share"] = region_totals["videos_count"] / total_videos

    collection_windows = data.groupby("region")["trending_date"].agg(["min", "max", "nunique"])
    common_start = collection_windows["min"].max()
    common_period = data.loc[data["trending_date"] >= common_start]
    common_region_totals = common_period.groupby("region")["videos_count"].sum()
    japan_common_share = common_region_totals["Japan"] / common_region_totals.sum()

    print(f"Total de vídeos contabilizados: {total_videos:,.0f}".replace(",", "."))
    print("\nCategorias com maior volume:")
    for row in category_totals.head(5).itertuples(index=False):
        print(f"- {row.category_title}: {row.videos_count:,.0f} ({format_percent(row.share)})")

    print("\nParticipação por região:")
    for row in region_totals.itertuples(index=False):
        print(f"- {row.region}: {format_percent(row.share)}")

    print("\nJanela de coleta por região:")
    print(collection_windows.to_string())
    print(
        f"\nParticipação do Japão no período comum iniciado em "
        f"{common_start:%d/%m/%Y}: {format_percent(japan_common_share)}"
    )


if __name__ == "__main__":
    main()
