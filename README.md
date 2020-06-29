# BD2pc4

# Face Recognition

The face recognition library for python plays an important role in this project, using only its basic functions we are able to transform a picture with a face in it into its characteristic vector. We use this vector to compare the facial features and determine if the same person appears in both pictures or if at least they are alike.

# Preprocessing

Given a database with >200mb worth of pictures of known people, sometimes with more than one photo of the same individual, we need to get every single vector for each picture and associate the corresponding name for each vector. Then, we write the resulting list of lists to disk so we only do this operation once. We perform this in [faceRecognition.py](./faceRecognition.py)

# KNN
KNN is a method used for classification and regression taks. In this project it will serve the role as
a classifier. The K nearest neighbors should return points (or faces in this case) that are similar
in the way of the category of the first.Here we compare the times it takes on a varying N sized database to search for the KNN. In our
examples we will use K = 10, or 10 most similar faces. TThe speed tests is done in a KNN implemented sequentially and then the use of a support multidimentional indexing data structure called RTree. Here we compare efficient are.

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
We will use the multimentional indexing structure RTree commonly used for spatial contents. However we know that a vector is finally a point in a D dimensional
space where D is the length of the vectore. By this logic the RTree should prove usefull for our propouse. To implement this we used the python libary *rtree* which allows for easy RTree creation and queuing.

### Implementation
We read the result vectors and create an RTree with a multidimentional index of 128 dimentions, we
then proceed to insert each vector as a *region* of area 1 (point) inside the tree. This is done for
all test values of N (100, 200, 400, ... ,12800) finally we run a query, that is a random vector
that was chosen beforehand, for the knn (we use k = 10). Again, the implementation can be seen [here](./rtree_knn.py)

## Comparison

Given different values *N* that represents the size of the collection, we timed the performance of both structures doing a KNN search using *k* = 16 for each *N* and we got the following results:

| Time        | KNN-RTree | KNN-Sequential |
| ----------- | --------- | -------------- |
| *N* = 100   | 0.8595    | 0.8906         |
| *N* = 200   | 0.8362    | 0.8077         |
| *N* = 400   | 0.8718    | 0.8221         |
| *N* = 800   | 0.8446    | 0.9090         |
| *N* = 1600  | 0.8768    | 0.8787         |
| *N* = 3200  | 1.0006    | 0.9886         |
| *N* = 6400  | 1.1493    | 1.1610         |
| *N* = 12800 | 1.5023    | 1.4575         |

