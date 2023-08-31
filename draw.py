import csv
import matplotlib.pyplot as plt

def read_coordinates_from_csv(file_path):
    coordinates = []
    with open(file_path, 'r') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            x, y = map(float, row)
            coordinates.append((x, y))
    return coordinates


def calculate_image_size(coordinates):
    x_values, y_values = zip(*coordinates)
    max_x = max(x_values)
    max_y = max(y_values)
    return max_x + 20, max_y + 20


def plot_shape(coordinates):
    x_coordinates, y_coordinates = zip(*coordinates)
    # Create a figure and axis
    fig, ax = plt.subplots()
    # Plot the polygon using x and y coordinates
    ax.plot(x_coordinates, y_coordinates, marker='o')

    # Set labels and title
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_title('Polygon Shape')
    plt.show()


def calculate_polygon_area(coordinates):
    n = len(coordinates)
    area = 0
    for i in range(n):
        x1, y1 = coordinates[i]
        x2, y2 = coordinates[(i + 1) % n]
        area += (x1 * y2 - x2 * y1)
    return abs(area) / 2


def main(csv_file_path):
    coordinates = read_coordinates_from_csv(csv_file_path)
    print("Close shape window to see it's area")
    plot_shape(coordinates)
    print(f'polygon area: {calculate_polygon_area(coordinates)}')


if __name__ == "__main__":
    csv_file_path = 'shape.csv'
    main(csv_file_path=csv_file_path)
