import matplotlib.pyplot as plt


def overall_chart(data, crit_number, crit_name, file_name, log_scale):
    plt.clf()
    # Inicjalizacja list sumarycznych dla każdego algorytmu
    sum_astar = [0.0] * 8
    sum_bfs = [0.0] * 8
    sum_dfs = [0.0] * 8

    # Inicjalizacja list średnich wartości dla każdego algorytmu
    avg_astar_table = []
    avg_bfs_table = []
    avg_dfs_table = []

    astar_counts = [0.0] * 7
    bfs_counts = [0.0] * 7
    dfs_counts = [0.0] * 7

    # Przetwarzanie danych i obliczanie sum oraz ilości wystąpień
    for d in data:
        index = int(d[0])
        value = float(d[crit_number + 3])

        if d[2] == 'astr':
            sum_astar[index] += value
            sum_astar[0] += 1
            astar_counts[index - 1] += 1.0
        elif d[2] == 'bfs':
            sum_bfs[index] += value
            sum_bfs[0] += 1
            bfs_counts[index - 1] += 1.0
        elif d[2] == 'dfs':
            sum_dfs[index] += value
            sum_dfs[0] += 1
            dfs_counts[index - 1] += 1.0

    # Obliczanie średnich wartości dla każdego algorytmu
    for i in range(0, 7):
        avg_astar_table.append(sum_astar[i + 1] / astar_counts[i])
        avg_bfs_table.append(sum_bfs[i + 1] / bfs_counts[i])
        avg_dfs_table.append(sum_dfs[i + 1] / dfs_counts[i])

    # Generowanie wykresu
    x = [1, 2, 3, 4, 5, 6, 7]
    plt.hist(
        [x, x, x],
        weights=[avg_bfs_table, avg_dfs_table, avg_astar_table],
        label=['BFS', 'DFS', 'A*'],
        color=['#4169E1', '#FF8C00', '#228B22'],
        bins=[0.5, 1.5, 2.5, 3.6, 4.5, 5.5, 6.5, 7.5]
    )

    # Konfiguracja osi i legendy
    plt.title('Overall')
    plt.xlabel('Solution Depth')
    plt.ylabel(crit_name)
    plt.legend(('BFS', 'DFS', 'A*'), loc='upper right')

    # Opcjonalne skalowanie logarytmiczne osi y
    if log_scale:
        plt.yscale("log")

    # Zapisanie wykresu do pliku
    plt.savefig('./charts/' + file_name)

def load_data(file_path):
    with open(file_path, 'r', encoding='utf-8') as csvfile:
        data_frame = list()
        for line in csvfile.readlines():
            array = line.split()
            data_frame.append(array)

    return data_frame


# Wczytanie danych
data = load_data('Data.csv')

# Generowanie wykresów podsumowujących dla różnych kryteriów
overall_chart(data, 1, "Solution Length", "overall_solution_length", False)
overall_chart(data, 2, "Number of Visited States (log scale)", "overall_visited_states", True)
overall_chart(data, 3, "Number of Processed States (log scale)", "overall_processed_states", True)
overall_chart(data, 4, "Max Recursion Depth Reached", "overall_recursion_depth", False)
overall_chart(data, 5, "Computation Time [ms] (log scale)", "overall_computation_time", True)
