[![Open in Visual Studio Code](https://classroom.github.com/assets/open-in-vscode-718a45dd9cf7e7f842a935f5ebbe5719a5e09af4491e668f4dbf3b35d5cca122.svg)](https://classroom.github.com/online_ide?assignment_repo_id=14753976&assignment_repo_type=AssignmentRepo)

:warning: Everything between << >> needs to be replaced (remove << >> after replacing)

# Ramen Hero
## CS110 Final Project  Spring, 2024 

## Team Members

Tasnimul Fahim, Andy Huang

***

## Project Description

You are a hero who is getting attacked by arrows. However, you have your slithering companion to defend you from these arrows. The question is how long can you last as the speed of the arrows increase?

***    

## GUI Design

### Initial Design

![initial gui](assets/backround.jpg)

### Final Design

![final gui](assets/finalgui.png)

## Program Design

### Features

1. Level Counter
2. Moveable Sprite
3. Collisions
4. Music
5. Arrow Counter

### Classes

airbend.py class is the class that holds the shield
arrow.py class is the class that holds all the enemy arrows
controller.py allows sprites to move and controls game logic
hero.py is the class that holds the heart sprite
music.py holds the music files

## ATP
Test 1: Games opens up 
| Step                 |Procedure             |Expected Results                   |
|----------------------|:--------------------:|----------------------------------:|
|  1                   | Click Run            |Game Autostarts as it should       |
|  2                   | Game Starts          |                                   |


Test 2: Verify shield moves in the direction of the arrow keys 
| Step                 |Procedure             |Expected Results                   |
|----------------------|:--------------------:|----------------------------------:|
|  1                   | Start game           |    Program starts                 |
|  2                   | Press Left arrow key |   snake.rect.x changes by -50     |
|  3                   |Verify shield moves Left|  Visually, the shield moves left|
|  4                   | Press Up arrow key   |   snake.rect.y changes by -50     |
|  5                   |Verify shield moves Up|   Visually, the shield moves up   |
|  6                   | Press Right arrow key|   snake.rect.x changes by 50      |
|  7                   |Verify shield moves Right| Visually, the shield moves right|
|  8                   | Press Down arrow key |   snake.rect.y changes by 50      |
|  9                   |Verify shield moves Down| Visually, the shield moves down |

Test 3: Collision; Arrow hits shield 
| Step                 |Procedure             |Expected Results                  |
|----------------------|:--------------------:|--------------------------------- |
|  1         |Game starts                        |program runs             |                        
|  2         |Arrow moves towards hero           |arrow position is changing to reflect movement|                        
|  3         |Verify arrow collides with shield  | if arrow collides then arrowcounter -1 and arrow disappears |                  

Test 4: Next Level Counter
| Step  |Procedure                                         |Expected Results      |
|-------|:------------------------------------------------:|----------------------|
|  1    |Level icon pops up on screen                     | Level text appears at bottom of screen    |
|  2    |Increase level counter by 1|checks number of collisions and reassigns level value based on amount of collisions|
|  3    |Verify speed of arrows increase                  | speed reflects next level speed  |

Test 5: Music runs
| Step                 |Procedure             |Expected Results                   |
|----------------------|:--------------------:|----------------------------------:|
|  1                   | Game Starts          |                                   |
|  2                   | Music Plays          |  music.startmusic() runs music.py |

Test 6: Arrow Counter (amount of arrows left per stage)
| Step                 |Procedure                  |Expected Results                   |
|----------------------|:-------------------------:|----------------------------------:|
|  1                   | Game Starts               |                                   |
|  2                   | 4 arrows spawns           |  numArrows increments by 4        |
|  3                   | Shield blocks Arrow       |numArrows decrements by 1, arrow is removed from group  |
|  4                   | Verify change in Arrow counter    | text display is updated           |

Glitches
|  Sometimes the arrows don't collide with the heart |
