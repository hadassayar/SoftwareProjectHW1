import math
import sys


def kmeans(K, iter, input_data):
    epsilon = 0.0001
    num_of_clusters = K
    file = input_data
    array_of_centroids = build_table(num_of_clusters, input_data)[0] #initialize a table with the first k vectors in the input file
    N = build_table(num_of_clusters, input_data)[1]
    if num_of_clusters >= N:
        print("Invalid number of clusters!")
        return
    iter_cnt = 0
    delta = epsilon + 1
    while(iter_cnt < iter and delta >= epsilon):
        clusters = [[] for i in range(num_of_clusters)]
        iter_cnt +=1
        interactive_file = open(file, 'r')
        lines = interactive_file.readlines()
        line_index = 0
        for line in lines:
            line_index += 1
            if (iter_cnt == 1) and (line_index <= num_of_clusters):
                vector = list(line.split(","))
                vector1 = create_vector(vector)
                clusters.append(vector1)
                continue
            vector = list(line.split(","))
            vector1 = create_vector(vector)
            d = len(vector1)
            min_distance = math.inf
            min_distance_index = -1
            for i in range(num_of_clusters):
                curr_distance = calc_distance(vector1, array_of_centroids[i])
                if curr_distance < min_distance:
                    min_distance = curr_distance
                    min_distance_index = i
            clusters[min_distance_index].append(vector1)
        array_of_centroids = update_centroid(clusters, num_of_clusters, d)
        if iter_cnt != 1:
            delta = calc_delta(array_of_centroids, prev_array_of_centroids)
        prev_array_of_centroids = array_of_centroids.copy()
        line_index = 0
        interactive_file.close()
    return create_output(array_of_centroids)


def calc_delta(new_centroids, prev_centroids):
    delta = 0
    for i in range(len(new_centroids)):
        distance = calc_distance(new_centroids[i],prev_centroids[i])
        if distance > delta:
            delta = distance
    return delta


def build_table(num_of_clusters, input_data):
    array_of_centroids = [[] for i in range(num_of_clusters)]
    file = input_data
    interactive_file = open(file, 'r')
    lines = interactive_file.readlines()
    line_index = 0
    for line in lines:
        vector = list(line.split(","))
        vector1 = create_vector(vector)
        if line_index < num_of_clusters:
            array_of_centroids[line_index] = vector1
            line_index += 1
        else:
            break
    N = len(lines)
    interactive_file.close()
    return [array_of_centroids ,N]


def create_vector(vector):
    vector[-1] = vector[-1][:len(vector[-1]) - 2]
    for j in range(len(vector)):
        vector[j] = float(vector[j])
    return vector


def calc_distance(vector1, vector2):
    i = 0
    summ = 0
    for i in range(len(vector1)):
        summ += pow((vector1[i] - vector2[i]), 2)
    return math.sqrt(summ)


def update_centroid(clusters, num_of_clusters, d):
    new_centroids = [[] for i in range(num_of_clusters)]
    for i in range(num_of_clusters):
        new_centroids[i] = [0 for i in range(d)]
        num_of_points = len(clusters[i])
        for point in clusters[i]:
            for coord in range(d):
                new_centroids[i][coord] += point[coord] / num_of_points
    return new_centroids


def create_output(vectors_array):
    for vector in vectors_array:
        for i in range(len(vector)):
            vector[i] = '{:.4f}'.format(vector[i])
        print(','.join(vector))


def main():
    lst_of_arguments = sys.argv
    first_argument = int(lst_of_arguments[1])
    second_argument = lst_of_arguments[2]
    if second_argument.isdigit():
        if int(second_argument) >= 1000 or int(second_argument) < 0:
            print("Invalid maximum iteration!")
            return
        else:
            kmeans(first_argument, int(second_argument), lst_of_arguments[3])
    else:
        kmeans(first_argument, 200, lst_of_arguments[2])


if __name__ == "__main__":
    main()
