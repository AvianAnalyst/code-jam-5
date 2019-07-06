import json
from pathlib import Path
from typing import Dict
from colorama import Fore
from .investment import Investment
from .organization import Organization
from .planetary_effects import PlanetaryEffects
from .policy import Policy


class InvestmentOptions:
    def __init__(self) -> None:
        self.options = self.create_investements()

    def __str__(self) -> str:
        menu = []
        menu.append(Fore.CYAN + "Investment options:" + Fore.WHITE)
        for key, i in self.options.items():
            if i.current_policy:
                menu.append(f"{key}: {i.organization.name}")
            else:
                menu.append(Fore.RED + f"{key}: {i.organization.name}" + Fore.WHITE)
        return "\n".join(menu)

    def _parse_json(self, file_location: str) -> Dict:
        """Helper function to load a json and dump it to a dictionary"""
        with open(file_location, mode="r") as json_file:
            raw_json = json.loads(json_file.read())
        return raw_json

    def create_investements(self) -> Dict:
        """From a json file with CEOs, organization names and policies creates
            a dictionary of options for the player"""
        path = Path().cwd().resolve()
        raw_json = self._parse_json(path / "resources" / "data" / "organizations.json")
        investement_list = []
        for entry in raw_json:
            org = Organization(entry["name"], entry["ceo"], entry["description"])
            policy_list = []
            for policies in entry["policies"]:
                planet_effects = PlanetaryEffects(
                    policies["bio"],
                    policies["temperature"],
                    policies["co2"],
                    policies["habitable_land"],
                )
                policy = Policy(
                    policies["name"],
                    policies["description"],
                    planet_effects,
                    policies["roi"],
                )
                policy_list.append(policy)
            new_investment = Investment(org, policy_list)
            investement_list.append(new_investment)

        investement_options = {}
        for index, investment in enumerate(investement_list):
            investement_options[str(index + 1)] = investment

        return investement_options
