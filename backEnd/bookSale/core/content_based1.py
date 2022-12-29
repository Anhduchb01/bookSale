import pandas as pd
import numpy as np
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.linear_model import Ridge
from sklearn import linear_model
from sklearn.preprocessing import OneHotEncoder

def get_items_rated_by_user(rate_matrix, user_id):
    y = rate_matrix[:,0]
    ids = np.where(y == user_id)[0]
    item_ids = rate_matrix[ids, 1] - 1
    scores = rate_matrix[ids, 2]
    return (item_ids, scores)

class Contentbased:
    def __init__(self, Y, X_train, n_users, n_items, lamda = 1):
        self.Y = Y
        self.lamda = lamda
        self.X_train = X_train
        self.n_users = n_users
        self.n_items = n_items
        
    def fit(self):
        transformer = TfidfTransformer(smooth_idf=True, norm ='l2')
        tfidf = transformer.fit_transform(self.X_train.tolist()).toarray()
        d = tfidf.shape[1] # data dimension
        W = np.zeros((d, self.n_users))
        b = np.zeros((1, self.n_users))
        for n in range(self.n_users):    
            ids, scores = get_items_rated_by_user(self.Y, n)
            clf = Ridge(alpha= self.lamda, fit_intercept  = True)
            Xhat = tfidf[ids, :]
            clf.fit(Xhat, scores) 
            W[:, n] = clf.coef_
            b[0, n] = clf.intercept_
        self.Yhat = tfidf.dot(W) + b
        
    def RMSE(self, Data_test):
        se = 0
        cnt = 0
        for n in range(self.n_users):
            ids, scores_truth = get_items_rated_by_user(Data_test, n)
            scores_pred = self.Yhat[ids, n]
            e = scores_truth - scores_pred 
            se += (e*e).sum(axis = 0)
            cnt += e.size 
        return np.sqrt(se/cnt)
    
    def recommend(self, user_id, top):
        a = np.zeros((self.n_items,))
        recommended_items = []
        items_rated_by_user, score = get_items_rated_by_user(self.Y, user_id)
        for i in range(self.n_items):
            if i not in items_rated_by_user:
                a[i] = self.Yhat[i, user_id]
        if len(a) < top:
            recommended_items = np.argsort(a)[-len(a):]
        else:
            recommended_items = np.argsort(a)[-top:]
        return recommended_items

def process_data(rating, category, product):
    ## Process rating 
    rating = pd.DataFrame(rating["Rating"])[["user_id",'product_id',"rating"]]
    rate_train = rating.to_numpy()
    n_users = len(rating["user_id"].unique())

    categories = pd.DataFrame(category["Category"])
    trans = dict()
    for i in range(len(categories)):
        trans[categories['category_id'][i]] = categories['category_name'][i]
    
    product = pd.DataFrame(product["Product"])[["product_id", "category_id"]]

    n_items = product.shape[0]
    print('Number of items:', n_items)
    transform = OneHotEncoder().fit([[i] for i in range(max(product['category_id'])+1)])
    product['feature'] = [transform.transform([[product['category_id'][i]]]).toarray()[0] for i in range(len(product))]

    X_train = product['feature'].to_numpy()[:,-1]
    # X_train_counts = np.zeros((X_train.shape[0],34))
    # for i in range(len(X_train)):
    #     for j in range(len(X_train[i])):
    #         X_train_counts[i,j] = X_train[i][j]
            
    return rate_train, X_train, n_users, n_items

def get_item_cb_for_user(rating, category, product, id_user):
    rate_train, X_train, n_users, n_items = process_data(rating, category, product)
    cb = Contentbased(rate_train, X_train, n_users=n_users, n_items=n_items)
    cb.fit()
    return list(cb.recommend(id_user, 4))

