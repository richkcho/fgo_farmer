from typing import List

class Image:
    pass

class BattleScreenEnemyInfo:
    def __init__(self,
                 name: str,
                 cls: str,
                 is_servant: bool,
                 lv: int,
                 hp: int,
                 cur_np_charge: int,
                 max_np_charge: int) -> None:
        self.name = name
        self.cls = cls
        self.is_servant = is_servant
        self.lv = lv
        self.hp = hp
        self.cur_np_charge = cur_np_charge
        self.max_np_charge = max_np_charge

class BattleScreenServantInfo:
    def __init__(self,
                 name: str,
                 lv: int,
                 hp: int,
                 np: int) -> None:
        self.name = name
        self.lv = lv
        self.hp = hp
        self.np = np

class BattleScreenInfo:
    def __init__(self,
            enemies: List[BattleScreenEnemyInfo],
            servants: List[BattleScreenServantInfo],
            crit_stars: int) -> None:
        self.enemies = enemies
        self.servants = servants
        self.crit_stars = crit_stars

class CommandCardInfo:
    def __init__(self,
                 servant: str,
                 card_type: str,
                 crit_rate: int,
                 is_np: bool) -> None:
        self.servant = servant
        self.card_type = card_type
        self.crit_rate = crit_rate
        self.is_np = is_np

class PartyScreenServantInfo:
    def __init__(self,
                 name: str,
                 lv: int,
                 max_hp: int,
                 max_np: int) -> None:
        self.name = name
        self.lv = lv
        self.max_hp = max_hp
        self.max_np = max_np
