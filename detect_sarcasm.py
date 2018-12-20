# Uses the data.csv file to train the classifiers
from sklearn.neural_network import MLPClassifier
from sklearn.metrics import confusion_matrix
from sklearn.metrics import precision_score
from sklearn.metrics import recall_score
from sklearn.metrics import accuracy_score

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
    
    return X, y, feats

# TODO: tweak parameters
def nn_clf():

    clf = MLPClassifier(solver='lbfgs', alpha=1e-5,
                    hidden_layer_sizes=(5, 2), random_state=1)
    
##    MLPClassifier(activation='relu', alpha=1e-05, batch_size='auto',
##                  beta_1=0.9, beta_2=0.999, early_stopping=False,
##                  epsilon=1e-08, hidden_layer_sizes=(5, 2),
##                  learning_rate='constant', learning_rate_init=0.001,
##                  max_iter=200, momentum=0.9, n_iter_no_change=10,
##                  nesterovs_momentum=True, power_t=0.5, random_state=1,
##                  shuffle=True, solver='lbfgs', tol=0.0001,
##                  validation_fraction=0.1, verbose=False, warm_start=False)
    return clf


if __name__ == '__main__':
    testf = 'data/data.csv'
    trainf = 'data/test_data1.csv'
    print("getting training data")
    X, y, feats = get_data(testf)

    print("setting up classifier")
    clf = nn_clf()
    print("fitting classifier")
    clf.fit(X, y)

    print("getting test data")
    Xt, yt, _ = get_data(trainf)

    print("predicting labels")
    y_pred = clf.predict(Xt)
    print('confusion matrix:\n', confusion_matrix(yt, y_pred, [0,1]))
    print('precision:\n', precision_score(yt, y_pred, [0,1]))
    print('recall:\n', recall_score(yt, y_pred, [0,1]))
    print('accuracy:\n', accuracy_score(yt, y_pred, [0,1]))
