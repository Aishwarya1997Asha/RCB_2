import json
import os


# create an instance variable and assign with instance variable of json file

class Cricket:
    _text_player = "player"
    _text_role = "role"
    _text_country = 'country'

    def __init__(self, json_file_):
        self.json_file_players = json_file_

    # created object here and checking 2 for string and dict obj
    def _get_file(self):
        if isinstance(self.json_file_players, str):
            with open(self.json_file_players) as file:
                obj = json.load(file)
            return obj
        elif isinstance(self.json_file_players, dict):
            return self.json_file_players

    # checks how many no of players are there or not
    def players_count(self):
        players = self._get_file().get(self._text_player)
        return len(players)

    # returns wicket keeper or countries using type_name and type
    def players_type(self, type_, type_name, not_in=False):
        players = self._get_file().get(self._text_player)
        if not_in:
            return list(filter(lambda con: con.get(type_) != type_name, players))
        else:
            return list(filter(lambda con: con.get(type_) == type_name, players))

    # filters the countries
    def country_filter(self, country="india", not_in=False):
        country = country.title()
        flag = country and not_in
        return self.players_type(self._text_country, country, not_in=True) if flag \
            else self.players_type(self._text_country, country)

    # role of the player it finds out
    def role_filter(self, role="Wicket-keeper", not_in=False):
        role = role.capitalize()
        flag = role and not_in
        return self.players_type(self._text_role, role, not_in=True) if flag \
            else self.players_type(self._text_role, role)