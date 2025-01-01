import csv
from darts.models import Games, Players, Matches


def insert_from_csv():

    with open('games.csv', mode='r') as file:

        matches = get_foreign_instances(Matches)
        players = get_foreign_instances(Players)

        reader = csv.DictReader(file)
        
        objects = []
        for row in reader:
            match_id = int(row['MatchID'])
            player_id = int(row['PlayerID'])
            game = Games(
                match=matches[match_id],
                player=players[player_id],
                points=int(row['Points']),
                darts=int(row['Darts']),
                result=row['Result']
            )
            objects.append(game)
                
    Games.objects.bulk_create(objects)
    print(f"Inserted {len(objects)} records.")


def show_players():
    model = Players
    players = model.objects.all()
    for player in players:
        print(player.id, player)


def show_matches():
    model = Matches
    matches = model.objects.all()
    print("loop 1:")
    for match in matches:
        print(match.id, match)
    matches = {match.id: match for match in Matches.objects.all()}
    print("loop 2")
    for i in range(1, len(matches)):
        print(i, matches[i])


def show_games():
    for game in Games.objects.all():
        print(game.id, game)


def get_foreign_instances(model):

    return {instance.id: instance for instance in model.objects.all()}
