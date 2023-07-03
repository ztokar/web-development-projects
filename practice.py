from prettytable import PrettyTable

table=PrettyTable()
table.add_column("Pokemonname",["Pikachu","CHarmander"])
table.add_column("Type",["Fire","Water"])

table.align="r"

print(table)
