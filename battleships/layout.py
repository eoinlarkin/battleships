logo = """
    ██████╗  █████╗ ████████╗████████╗██╗     ███████╗███████╗██╗  ██╗██╗██████╗ ███████╗
    ██╔══██╗██╔══██╗╚══██╔══╝╚══██╔══╝██║     ██╔════╝██╔════╝██║  ██║██║██╔══██╗██╔════╝
    ██████╔╝███████║   ██║      ██║   ██║     █████╗  ███████╗███████║██║██████╔╝███████╗
    ██╔══██╗██╔══██║   ██║      ██║   ██║     ██╔══╝  ╚════██║██╔══██║██║██╔═══╝ ╚════██║
    ██████╔╝██║  ██║   ██║      ██║   ███████╗███████╗███████║██║  ██║██║██║     ███████║
    ╚═════╝ ╚═╝  ╚═╝   ╚═╝      ╚═╝   ╚══════╝╚══════╝╚══════╝╚═╝  ╚═╝╚═╝╚═╝     ╚══════╝
"""


player_board = """
           ┌───────────────────────────────────────────────────────────────────────┐
           │         1   2   3   4   5   6   7   8                                 │
           │       ┌───┬───┬───┬───┬───┬───┬───┬───┐       ┌───────────────┐       │
           │     A │ ~ │ ~ │ ~ │ ~ │ ~ │ ~ │ ~ │ ~ │       │Hull Integrity:│       │
           │       ├───┼───┼───┼───┼───┼───┼───┼───┤       ├───────────────┘──┐    │
           │     B │ ~ │ ~ │ ~ │ ~ │ ~ │ ~ │ ~ │ ~ │       │ Cruiser      XX  │    │
           │       ├───┼───┼───┼───┼───┼───┼───┼───┤       │ Destroyer    XX  │    │
           │     C │ ~ │ ~ │ ~ │ ~ │ ~ │ ~ │ ~ │ ~ │       │ Battleship   XX  │    │
           │       ├───┼───┼───┼───┼───┼───┼───┼───┤       └──────────────────┘    │
 PLAYER:   │     D │ ~ │ ~ │ ~ │ ~ │ ~ │ ~ │ ~ │ ~ │                               │
           │       ├───┼───┼───┼───┼───┼───┼───┼───┤                               │
           │     E | ~ │ ~ │ ~ │ ~ │ ~ │ ~ │ ~ │ ~ │                               │
           │       ├───┼───┼───┼───┼───┼───┼───┼───┤                               │
           │     F │ ~ │ ~ │ ~ │ ~ │ ~ │ ~ │ ~ │ ~ │                               │
           │       ├───┼───┼───┼───┼───┼───┼───┼───┤                               │
           │     G │ ~ │ ~ │ ~ │ ~ │ ~ │ ~ │ ~ │ ~ │                               │
           │       ├───┼───┼───┼───┼───┼───┼───┼───┤                               │
           │     H │ ~ │ ~ │ ~ │ ~ │ ~ │ ~ │ ~ │ ~ │                               │
           │       └───┴───┴───┴───┴───┴───┴───┴───┘                               │
           └───────────────────────────────────────────────────────────────────────┘
"""



computer_board = """
           ┌───────────────────────────────────────────────────────────────────────┐
           │                                     1   2   3   4   5   6   7   8     │
           │                                   ┌───┬───┬───┬───┬───┬───┬───┬───┐   │
           │                                 A │ ~ │ ~ │ ~ │ ~ │ ~ │ ~ │ ~ │ ~ │   │
           │                                   ├───┼───┼───┼───┼───┼───┼───┼───┤   │
           │                                 B │ ~ │ ~ │ ~ │ ~ │ ~ │ ~ │ ~ │ ~ │   │
           │                                   ├───┼───┼───┼───┼───┼───┼───┼───┤   │
           │                                 C │ ~ │ ~ │ ~ │ ~ │ ~ │ ~ │ ~ │ ~ │   │
           │                                   ├───┼───┼───┼───┼───┼───┼───┼───┤   │
 COMPUTER: │                                 D │ ~ │ ~ │ ~ │ ~ │ ~ │ ~ │ ~ │ ~ │   │
           │                                   ├───┼───┼───┼───┼───┼───┼───┼───┤   │
           │     ┌───────────────┐           E | ~ │ ~ │ ~ │ ~ │ ~ │ ~ │ ~ │ ~ │   │
           │     │Hull Integrity:│             ├───┼───┼───┼───┼───┼───┼───┼───┤   │ 
           │     ├───────────────┘──┐        F │ ~ │ ~ │ ~ │ ~ │ ~ │ ~ │ ~ │ ~ │   │
           │     │ Cruiser      XX  │          ├───┼───┼───┼───┼───┼───┼───┼───┤   │
           │     │ Destroyer    XX  │        G │ ~ │ ~ │ ~ │ ~ │ ~ │ ~ │ ~ │ ~ │   │
           │     │ Battleship   XX  │          ├───┼───┼───┼───┼───┼───┼───┼───┤   │
           │     └──────────────────┘        H │ ~ │ ~ │ ~ │ ~ │ ~ │ ~ │ ~ │ ~ │   │
           │                                   └───┴───┴───┴───┴───┴───┴───┴───┘   │
           └───────────────────────────────────────────────────────────────────────┘
"""

instruct_text = """
Game Instructions go here
"""