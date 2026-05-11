import pandas as pd
import joblib
from sklearn.pipeline import Pipeline, FeatureUnion
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.svm import LinearSVC
from sklearn.calibration import CalibratedClassifierCV
from sklearn.model_selection import train_test_split, StratifiedKFold
from sklearn.metrics import classification_report, accuracy_score

df=pd.read_csv("training_data.csv").dropna()
X=df["text"].astype(str)
y_intent=df["intent"].astype(str)
y_product=df["product"].astype(str)


product_counts=y_product.value_counts()
valid_products=product_counts[product_counts>=2].index
X_product=X[y_product.isin(valid_products)]
y_product_filtered=y_product[y_product.isin(valid_products)]

X_train,X_test,yi_train,yi_test=train_test_split(
    X, y_intent, test_size=0.2, random_state=42, stratify=y_intent
)
X_train2,X_test2,yp_train,yp_test=train_test_split(
    X_product,
    y_product_filtered,
    test_size=0.2,
    random_state=42,
    stratify=y_product_filtered
)

intent_model=Pipeline([
    ("tfidf",TfidfVectorizer(
        lowercase=True,
        stop_words="english",
        ngram_range=(1,2)
    )),
    ("clf", LogisticRegression(max_iter=2000))
])

intent_model.fit(X_train,yi_train)
print("INTENT:")
print("Accuracy:", accuracy_score(yi_test,intent_model.predict(X_test)))
print(classification_report(yi_test,intent_model.predict(X_test)))
joblib.dump(intent_model, "intent_model.pkl")
print("Intent model saved.\n")

product_features=FeatureUnion([
    ("word_tfidf",TfidfVectorizer(
        lowercase=True,
        analyzer="word",
        ngram_range=(1,2),
        min_df=1,
        sublinear_tf=True
    )),
    ("char_tfidf",TfidfVectorizer(
        lowercase=True,
        analyzer="char_wb",
        ngram_range=(3,5),
        min_df=1,
        sublinear_tf=True
    )),
])

product_model=Pipeline([
    ("features",product_features),
    ("clf",CalibratedClassifierCV(
        LinearSVC(max_iter=3000,C=1.0),
        cv=2,
        method="sigmoid"
    ))
])

product_model.fit(X_train2, yp_train)
print("PRODUCT:")
print("Accuracy:",accuracy_score(yp_test,product_model.predict(X_test2)))
print(classification_report(yp_test,product_model.predict(X_test2)))
joblib.dump(product_model, "product_model.pkl")
print("Product model saved.\n")

