import math
import sys


def kmeans(K, iter, input_data):
    epsilon = 0.001
    num_of_clusters = K
    array_of_centroids = [[] for i in range(K)]
    file = input_data
    interactive_file = open(file, 'r')
    lines = interactive_file.readlines()
    N = len(lines)
    if num_of_clusters >= N:
        print("Invalid number of clusters!")
        return
    line_index = 0
    count_iter = 0
    for line in lines:
        if count_iter >= iter:
            return create_output(array_of_centroids)
        count_iter += 1
        vector = list(line.split(","))
        vector[-1] = vector[-1][:len(vector[-1]) - 2]
        for j in range(len(vector)):
            vector[j] = float(vector[j])
        vector.append(1)
        if line_index < K:
            array_of_centroids[line_index] = vector
            line_index += 1
        else:
            min_distance = math.inf
            min_distance_index = -1
            for i in range(num_of_clusters):
                curr_distance = calc_distance(vector, array_of_centroids[i])
                if curr_distance < min_distance:
                    min_distance = curr_distance
                    min_distance_index = i
            update = update_centroid(array_of_centroids[min_distance_index], vector)
            array_of_centroids[min_distance_index] = update[0]
            if update[1] < epsilon:
                return create_output(array_of_centroids)


def calc_distance(vector1, vector2):
    i = 0
    summ = 0
    for i in range(len(vector1) - 1):
        summ += pow((vector1[i] - vector2[i]), 2)
    return math.sqrt(summ)


def update_centroid(curr_centroid, new_vector):
    num_of_points = curr_centroid[-1]
    new_centroid = [0] * len(curr_centroid)
    new_centroid[-1] = num_of_points + 1
    for i in range(len(curr_centroid) - 1):
        new_centroid[i] = ((curr_centroid[i] * num_of_points) + new_vector[i]) / (num_of_points + 1)
    distance = calc_distance(curr_centroid, new_centroid)
    return [new_centroid, distance]


def create_output(vectors_array):
    for vector in vectors_array:
        for i in range(len(vector) - 1):
            vector[i] = '{:.4f}'.format(vector[i])
        vector.pop()
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
