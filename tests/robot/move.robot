*** Settings ***
Documentation     I want to move my character. If they attempt to move past a boundary, the move results in no change in position.
Test Template     Move character
Library           MoveLibrary.py

*** Test Cases ***                  StartingX     StartingY     StartingMoveCount     Direction     EndingX     EndingY     EndingMoveCount
Move in the middle of the board     0             0             1                     NORTH         0           1           2
Move on the edge of the board       0             0             5                     SOUTH         0           0           6
Start top left bounce off NORTH     0               9           3                       NORTH       0           9           4
Start top left bounce off WEST      0               9           7                       WEST        0           9           8
start top right bounce off EAST     9               9           11                      EAST        9           9           12
start bottom left bounce off SOUTH  0               0           24                      SOUTH       0           0           25



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