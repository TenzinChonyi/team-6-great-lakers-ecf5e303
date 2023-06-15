*** Settings ***
Documentation     
...             I want to move my character. If they attempt to move past a boundary, the move results in no change in position.
...             This contains our spec by example table, that we created our ATDD cases out of.
...             https://drive.google.com/file/d/16QioQL1jWsGwbEui_Tw08fOoxV5NAdrB/view?ts=648b4442&pli=1


Test Template     Move character
Library           MoveLibrary.py

*** Test Cases ***                  StartingX     StartingY     StartingMoveCount     Direction     EndingX     EndingY     EndingMoveCount
Start top left bounce off NORTH         0          9            3                       NORTH       0           9           4
Start top left bounce off WEST          0          9            7                       WEST        0           9           8
start top right bounce off EAST         9          9            11                      EAST        9           9           12
start bottom left bounce off SOUTH      0          0            24                      SOUTH       0           0           25
Move north in bound                     5          5            33                      NORTH       5           6           34
Move south in bound                     5          5            23                      SOUTH       5           4           24
Move west in bound                      5          5            37                      WEST        4           5           38
Move east in bound                      5          5            90                      EAST        6           5           91

*** Keywords ***
Move character
    [Arguments]    ${startingX}    ${startingY}    ${startingMoveCount}    ${direction}    ${endingX}    ${endingY}    ${endingMoveCount}
    Initialize character xposition with  ${startingX}
    Initialize character yposition with  ${startingY}
    Initialize character moveCount with  ${startingMoveCount}
    Move in direction                    ${direction}
    Character xposition should be        ${endingX}
    Character yposition should be        ${endingY}
    Character moveCount should be        ${endingMoveCount}