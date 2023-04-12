

#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <math.h>
#include <time.h>

int generateRand(int low, int high);
int exponent(int n);
void printBoxes(int a, int b, int c);
void dots_loading();
int updateBox(int box, int token);
int calculateStars(int box, int token);
int checkWin(int difficulty, int a, int b, int c, int target);

int main()
{

    int exit = 0;

    while (exit != 1)
    {
        // declare variables
        int difficulty;
        int tokensConsumed = 0;
        int tokensLeft = -1;
        int stars = 0;
        int again = 0;
        int rookieOption = 0;

        // trash
        char trash;

        // game variables
        int a, b, c, target, token;
        int x;

        printf("\n\n\t-----------------------------------------------------------------------------------------------------------------------\n");
        printf("\t|                                                                                                                     |\n");
        printf("\t|                                          Hello, Player! Welcome to Merge2Win.                                       |\n");
        printf("\t|                                                                                                                     |\n");
        printf("\t|                                                                                                                     |\n");
        printf("\t|       Merge2win is a game that trains our brain to calculate in terms of powers of 2. Because 2 is the base         |\n");
        printf("\t|       ofthe binary number system, it is common to use the powers of 2 in computer science. This game requires       |\n");
        printf("\t|       us to quickly and mentally manipulate numbers thatare powers of 2, at the same time, strategize to win        |\n");
        printf("\t|       the game with the most stars.                                                                                 |\n");
        printf("\t|                                                                                                                     |\n");
        sleep(2);
        printf("\t|                                                       Let's START!                                                  |\n");
        printf("\t|                                                                                                                     |\n");
        printf("\t|                                                                                                                     |\n");
        printf("\t=======================================================================================================================\n\n");

        sleep(2);

        printf("                                                                 Loading  ");
        sleep(2);
        printf(". ");
        sleep(1);
        printf(". ");
        sleep(1);
        printf(". ");
        sleep(1);
        printf(".\n\n\n");
        sleep(1);
        printf("                                                Press any key to start the game.  ");
        getchar();

        // set how many tokens can be consumed based on difficulty
        while (tokensLeft < 0)
        {
            // select difficulty
            printf("\n========================================================================\n");
            printf("\nPick a difficulty...\n\n");
            printf("[1] Rookie\n");
            printf("[2] Skilled\n");
            printf("[3] Expert\n\n");
            printf(": ");
            // if not an integer
            difficulty = 0;
            if (scanf("%d", &difficulty) == 0)
            {
                scanf("%c", &trash);
            }

            // set tokensLeft
            switch (difficulty)
            {
            case 1: // rookie
                // infinity = 2147483647 = maximum possible int
                tokensLeft = 2147483647;
                break;
            case 2: // skilled
                tokensLeft = 20;
                break;
            case 3: // expert
                tokensLeft = 10;
                break;
            default: // input is an int that is not 1, 2, or 3
                printf("\n========================================================================\n");
                printf("\nInvalid input. Please try again.\n");
                fflush(stdin);
                break;
            }
        }

        // generate initial values
        x = generateRand(8, 12);
        target = exponent(x);             // 2^x, 8 <= n <= 12
        a = exponent(generateRand(1, x)); // 2^m <= 2^x
        b = exponent(generateRand(1, x)); // 2^m <= 2^x
        c = exponent(generateRand(1, x)); // 2^m <= 2^x

        // game loop
        int gameover = 0; // 1 if win, -1 if lose
        int valid = 1;
        while (gameover == 0)
        {
            printf("\n========================================================================");

            char box;

            if (valid == 1)
            {
                // generate new value for token
                int z = generateRand(1, 12);
                token = pow(2, z); // 2^m <= 2^x
            }
            else
            {
            }

            // print tokensLeft
            if (tokensLeft > 20) // rookie
            {

                printf("\n|                                                                      \n");
                printf("|  Tokens: Unlimited                                                   \n");
                printf("|  Tokens Consumed: %d                                                  ", tokensConsumed);
                printf("\n|                                                                      ");
                printf("\n|                                                                      \n");
            }
            else
            {

                printf("\n|  Tokens Left: %d                                                      \n", tokensLeft);
                printf("|  Tokens Consumed: %d                                                  \n", tokensConsumed);
                printf("|                                                                      \n");
                printf("|                                                                      \n");
            }

            // print boxes
            printBoxes(a, b, c);

            // print stars
            printf("|  Stars: %d                                                            \n", stars);

            // print target
            printf("|  Target: %d                                                         \n", target);

            // print token
            printf("|  Token: %d                                                            ", token);
            printf("\n|                                                                      ");

            // pick box
            printf("\n|  Pick a box: ");
            scanf(" %c", &box);

            switch (box)
            {
            case 'a':
            case 'A':
                // pBox = a;
                stars += calculateStars(a, token);
                a = updateBox(a, token);
                valid = 1;
                break;
            case 'b':
            case 'B':
                stars += calculateStars(b, token);
                b = updateBox(b, token);
                valid = 1;
                break;
            case 'c':
            case 'C':
                stars += calculateStars(c, token);
                c = updateBox(c, token);
                valid = 1;
                break;
            default:
                printf("========================================================================\n");
                printf("\nInvalid input. Please try again.\n\n");
                valid = 0;
            }

            // make sure stars do not go below 0
            if (stars < 0)
            {
                stars = 0;
            }

            // subtract a token if input is valid
            if (valid == 1)
            {
                tokensLeft--;
                tokensConsumed++;
            }

            // check if player has won
            gameover = checkWin(difficulty, a, b, c, target);

            // check if player still has tokens left and have not won the game
            if (tokensLeft < 1 && gameover != 1)
            {
                gameover = -1;
            }

            if (difficulty == 1 && tokensConsumed != 0 && tokensConsumed % 51 == 0)
            {
                // play again?
                while (!(rookieOption == 1 || rookieOption == 2 || rookieOption == 3))
                {
                    printf("===================================================================\n");
                    printf("|                                                                 |\n");
                    printf("|                             WARNING!                            |\n");
                    printf("|                                                                 |\n");
                    printf("| You have already consumed 50 tokens, what would you like to do: |\n");
                    printf("|                                                                 |\n");
                    printf("|                                                                 |\n");
                    printf("===================================================================\n\n");
                    printf("[1] Restart\n");
                    printf("[2] Continue\n");
                    printf("[3] Quit\n");
                    printf(": ");

                    if (scanf("%d", &rookieOption) == 0)
                    {
                        scanf("%c", &trash);
                    }
                    printf("========================================================================\n\n");

                    if (rookieOption == 1)
                    {
                        exit = 0;
                        gameover = -1;
                    }
                    else if (rookieOption == 2)
                    {
                        // pass
                    }
                    else if (rookieOption == 3)
                    {
                        exit = 1;
                        gameover = -1;
                    }
                    else
                    {
                        printf("Invalid input. Please try again.\n");
                    }
                }
                rookieOption = 4;
            }
            printf("========================================================================\n\n");
        }

        if (gameover == 1) // means win
        {
            // add bonus stars
            if (tokensConsumed <= 10)
            {
                printf("Great work! You have received 10 bonus stars!\n\n");
                printf("========================================================================\n\n");
                stars += 10;
            }
            else if (tokensConsumed > 10 && tokensConsumed < 20)
            {
                printf("Nice one! You have received 5 bonus stars!\n\n");
                printf("========================================================================\n\n");
                stars += 5;
            }
            printf("========================================================================\n\n");
            printf("Congratulations player! You WON with only %d TOKENS consumed!\n\n", tokensConsumed);
            printf("Here is the total number of STAR(S) accumulated: %d\n\n", stars);
            printf("========================================================================\n\n");
        }
        else if (gameover == -1) // means lose
        {
            printf("Nice try, player! You LOST!\n\n");
            printf("========================================================================\n\n");
        }

        if (!(rookieOption > 0))
        {
            // asks the user if play again after consuming 20 tokens for SKILLED && 10 tokens for EXPERT
            while (!(again == 1 || again == 2))
            {
                printf("Would you like to play again?\n");
                printf("[1] Yes\n");
                printf("[2] No\n");
                printf(": ");
                if (scanf("%d", &again) == 0)
                {
                    scanf("%c", &trash);
                }
                printf("\n========================================================================\n\n");

                if (again == 1)
                {
                    exit = 0;
                }
                else if (again == 2)
                {
                    printf("Thank you for playing Merge2win!\n\n");
                    printf("========================================================================\n\n");
                    exit = 1;
                }
                else
                {
                    printf("Invalid input. Please try again.\n");
                    printf("\n========================================================================\n\n");
                }
            }
        }

        getchar();
    }
    return 0; // end
}

