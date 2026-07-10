import math
import numpy as np
import matplotlib.pyplot as plt

def one_dimensional_function(x):
    return x**2 + 5 * math.sin(x)

def two_dimensional_function(x, y):
    return x**2 - y**3 + 7*y

def simulated_annealing(objective_function, initial_solution, temperature, cooling_rate, num_iterations, optimization_type):
    current_solution = initial_solution
    current_value = objective_function(*current_solution)

    for i in range(num_iterations):
        neighbor_solution = current_solution + np.random.uniform(-0.5, 0.5, size=len(current_solution))
        neighbor_value = objective_function(*neighbor_solution)

        # Zależnie od wyboru optymalizacji (minimum lub maksimum)
        if (optimization_type == 'minimum' and neighbor_value < current_value) or \
           (optimization_type == 'maksimum' and neighbor_value > current_value) or \
           np.random.rand() < np.exp(-(neighbor_value - current_value) / temperature):

            current_solution = neighbor_solution
            current_value = neighbor_value

        temperature *= cooling_rate

    return current_solution, current_value

def get_user_function(dimensions):
    if dimensions == 1:
        function_str = input("Wprowadź funkcję jednowymiarową f(x): ")
        return lambda x: eval(function_str)
    elif dimensions == 2:
        function_str = input("Wprowadź funkcję dwuwymiarową f(x, y): ")
        return lambda x, y: eval(function_str)
    else:
        print("Nieobsługiwana liczba wymiarów.")

def plot_function(objective_function, solution, title):
    if len(solution) == 1:
        x_values = np.linspace(solution[0] - 10, solution[0] + 10, 100)
        y_values = [objective_function(x) for x in x_values]
        plt.plot(x_values, y_values, label='Funkcja celu')
        plt.scatter(solution[0], objective_function(solution[0]), color='red', label=title)
        plt.xlabel('x')
        plt.ylabel('Wartość funkcji celu')
        plt.legend()
        plt.show()
    elif len(solution) == 2:
        x_values = np.linspace(solution[0] - 10, solution[0] + 10, 100)
        y_values = np.linspace(solution[1] - 10, solution[1] + 10, 100)
        X, Y = np.meshgrid(x_values, y_values)
        Z = objective_function(X, Y)
        fig = plt.figure()
        ax = fig.add_subplot(111, projection='3d')
        ax.plot_surface(X, Y, Z, cmap='viridis')
        ax.scatter(solution[0], solution[1], objective_function(*solution), color='red', label=title)
        ax.set_xlabel('x')
        ax.set_ylabel('y')
        ax.set_zlabel('Wartość funkcji celu')
        plt.show()

if __name__ == "__main__":
    dimensions = int(input("Podaj liczbę wymiarów funkcji (1 lub 2): "))

    if dimensions not in [1, 2]:
        print("Nieobsługiwana liczba wymiarów.")
        exit()

    objective_function = get_user_function(dimensions)

    optimization_type = input("Czy chcesz wyliczyć minimum czy maksimum funkcji? (minimum/maksimum): ").lower()
    if optimization_type not in ['minimum', 'maksimum']:
        print("Niepoprawny rodzaj optymalizacji.")
        exit()

    if dimensions == 1:
        initial_solution = np.random.uniform(-10, 10),
    elif dimensions == 2:
        initial_solution = np.random.uniform(-10, 10), np.random.uniform(-10, 10)

    initial_temperature = 100.0
    cooling_rate = 0.95
    num_iterations = 1000

    result_solution, result_value = simulated_annealing(objective_function, initial_solution, initial_temperature, cooling_rate, num_iterations, optimization_type)

    plot_function(objective_function, result_solution, f"{optimization_type.capitalize()} funkcji")

    if optimization_type == 'minimum':
        print(f"Minimum funkcji: {result_solution}")
    else:
        print(f"Maksimum funkcji: {result_solution}")