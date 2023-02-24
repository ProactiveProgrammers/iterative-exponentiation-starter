"""Define the command-line interface for the iterator program."""

import typer

from iterator import display
from iterator import iterate

# create a Typer object to support the command-line interface
cli = typer.Typer()

# TODO: Read all of the source code inside of this file
# and make sure that you understand it and how it uses
# the Python source code provided in other files

# TODO: Make sure that your program works when the specified
# minimum value is not zero! For instance, the program should
# work correctly when the minimum value is 2 and the maximum
# value is 10. This would mean that the program startx to compute
# the value of 2**2 and then stops after computing 2**9.
#
# Here is an example for these specific inputs:
#
# 2**2 = 4
# 2**3 = 8
# 2**4 = 16
# 2**5 = 32
# 2**6 = 64
# 2**7 = 128
# 2**8 = 256
# 2**9 = 512


@cli.command()
def main(
    forloop: bool = typer.Option(False, "--forloop"),
    whileloop: bool = typer.Option(False, "--whileloop"),
    minimum: int = typer.Option(1, min=0, max=100),
    maximum: int = typer.Option(5, min=0, max=100),
):
    """Calculate the powers of 2 from 0 to 20 using iteration constructs."""
    # display the debugging output for the program's command-line arguments
    typer.echo(
        f"Calculating the powers of 2 from {minimum} to {maximum} with iteration:"
    )
    typer.echo("")
    typer.echo(f"  Should I use a for loop? {display.convert_bool_to_answer(forloop)}")
    typer.echo(
        f"  Should I use a while loop? {display.convert_bool_to_answer(whileloop)}"
    )
    typer.echo("")
    # compute the powers of 2 using a function in the iterate module that uses a for loop
    if forloop is True:
        typer.echo("  Here is the output with the for loop.")
        typer.echo("")
        forloop_list = iterate.calculate_powers_of_two_for_loop(minimum, maximum)
        display.display_list(forloop_list, "   ")
        typer.echo("")
    # compute the powers of 2 using a function in the iterate module that uses a while loop
    if whileloop is True:
        typer.echo("  Here is the output with the while loop.")
        typer.echo("")
        whileloop_list = iterate.calculate_powers_of_two_while_loop(minimum, maximum)
        display.display_list(whileloop_list, "   ")
        typer.echo("")
    # display a final message and some extra spacing
    typer.echo("Wow, all of that iteration was exhausting! 😂")
    typer.echo("")
