# Uses the data.csv file to train the classifiers
from sklearn.neural_network import MLPClassifier

def get_data(file):
    # read the data from the data.csv file line-by-line
    # each line is an array in X (besides last line
    # the last element of each line is the y value

    X = [] # feature vector
    y = [] # labels
    
    f = open(file, 'r')
    for line in f:
        vs = line.split(', ')
        X.append(vs[:-1])
        y.append(vs[-1])
    
    return X, y

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


clf.predict(Xt)


if __name__ == '__main__':
    testf = 'data/data.csv'
    trainf = 'data/_.csv' # TODO: make and put location of training file
    X, y = get_data(testf)

    clf = nn_clf()
    clf.fit(X, y)
    
    Xt, yt = get_data(trainf)

    clf.predict(Xt, yt)