/*
    This function generates a random integer with the range of low to high, inclusive.
    Precondition: low and high are positive integers.
    @param low is the lowest value that can be generated, the generated int is greater
    than or equal to low
    @param high is the highest value that can be generated, the generated int is less
    than or equal to high
    @return the randomly generated integer
*/
int generateRand(int low, int high)
{
    int randomInt = rand();

    int r = (randomInt % high - low) + low; // range of [low, high]

    if (r < low)
    {
        r = low;
    }

    return r;
}

/*
    This function solves for the power of 2 given an exponent.
    Precondition: n is a positive integer.
    @param n is the power to be applied to 2
    @return the nth power of 2
*/
int exponent(int n)
{
    int result = 2;
    for (int i = 0; i < n; i++)
    {
        result *= 2;
    }
    return result;
}

/*
    This function prints the values in the boxes: a, b, and c.
    Precondition: None.
    @param a is the value for the box a
    @param b is the value for the box b
    @param c is the value for the box c
    @return void
*/
void printBoxes(int a, int b, int c)
{
    printf("|       =\tA\t=\tB\t=\tC\t=\t       \n");
    printf("|       |\t%d\t|\t%d\t|\t%d\t|              \n", a, b, c);
    printf("|       =\t=\t=\t=\t=\t=\t=              ");
    printf("\n|                                                                      ");
    printf("\n|                                                                      \n");
}

