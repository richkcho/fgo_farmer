from typing import List
from models import *

class CvInterface:
    @staticmethod
    def getBattleScreenInfo(battle_screen_img: Image) -> BattleScreenInfo:
        '''Grab information from the in-battle screen'''
        pass
    
    @staticmethod
    def getPartyScreenInfo(party_screen_img: Image) -> List[PartyScreenServantInfo]:
        '''Grab information from the selection screen'''
        pass

    @staticmethod 
    def getCommandCardInfo(command_phase_img: Image) -> List[CommandCardInfo]:
        '''Grab information from the command cards screen'''
        pass

# Call CvMagic.getBattleScreenInfo(img)
class CvMagic(CvInterface):
    pass
