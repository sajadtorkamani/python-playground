import re


def nba_cup(results_str: str, team: str) -> str:
    if team == "":
        return ""

    stats = {
        "wins": 0,
        "draws": 0,
        "losses": 0,
        "points_scored": 0,
        "points_conceded": 0,
        "total_points": 0
    }

    result_rows = results_str.split(",")

    for row in result_rows:
        try:
            # Extract info about each match
            rows = re.split("(?<=\d)\s(?=\w)", row)
            home_team = get_team_info(rows[0])
            home_team_score = home_team["score"]
            home_team_name = home_team["name"]
            away_team = get_team_info(rows[1])
            away_team_score = away_team["score"]
            away_team_name = away_team["name"]

            # Ignore other matches that don't involve the team in question
            if team not in [home_team_name, away_team_name]:
                continue

            is_home_team = team == home_team_name

            # Build stats
            # ---------------------

            # Handle draws
            if home_team_score == away_team_score:
                stats["draws"] += 1
                stats["total_points"] += 1

            # Handle home team
            elif is_home_team:
                if home_team_score > away_team_score:
                    stats["wins"] += 1
                    stats["total_points"] += 3
                else:
                    stats["losses"] += 1

            # Handle away team
            else:
                if away_team_score > home_team_score:
                    stats["wins"] += 1
                    stats["total_points"] += 3
                else:
                    stats["losses"] += 1

            if is_home_team:
                stats["points_scored"] += home_team_score
                stats["points_conceded"] += away_team_score
            else:
                stats["points_scored"] += away_team_score
                stats["points_conceded"] += home_team_score
        except:
            return f"Error(float number):{row}"

    is_valid_team = (stats["wins"] + stats["losses"] + stats["draws"]) > 0

    if is_valid_team:
        return format_stats(team, stats)
    else:
        return f"{team}:This team didn't play!"


def get_team_info(row: str) -> dict:
    parts = row.split(' ')
    score = parts.pop()
    team_name = ' '.join(parts)

    return {"name": team_name, "score": int(score)}


def format_stats(team: str, stats: dict) -> str:
    stats = {
        "W": stats["wins"],
        "D": stats["draws"],
        "L": stats["losses"],
        "Scored": stats["points_scored"],
        "Conceded": stats["points_conceded"],
        "Points": stats["total_points"],
    }

    result = ''

    for key, value in stats.items():
        result += f"{key}={value};"

    return f"{team}:{result}"[:-1]
