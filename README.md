[![Open in Visual Studio Code](https://classroom.github.com/assets/open-in-vscode-718a45dd9cf7e7f842a935f5ebbe5719a5e09af4491e668f4dbf3b35d5cca122.svg)](https://classroom.github.com/online_ide?assignment_repo_id=14753976&assignment_repo_type=AssignmentRepo)

:warning: Everything between << >> needs to be replaced (remove << >> after replacing)

# Ramen
## CS110 Final Project  Spring, 2024 

## Team Members

Tasnimul Fahim, Andy Huang

***

## Project Description

You are an airbender who is getting attacked by arrows. However, you have your glider to defend you from these arrows. The question is how long can you last?

***    

## GUI Design

### Initial Design

![initial gui](assets/gui.jpg)

### Final Design

![final gui](assets/finalgui.jpg)

## Program Design

### Features

1. Level Counter
2. Moveable Sprite
3. Collisions
4. Music
5. Game Over Screen

### Classes

- << You should have a list of each of your classes with a description >>

## ATP
Test 1: Games opens up 
| Step                 |Procedure             |Expected Results                   |
|----------------------|:--------------------:|----------------------------------:|
|  1                   | Click Run            |Game Autostarts as it should       |
|  2                   | Game Starts          |                                   |


Test 2: Verify shield moves in the direction of the arrow keys 
| Step                 |Procedure             |Expected Results                   |
|----------------------|:--------------------:|----------------------------------:|
|  1                   | Start game           |      Player moves in the          |
|  2                   | Press Left arrow key |      direction in respect to      |
|  3                   |Verify shield moves Left|    the directional arrow        |
|  4                   | Press Up arrow key   |      key pressed.                 |
|  5                   |Verify shield moves Up|                                   |
|  6                   | Press Right arrow key|                                   |
|  7                   |Verify shield moves Right|                                |
|  8                   | Press Down arrow key |                                   |
|  9                   |Verify shield moves Down|                                 |

Test 3: Collision; Arrow hits shield 
| Step                 |Procedure             |Expected Results                  |
|----------------------|:--------------------:|--------------------------------- |
|  1         |Game starts                        |    Arrow Sprite should        |                        
|  2         |Arrow moves towards hero           |  dissapear. "Hero" should     |                            
|  3         |Verify arrow collides with shield  | be alive and game continues   |
                        
Test 4: Collision; Arrow hits hero
| Step     |Procedure                        |Expected Results                |
|----------|:--------------------:           |--------------------------------|
|  1       |Game starts                      | Controller movement ends.      |
|  2       |Arrow moves towards hero         | Game Over Text Appears.        |
|  3       |Verify arrow collides with player|                                |

Test 5: Next Level Counter
| Step  |Procedure                                         |Expected Results      |
|-------|:------------------------------------------------:|----------------------|
|  1    | Level icon pops up on screen                     | Level number will    |
|  2    |After waves of arrows, increase level counter by 1| visibly change. More |
|  3    |Verify amount of arrows increase                  | arrows will appear.  |
Test 6: Music runs
| Step                 |Procedure             |Expected Results                   |
|----------------------|:--------------------:|----------------------------------:|
|  1                   | Game Starts          |  Music should be playing,         |
|  2                   | Music Plays          |  once game starts.                |

Test 7: Level Mastery
| Step                 |Procedure                  |Expected Results                   |
|----------------------|:-------------------------:|----------------------------------:|
|  1                   | Game Starts               |      "You are A Hero"             |
|  2                   | Survive Levels 1-4        |       text appears.               |
|  3                   | Verify Level 4 is finished|                                   |
|  4                   | Wait for message to appear|                                   |


