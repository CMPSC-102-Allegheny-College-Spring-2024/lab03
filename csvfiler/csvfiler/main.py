#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# run command: 
# poetry run csvfiler --name myname --ghhandle myHandle --favfilm myfilm --favsong mysong --favfood myFood

import csv
from rich.console import Console
import typer

def write_to_csv(file_path:str, user_info: str) -> None:
    """ Function to write the tuple to csv. """
    with open(file_path, mode='a', newline='') as file:
        writer = csv.writer(file)
        # print(f" {user_info} : {type(user_info)}")
        writer.writerow(user_info)
# end of write_to_csv()

# create a Typer object to support the command-line interface

# TODO: Create a Typer instance and assign it to the variable cli

# TODO: Define a command named 'main' with optional parameters for `name`, `ghhandle`, `favfilm`, `favsong`, and `favfood`

@cli.command()


    # TODO: Create a Console instance and assign it to the variable console

    # TODO: Print a message with the provided name using emoji sparkles

    # TODO: Print a message with the provided GitHub handle using emoji sparkles

    # TODO: Print a message with the provided favorite film using emoji sparkles

    # TODO: Print a message with the provided favorite song using emoji sparkles

    # TODO: Print a message with the provided favorite food using emoji sparkles

    file_path = 'user_data.csv' # file in which we save data

    # TODO: Create a tuple called user_info containing the collected variables from the command line.

    # TODO: Pass the variables `file_path` and `user_info` to `write_to_csv()` to create a csv file

# end of main()
