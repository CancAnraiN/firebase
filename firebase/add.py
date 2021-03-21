
# 引用必要套件
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

# 引用私密金鑰
# path/to/serviceAccount.json 請用自己存放的路徑
cred = credentials.Certificate('cmail-46498-firebase-adminsdk-iry01-15f00b3be5.json')

# 初始化firebase，注意不能重複初始化
firebase_admin.initialize_app(cred)

# 初始化firestore
db = firestore.client()

doc = {
    'name': "罐罐",
    'email': "gary@gmail.com"
}

# 語法
# ref = db.collection("集合路徑")

doc_ref = db.collection("Users").document("user1")

# ef提供一個add的方法，input必須是文件，型別是dictionary

doc_ref.set(doc)
