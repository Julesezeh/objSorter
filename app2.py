col = "c119"
row = "r256"

def formatColRows (row,col):
    new_column = f"col_{col[1:]}"
    new_row = f"row_{row[1:]}"
    print(f"{new_row}{new_column}")


formatColRows(row,col)