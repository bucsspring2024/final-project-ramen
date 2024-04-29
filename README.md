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
|  1                   | Click Run            |                                   |
|  2                   | Game Starts          |                                   |


Test 2: Verify shield moves in the direction of the arrow keys 
| Step                 |Procedure             |Expected Results                   |
|----------------------|:--------------------:|----------------------------------:|
|  1                   | Start game           |                                   |
|  2                   | Press Left arrow key |                                   |
|  3                   |Verify shield moves Left|                                 |
|  4                   | Press Up arrow key   |                                   |
|  5                   |Verify shield moves Up|                                   |
|  6                   | Press Right arrow key|                                   |
|  7                   |Verify shield moves Right|                                |
|  8                   | Press Down arrow key |                                   |
|  9                   |Verify shield moves Down|                                 |

Test 3: Collision; Arrow hits shield 
| Step                 |Procedure             |Expected Results                   |
|----------------------|:--------------------:|----------------------------------:|
|  1                   |Game starts           |                                   |
|  2                   |Arrow moves towards hero|                                 |
|  3                   |Verify arrow collides with shield|                        |

Test 4: Collision; Arrow hits hero
| Step                 |Procedure             |Expected Results                   |
|----------------------|:--------------------:|----------------------------------:|
|  1                   |Game starts           |                                   |
|  2                   |Arrow moves towards hero|                                 |
|  3                   |Verify arrow collides with player|                        |

Test 5: Next Level Counter
| Step                 |Procedure             |Expected Results                   |
|----------------------|:--------------------:|----------------------------------:|
|  1                   | Level icon pops up on screen |                           |
|  2                   |After # of arrows, increase level counter by 1|           |

Test 6: Music runs
| Step                 |Procedure             |Expected Results                   |
|----------------------|:--------------------:|----------------------------------:|
|  1                   | Game Starts          |                                   |
|  2                   | Music Plays          |                                   |

Test 7: Music Ends
| Step                 |Procedure             |Expected Results                   |
|----------------------|:--------------------:|----------------------------------:|
|  1                   | Game Starts          |                                   |
|  2                   | Music Plays          |                                   |
|  3                   | Game Over Screen     |                                   |
|  4                   | Music Stops          |                                   |


