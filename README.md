# BD2pc4


# KNN
Here we compare the times it takes on a varying N sized database to search for the KNN. In our
examples we will use K = 10. The tests are on KNN search based off an RTree or in a sequential
manner.

## Sequential
### Implementation
### Results

## RTree
Here we used the python libari *rtree* which allows for easy RTree creation and quering.

### Implementation
We read the result vectors and create an RTree with a multidimentional index of 128 dimentions, when
then proceed to insert each vector as a *region* of area 1 (point) inside the tree. This is done for
all test values of N (100, 200, 400, ... ,12800) finally we run a query, that is a random vector
that was chosen beforehand, for the knn (we use k = 10).

### Results
These are the results for the different values of N.
100: 0.0006661415100097656 seconds
200: 0.0004992485046386719 seconds
400: 0.0010790824890136719 seconds
800: 0.0012073516845703125 seconds
1600: 0.0020966529846191406 seconds
3200: 0.005741596221923828 seconds
6400: 0.015937089920043945 seconds
12800: 0.03295302391052246 seconds
