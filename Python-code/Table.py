# pip install prettytable

from prettytable import PrettyTable
myTable = PrettyTable(["Student Name", "Class", "Section", "Percentage"])
myTable.add_row(["Andrew", "X", "B", "91.2%"])
myTable.add_row(["Jay", "X", "C", "63.5%"])
myTable.add_row(["Harry", "X", "A", "90.23%"])
myTable.add_row(["Bernadette", "X", "D", "92.7%"])
myTable.add_row(["Shai", "X", "A", "98.2%"])
myTable.add_row(["Raj", "X", "B", "88.1%"])
myTable.add_row(["Amy", "X", "B", "95.0%"])
print(myTable)
