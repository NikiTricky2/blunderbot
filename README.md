# Blunderbot
You know how chess bots nowadays are too overpowered? Blunderbot allows you to experience that power over these machines again. 
1. Download *any* chess engine
2. Set the path of the engine in `PATH_TO_ENGINE`
3. Start the program
4. Enjoy!

Curious on how this bot plays? Check out [this chess.com article](https://www.chess.com/blog/NikiTricky2/blunderbot-the-reverse-chess-bot).

## How to use blunderbot
After you've set the engine path and run the program, you will be asked what color should blunderbot play. When it's that color's turn blunderbot will calculate the worst possible move and present it to you. Moves are in the notation `start position` `end position` meaning that a pawn on e3 moving to e4 is the move `e3e4` If you play an invalid move, the program will alert you and prompt again. In the case that the move is actually valid, you can check with the providied FEN code.

## Advanced usage

### Undoing moves
When you've made a mistake, on the next move prompt, write `undo` and the board will be restored to its previous state.

### Time control
Move calculations taking too long? In the first couple lines of code you'll see some variables that you can change (with descriptions ofc). Make sure that all variables except one are set to `None`, otherwise it could cause undesirable results.

### Rendering
FEN code troubleshooting isn't for you? Render the board every turn with setting the `RENDER_BOARD` variable to the path of the board.

## Contributing
There is an error in blunderbot you know how to fix? You want to add more functionality? Submit a pull request (or more undesirably, an issue) and i'll respond in adequate time.
