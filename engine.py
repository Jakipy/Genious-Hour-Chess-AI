class Gamestate():
    def __init__(self):
        self.board = [
            ["bR","bN","bB","bQ","bK","bB","bN","bR"]
            ["bP","bP","bP","bP","bP","bP","bP","bP"]
            ["bR","bN","bB","bQ","bK","bB","bN","bR"]
            ["bR","bN","bB","bQ","bK","bB","bN","bR"]
            ["bR","bN","bB","bQ","bK","bB","bN","bR"]
            ["bR","bN","bB","bQ","bK","bB","bN","bR"]
            ["wP","wP","wP","wP","wP","wP","wP","wP"]
            ["wR","wN","wB","wQ","wK","wB","wN","wR"]

        ]

        self.whitetomove = True
        self.Movelog = []
