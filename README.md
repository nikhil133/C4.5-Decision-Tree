# C4.5-Decision-Tree
Advance version of ID3 algorithm Recursive Decision Tree (Machine Learning)

## About
ID3 (Iterative Dichotomiser 3)  is a decision tree algorithm which classifies its children on the basis of the information gain
based on the feature. Branches of the decision tree depends on the number of feature value a feature has.
ID3 is best used to classify data with shorter size. Since large amount of data will lead to increase in depth of of the tree which may lead to unwanted branches to achieve the accuracy at max to classify the classes.
  At this point c4.5 algorithm comes in handy. c4.5 splits in the same form as the ID3 but the children node is splited on the basis of threshold obtained from feature value which creates tree of a binary form. The depth of the tree is evaluated once the tree is generated.
Tree pruning is done to reduce the depth of the tree.

### Information Gain
      ##### Entropy: Entropy {\displaystyle H(S)} H(S) is a measure of the amount of uncertainty in the (data) set {\displaystyle S} S (i.e. entropy characterizes the (data) set {\displaystyle S} S).

{\displaystyle H(S)=\sum _{x\in X}-p(x)\log _{2}p(x)} {\displaystyle H(S)=\sum _{x\in X}-p(x)\log _{2}p(x)}
  
