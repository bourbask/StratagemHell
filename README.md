# Stratagem Hell

Stratagem Hell is a simple Pygame-based game where players must input a series of button combinations within a certain time limit. The game is inspired by the Helldivers 2 video game.

## How it works

The game starts with a main menu inviting the player to start the game or quit. Once the game starts, a random combo is presented on the screen, along with a timer. The player must input the correct sequence of keys corresponding to the combo before the timer runs out. The keys used in the game are "z" (UP), "q" (LEFT), "s" (DOWN), and "d" (RIGHT). As the player progresses, the combos become more challenging and the time limit decreases. If the player inputs the correct combo within the time limit, they advance to the next level. If they fail to do so, the game ends and they have the option to retry, quit, or return to the main menu.

## Requirements

Install requirements with the following command :

```shell
pip install -r requirements.txt
```

## How to play

1. Clone the repository or download the source code files.
2. Make sure you have Python, Pygame, Dotenv installed on your system.
3. Run the game by executing the `main.py` file.
4. Follow the on-screen instructions to navigate the main menu, start the game, and input the combos.
5. Have fun challenging yourself with increasingly difficult combos!

## Combos

### Patriotic Administration Center

1. Machine Gun: Down, Left, Down, Up, Right
2. Anti-Material Rifle: Down, Left, Right, Up, Down
3. Stalwart: Down, Left, Down, Up, Up, Left
4. Expendable Anti-Tank: Down, Down, Left, Up, Right
5. Recoiled Rifle: Down, Left, Right, Right, Left
6. Flamethrower: Down, Left, Up, Down, Up
7. Autocannon: Down, Left, Down, Up, Up, Right
8. Railgun: Down, Right, Left, Down, Up, Left, Right
9. Spear: Down, Down, Up, Down, Down

### Orbital Cannons

1. Orbital Gatling Barrage: Right, Down, Left, Up, Up
2. Orbital Airburst Strike: Right, Right, Right
3. Orbital 120MM HE Barrage: Right, Down, Left, Right, Down
4. Orbital 380MM HE Barrage: Right, Down, Up, Up, Left, Down, Down
5. Orbital Walking Barrage: Right, Right, Down, Left, Right, Down
6. Orbital Lasers: Right, Down, Up, Right, Down
7. Orbital Railcannon Strike: Right, Up, Down, Down, Right

### Hangar

1. Eagle Strafing Run: Up, Right, Right
2. Eagle Airstrike: Up, Right, Down, Right
3. Eagle Cluster Bomb: Up, Right, Down, Down, Right
4. Eagle Napalm Airstrike: Up, Right, Down, Up
5. Jump Pack: Down, Up, Up, Down, Up
6. Eagle Smoke Strike: Up, Right, Up, Down
7. Eagle 110MM Rocket Pods: Up, Right, Up, Left
8. Eagle 500KG Bomb: Up, Right, Down, Down, Down

### Bridge

1. Orbital Precision Strike: Right, Right, Up
2. Orbital Gas Strike: Right, Right, Down, Right
3. Orbital EMS Strike: Right, Right, Left, Down
4. Orbital Smoke Strike: Right, Right, Down, Up
5. HMG Emplacement: Down, Up, Left, Right, Right, Left
6. Shield Generation Relay: Down, Up, Left, Down, Right, Right
7. Tesla Tower: Down, Up, Right, Up, Left, Right

### Engineering Bay

1. Anti-Personnel Minefield: Down, Left, Up, Right
2. Supply Pack: Down, Left, Down, Up, Up, Down
3. Grenade Launcher: Down, Left, Up, Left, Down
4. Laser Cannon: Down, Left, Down, Up, Left
5. Incendiary Mines: Down, Left, Left, Down
6. "Guard Dog" Rover: Down, Up, Left, Up, Right, Right
7. Ballistic Shield Backpack: Down, Left, Up, Up, Right
8. Arc thrower: Down, Right, Up, Left, Down
9. Shield Generator Pack: Down, Up, Left, Right, Left, Right

### Robotic Workshop

1. Machine Gun Sentry: Down, Up, Right, Right, Up
2. Gatling Sentry: Down, Up, Right, Left
3. Mortar Sentry: Down, Up, Right, Right, Down
4. "Guard Dog": Down, Up, Left, Up, Right, Down
5. Autocannon Sentry: Down, Up, Right, Up, Left, Up
6. Rocket Sentry: Down, Up, Right, Right, Left
7. EMS Mortar Sentry: Down, Down, Up, Up, Left
