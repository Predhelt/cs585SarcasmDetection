# Uses the data.csv file to train the classifiers
import numpy as np
from sklearn.neural_network import MLPClassifier
from sklearn.metrics import confusion_matrix
from sklearn.metrics import precision_score
from sklearn.metrics import recall_score
from sklearn.metrics import accuracy_score
from sklearn.model_selection import KFold

def get_data(file):
    # read the data from the data.csv file line-by-line
    # each line is an array in X (besides last line
    # the last element of each line is the y value

    X = [] # feature vector
    y = [] # labels
    
    f = open(file, 'r')
    line = f.readline()
    feats = line.split(', ')
    for line in f:
        vs = line.split(', ')
        X.append(list(map(float, vs[:-1])))
        y.append(int(vs[-1]))
    
    return np.array(X), np.array(y), feats

# TODO: tweak parameters
def nn_clf():

##    clf = MLPClassifier(solver='lbfgs', alpha=1e-5,
##                    hidden_layer_sizes=(3, 2), random_state=1)
    
    clf = MLPClassifier(activation='relu', alpha=1e-05, batch_size='auto',
                  beta_1=0.9, beta_2=0.999, early_stopping=False,
                  epsilon=1e-08, hidden_layer_sizes=(3, 2),
                  learning_rate='constant', learning_rate_init=0.001,
                  max_iter=200, momentum=0.9, nesterovs_momentum=True, power_t=0.5, random_state=1,
                  shuffle=True, solver='lbfgs', tol=0.0001,
                  validation_fraction=0.1, verbose=False, warm_start=False)
    return clf

def cross_validate(clf, X, y):
    kf = KFold(n_splits=2)
    i = 1
    for train_index, test_index in kf.split(X):
        X_train, X_test = X[train_index], X[test_index]
        y_train, y_test = y[train_index], y[test_index]
        clf.fit(X_train, y_train)
        y_pred = clf.predict(X_test)
        print('fold ', i)
        print('confusion matrix:\n', confusion_matrix(y_test, y_pred, [0,1]))
        print('precision:\n', precision_score(y_test, y_pred, [0,1]))
        print('recall:\n', recall_score(y_test, y_pred, [0,1]))
        print('accuracy:\n', accuracy_score(y_test, y_pred, [0,1]))
        print('---------------------')
        i+=1

if __name__ == '__main__':
    trainf = 'data/data.csv'
    testf = 'data/test_data1.csv'
    print("getting training data")
    X, y, feats = get_data(trainf)
    print("getting test data")
    Xt, yt, _ = get_data(testf)

##    Xv = np.concatenate([X, Xt], axis=0)
##    yv = np.concatenate([y, yt], axis=0)

    print("setting up classifier")
    clf = nn_clf()
##    print("running cross validation")
##    cross_validate(clf, Xv, yv)
    print("fitting classifier")
    clf.fit(X, y) # swapped training for test because test had more data

    

    print("predicting labels")
    y_pred = clf.predict(Xt)
    print('confusion matrix:\n', confusion_matrix(yt, y_pred, [0,1]))
    print('precision:\n', precision_score(yt, y_pred, [0,1]))
    print('recall:\n', recall_score(yt, y_pred, [0,1]))
    print('accuracy:\n', accuracy_score(yt, y_pred, [0,1]))

    failed_indices = []
    for i in range(len(y_pred)):
        if y_pred[i] != yt[i]:
            failed_indices.append(i)

    for i in failed_indices:
        print(i+1, 'prediction:', y_pred[i], 'truth:', yt[i])
    