/*
    This function applies the game logic given the value of the box and the token.
    Precondition: None
    @param box is the value of the box to be compared to token
    @param token is the value of the token
    @return updated value of the box
*/
int updateBox(int box, int token)
{
    // game logic
    if (token < box)
    {
        box = token; // box becomes token
    }
    else if (token > box)
    {
        box = token / box; // box becomes token / box
    }
    else if (token == box)
    {
        box = box + box; // box becomes box + box
    }

    return box;
}

/*
    This function calculates whether the stars should be incremented or decremented.
    @param box is the value of the box chosen
    @param token is the value of the token
    @return 1 or -1, 1 if it is to be incremented and -1 if decremented
*/
int calculateStars(int box, int token)
{
    int star = 0;
    if (token == box)
    {
        star = 1;
    }
    else
    {
        star = -1;
    }
    return star;
}

/*
    This function checks whether the player has already achieved the winning condition.
    @param difficulty is the difficulty mode of the player, win conditions vary
    based on difficulty
    @param a is the value for the box a
    @param b is the value for the box b
    @param c is the value for the box c
    @param target is the value of the target
    @return 1 or 0, 1 if the winning condition have been achieved and 0 otherwise
*/
int checkWin(int difficulty, int a, int b, int c, int target)
{
    int win = 0; // assume that board has not won
    int matchedBoxes = 0;

    if (a == target)
        matchedBoxes++;
    if (b == target)
        matchedBoxes++;
    if (c == target)
        matchedBoxes++;

    switch (difficulty)
    {
    case 1: // if rookie
        // check if atleast one box is equal to target
        if (matchedBoxes > 0)
            win = 1;
        break;
    case 2: // if skilled
        // check if atleast two boxes are equal to target
        if (matchedBoxes > 1)
            win = 1;
        break;
    case 3:
        // check if all boxes are equal to target
        if (matchedBoxes > 2)
            win = 1;
        break;
    }

    return win;
}
