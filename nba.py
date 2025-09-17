import pandas as pd

df = pd.read_csv("games.csv") 
season = df[df['SEASON'] == 2019]

season = season.rename(columns={
    'HOME_PTS': 'PTS_home',
    'AWAY_PTS': 'PTS_away'
})

season['TOTAL_POINTS'] = season['PTS_home'] + season['PTS_away']

sample = season[['GAME_DATE_EST', 'HOME_TEAM_ID', 'VISITOR_TEAM_ID', 'PTS_home', 'PTS_away', 'TOTAL_POINTS']].head(500)

def bubble_sort(arr, key):
    arr = arr.to_dict('records') 
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j][key] < arr[j + 1][key]:  
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr


sorted_games = bubble_sort(sample, "TOTAL_POINTS")

# Mostrar el top 10 partidos con más puntos totales
for g in sorted_games[:10]:
    print(f"{g['GAME_DATE_EST']}: {g['HOME_TEAM_ID']} {g['PTS_home']} - {g['VISITOR_TEAM_ID']} {g['PTS_away']} (Total: {g['TOTAL_POINTS']})")


print(pd.DataFrame(sorted_games).head())
