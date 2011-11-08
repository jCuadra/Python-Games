## Attempt at Mad Lib Program
## Liam Boyle


## Mainline Program
quit = "n"
##Inputting the words
while quit != "y":
    prompt = "Please enter the name of a color:\n"
    wordA = input(prompt)
    prompt = "Please enter a noun:\n"
    wordB = input(prompt)
    prompt = "Please enter a number:\n"
    wordC = input(prompt)
    prompt = "Please enter another noun:\n"
    wordD = input(prompt)
    wordE = input(prompt)
    prompt = "Please enter an adjective:\n"
    wordF = input(prompt)
    prompt = "Please enter a place:\n"
    wordG = input(prompt)
    print ("\n", "\n", "\n", "Baa Baa ", wordA, " sheep,\n",
        "Have you any ", wordB, "?\n", "Yes sir, yes sir,\n",
        wordC, " bags full;\n", "One for the ", wordD, "\n",
        "And one the the ", wordE, "\n", "And one for the ", wordF,
        " boy\n", "Who lives down the ", wordG, ".\n")
    ## mainline finished, continue question
    prompt = "Do you wish to quit y/n?\n"
    quit = input(prompt)

## End program