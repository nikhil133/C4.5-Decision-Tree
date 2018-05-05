# C4.5-Decision-Tree
__Advance version of ID3 algorithm Recursive Decision Tree (Machine Learning)

## About
_ID3 (Iterative Dichotomiser 3)  is a decision tree algorithm which classifies its children on the basis of the information gain
based on the feature. Branches of the decision tree depends on the number of feature value a feature has.
ID3 is best used to classify data with shorter size. Since large amount of data will lead to increase in depth of of the tree which may lead to unwanted branches to achieve the accuracy at max to classify the classes.
_At this point c4.5 algorithm comes in handy. c4.5 splits in the same form as the ID3 but the children node is splited on the basis of threshold obtained from feature value which creates tree of a binary form. The depth of the tree is evaluated once the tree is generated.
Tree pruning is done to reduce the depth of the tree.

### Information Gain
  **Entropy**: Entropy H(S) is a measure of the amount of uncertainty in the (data) set S
               H(S) = ![entropy](http://latex.codecogs.com/png.latex?-%5Csum_%7Bx%5Cepsilon%20X%7DP%28x%29*%5Clog_%7B2%7DP%28x%29)
                      
  **Information gain**: Information gain IG(A) is the measure of the difference in entropy from before to after the set S is split on an attribute A. In other words, how much uncertainty in S was reduced after splitting set S on attribute A.
               ![information gain](https://wikimedia.org/api/rest_v1/media/math/render/svg/5668519b925f915f58aba9ae4f3ba44bde588ef2)

  **Threshold**: Threshold is calculated as the average of sum of the positive class and negative class value for the feature which has the max information gain
  
## Example on Number.csv data

|Number|Goal|
|---|---|
|1|No|
|315|Yes|
|70|Yes|
|120|Yes|
|106|Yes|
|15|No|
|80|No|
|107|Yes|
|70|No|
|150|Yes|

  
