from dataclasses import dataclass
from datetime import datetime
from typing import Dict, List

@dataclass
class CropSeason:
    name: str
    best_planting_months: List[int]
    description: str
    recommended_crops: List[str]

SEASONS = {
    'Spring': CropSeason(
        name='Spring',
        best_planting_months=[2, 3, 4],
        description='Ideal time for crops requiring moderate temperatures and regular rainfall',
        recommended_crops=['Tomatoes', 'Cucumbers', 'Spinach', 'Carrots', 'Peas']
    ),
    'Summer': CropSeason(
        name='Summer',
        best_planting_months=[5, 6, 7],
        description='Best for heat-resistant crops and those needing long sunny days',
        recommended_crops=['Corn', 'Beans', 'Squash', 'Okra', 'Watermelon']
    ),
    'Fall': CropSeason(
        name='Fall',
        best_planting_months=[8, 9, 10],
        description='Suitable for cool-weather crops and root vegetables',
        recommended_crops=['Broccoli', 'Cabbage', 'Kale', 'Radishes', 'Beets']
    ),
    'Winter': CropSeason(
        name='Winter',
        best_planting_months=[11, 12, 1],
        description='Greenhouse cultivation and cold-hardy winter crops',
        recommended_crops=['Garlic', 'Onions', 'Winter Wheat', 'Lettuce', 'Brussels Sprouts']
    )
}

def get_current_season() -> CropSeason:
    current_month = datetime.now().month
    for season in SEASONS.values():
        if current_month in season.best_planting_months:
            return season
    return SEASONS['Spring']

def get_recommended_crops(month: int = None) -> Dict[str, List[str]]:
    if month is None:
        month = datetime.now().month
    return {season.name: season.recommended_crops for season in SEASONS.values() if month in season.best_planting_months}