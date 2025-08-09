# datareader.py

def read_csv(filename="data.csv"):
    """
    Reads the CSV file and returns the data as a list of lists.
    Each inner list represents a row.
    """
    # Open the file and read all lines.
    with open(filename, "r") as file:
        lines = file.readlines()

    # Split each line by commas and remove any extra whitespace.
    data = []
    for line in lines:
        # Remove spaces and the newline at the end
        line = line.strip()
        # Split the line into parts at each comma.
        row = line.split(",")
        data.append(row)
    return data

def get_row(row, filename="data.csv"):
    """
    Returns a specific row from the CSV file as a list.
    The row number is 1-based (e.g., row=1 returns the first row).
    """
    data = read_csv(filename)
    index = row - 1  # Convert to 0-based index used in Python
    if index < 0 or index >= len(data):
        return []  # Return an empty list if the row number is out of range
    return data[index]

def get_column(column, filename="data.csv"):
    """
    Returns a specific column from the CSV file as a list.
    The column number is 1-based (e.g., column=1 returns the first column).
    """
    data = read_csv(filename)
    index = column - 1  # Convert to 0-based index used in Python
    result = []
    for row in data:
        # If the row has enough columns, add the value.
        if index < len(row):
            result.append(row[index])
        else:
            result.append("")  # If not, add an empty string.
    return result
