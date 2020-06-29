# BD2pc4

# Face Recognition

The face recognition library for python plays an important role in this project, using only its basic functions we are able to transform a picture with a face in it into its characteristic vector. We use this vector to compare the facial features and determine if the same person appears in both pictures or if at least they are alike.

# Preprocessing

Given a database with >200mb worth of pictures of known people, sometimes with more than one photo of the same individual, we need to get every single vector for each picture and associate the corresponding name for each vector. Then, we write the resulting list of lists to disk so we only do this operation once. We perform this in [faceRecognition.py](./faceRecognition.py)

# KNN

Here we compare the times it takes on a varying N sized database to search for the KNN. In our
examples we will use K = 10. The tests are on KNN search based off an RTree or in a sequential
manner.

## Sequential
### Implementation

In order to implement our own sequential algorithm to find the *k* nearest faces in the whole dataset regarding an input, we need to order our list of characteristic vectors using the distance to our input as a key. After that, we take the *k* first elements of the resulting list. We are given two distance options: Euclidean distance and Manhattan Distance. We tested both of them for accuracy and here are the results:

*Using Nicole Kidman because she has a total of 19 photos in our database*

| Accuracy | ED    | MD    |
| -------- | ----- | ----- |
| *k* = 4  | 4/4   | 4/4   |
| *k* = 8  | 8/8   | 8/8   |
| *k* = 16 | 15/16 | 15/16 |

*Second try with Jennifer Lopez (21 photos in total)*

| Accuracy | ED    | MD    |
| -------- | ----- | ----- |
| *k* = 4  | 4/4   | 4/4   |
| *k* = 8  | 8/8   | 8/8   |
| *k* = 16 | 16/16 | 13/16 |

Using these results, we can conclude that using Euclidean distance is slightly more accurate than using Manhattan distance, therefore, we will be using ED from this point on.

It's worth noting that we do not have a priority queue where we insert each element since theoretically, the cost of pushing an element into a priority queue has a cost of log(n) making it a total cost of nlog(n) to insert the whole list. Compared to using a sorting algorithm, the cost is the same. The implementation can be seen [here](./Secuential_KNN.py)

## RTree
Here we used the python libari *rtree* which allows for easy RTree creation and queuing.

### Implementation
We read the result vectors and create an RTree with a multidimentional index of 128 dimentions, when
then proceed to insert each vector as a *region* of area 1 (point) inside the tree. This is done for
all test values of N (100, 200, 400, ... ,12800) finally we run a query, that is a random vector
that was chosen beforehand, for the knn (we use k = 10). Again, the implementation can be seen [here](./rtree_knn.py)

## Comparison

Given different values *N* that represents the size of the collection, we timed the performance of both structures doing a KNN search using *k* = 16 for each *N* and we got the following results:

| Time        | KNN-RTree | KNN-Sequential |
| ----------- | --------- | -------------- |
| *N* = 100   |           |                |
| *N* = 200   |           |                |
| *N* = 400   |           |                |
| *N* = 800   |           |                |
| *N* = 1600  |           |                |
| *N* = 3200  |           |                |
| *N* = 6400  |           |                |
| *N* = 12800 |           |                |

## Conclusion



These are the results for the different values of N.
100: 0.0006661415100097656 seconds
200: 0.0004992485046386719 seconds
400: 0.0010790824890136719 seconds
800: 0.0012073516845703125 seconds
1600: 0.0020966529846191406 seconds
3200: 0.005741596221923828 seconds
6400: 0.015937089920043945 seconds
12800: 0.03295302391052246 seconds
