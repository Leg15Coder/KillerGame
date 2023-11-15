class AccessError(Exception):
    def __init__(self, text: str):
        self.txt = text
