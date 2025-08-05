import discordrpc
import time

from ..core.utils import FSTUtils

class FSTDiscordRPC:
    def __init__(self, client_id: str):
        self.client_id = client_id
        self.rpc = discordrpc.RPC(app_id=self.client_id, output=False)
        
        FSTUtils.print_info("Connected to Discord.")
        FSTUtils.print_spacer()
            
    def set_presence(self, state: str, details: str):
        self.rpc.set_activity(
            state=state,
            details=details
        )