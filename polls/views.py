from django.http import HttpResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from keras.models import load_model
from .chatbot import *
from django.http import JsonResponse
@csrf_exempt

# from tensorflow import keras

# import os
# import numpy as np

# app=Flask(__name__)

# app.config['SECRET_KEY'] = 'AAAAAAAAAA'   



# size=130
# def predict_image(img_path):
#     im=keras.preprocessing.image.load_img(img_path,target_size=(size,size))
#     im=keras.preprocessing.image.img_to_array(im)
#     im=np.array(im).reshape(-1,size,size,3)
#     p=model.predict(im)
#     print(p)
#     return p

# @app.route('/')
# def index():
#     return render('index.html')

# # @app.route('/about')
# def about():
#     return render('about.html')


# @app.route('/image',methods=['GET','POST'])
# def image():
#     if request.method=='POST':
#         fakepath=request.form.get("todo")
#         print(fakepath)
#         img_path='/static/images/predict_images/'+fakepath.split("\\")[-1]
#         im_path='C:/Users/Lenovo/Desktop/WebApplication'+img_path
#         predict=jsonify({'categories':categories[np.argmax(predict_image(im_path))],
#                         'img':"<img class='pred_img' src="+img_path+" alt="">",
#                         'cat':str(predict_image(im_path)[0][0]),
#                         'dog':str(predict_image(im_path)[0][1])})
#         return predict


def index(request):
    return render(request, 'polls/index.html')

def about(request):
    return render(request, 'polls/about.html')

def chatbot(request):
    
    if request.method=='POST':
        
        
        message=request.POST['question']
        print(message)

        pred=predict_class(message)
        print(pred)
        res=get_response(pred)
        return JsonResponse({'res':res})

def chat(request):
    return render(request, 'polls/chat.html')
    
# def chat(request):
#     if request.method=='POST':
#         print('hh')
#         message=request.POST['message']
#         # pred=predict_class(message)
#         # res=get_response(pred)
#         print(message)

        
#     return render(request, 'polls/chat.html')


def cart(request):
    return render(request, 'polls/cart.html')