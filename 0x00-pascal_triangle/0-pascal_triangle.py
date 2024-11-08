def pascal_triangle(n):


    # Return an empty list if n is less than or equal to 0
    if n <= 0:
        return []
    
    # Initialize the triangle with the first row
    triangle = [[1]]
    
    # Generate rows 1 through n-1
    for i in range(1, n):
        # Start each row with 1
        row = [1]
        # Populate the middle values of the row based on the previous row
        for j in range(1, i):
            row.append(triangle[i-1][j-1] + triangle[i-1][j])
        # End each row with 1
        row.append(1)
        # Add the completed row to the triangle
        triangle.append(row)
    
    return triangle
