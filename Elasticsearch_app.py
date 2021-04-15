import streamlit as st
import os
import pandas as pd
import requests
from elasticsearch import Elasticsearch
from PIL import Image
import requests
from io import BytesIO


## Start the elasticsearch service on EC2
es = Elasticsearch(['http://54.81.254.7:9200/'])
st.header('Search similar images using Elasticsearch')
st.subheader('Select an image from the dropdown')
s=st.selectbox('',('0_0.jpg','100012_0.jpg','1000332_0.jpg'))
slid=st.slider('How many similar images you want to see?', 0, 10, 1)
button_clicked = st.button('Submit')
result = es.ping()
images_path = 'https://raw.githubusercontent.com/aakash-atnoorkar/Team5_INFO7374_Spring2021/main/Assignment%203/images/'

if button_clicked:

	st.text('Selected Image')
	st.image(images_path+str(s))
	res= es.search(index='spotify_annoy',body={'query':{'match':{'master_pi':str(s)}}})
	#st.write('response == ', res)
	st.text('Matching images are: ')
	d=[]
	for hit in res['hits']['hits']:
	    url=(hit['_source']['similar_pi'])
	    response = requests.get(images_path+url)
	    #img=Image.open(BytesIO(response.content))
	    d.append(images_path+url)
	for i in range(0,slid):
	    st.image(d[i])
