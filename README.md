# Classification On  X-Ray Diagnosis Images

<a  style = "color:red;" href="https://www.kaggle.com/sahintiryaki/xray-pneumonia-detection-90">Go Kaggle Notebook</a> <br>
## Application Video

![](https://github.com/SahinTiryaki/Classification-On-X-Ray-Diagnosis-Images./blob/main/static/images/app.gif)

## Data :orange_book:

#### What's the Pneumonia :grey_question:
&nbsp;&nbsp;&nbsp;Pneumonia is an infection that inflames the air sacs in one or both lungs. The air sacs may fill with fluid or pus (purulent material), causing cough with phlegm or pus, fever, chills, and difficulty breathing. A variety of organisms, including bacteria, viruses and fungi, can cause pneumonia. Pneumonia can range in seriousness from mild to life-threatening. It is most serious for infants and young children, people older than age 65, and people with health problems or weakened immune systems.<br>
&nbsp;&nbsp;&nbsp;The dataset have two classes; Normal (0), Pneumonia (1). The dataset was divied train-test-split. If you look at the above, you will see the images of dataset and count of images int the dataset.The are  5,863 X-Ray images (JPEG) in the dataset.İmages were replaced height and widht.Images's widht and height are 196 <br>
**Dataset File Architecture**<br>
<p align="left">
  <img src="https://github.com/SahinTiryaki/Classification-On-X-Ray-Diagnosis-Images./blob/main/static/images/datastructure.png" height="200" width="150" >
</p>
<strong>Images :arrow_down:</strong>
<p align="left">
  <img src="https://github.com/SahinTiryaki/Classification-On-X-Ray-Diagnosis-Images./blob/main/static/images/xraygoruntu.png" height="400" width="500" >
</p>

**Count of Images in The Dataset :bar_chart:**
<p align="left">
  <img src="https://github.com/SahinTiryaki/Classification-On-X-Ray-Diagnosis-Images./blob/main/static/images/miktarlar.png"  height="320" width="600" >
</p>
<a  style = "color:red;" href="https://www.kaggle.com/paultimothymooney/chest-xray-pneumonia">Go Images Repository</a> <br>

## Model
&nbsp;&nbsp;&nbsp;Given the dataset, the model is implemented based on a classification task. Model is implemented in deep learning library Tensorflow and the Model is selected as pretrained model VGGNet16<br>
**Model Power :muscle:** <br>
&nbsp;&nbsp;&nbsp;In the model, hyperparameters are chosen; batch size of 80 , epoch range of 10.This model was saved .h5 format for using again. Look at the below for understanding Model Architecture<br>
<p>
Line Cart about train dataset and validation  dataset<br>
<img src="https://github.com/SahinTiryaki/Classification-On-X-Ray-Diagnosis-Images./blob/main/static/images/tahmingrafik.png" height="300" width="600" >
</p>
<p>
  Confusion Matrix <br>
     <img src="https://github.com/SahinTiryaki/Classification-On-X-Ray-Diagnosis-Images./blob/main/static/images/confusionmatrix.png" height="300" width="500" >
 </p>

 <p>
  Classification Report <br>
     <img src="https://github.com/SahinTiryaki/Classification-On-X-Ray-Diagnosis-Images./blob/main/static/images/classificationreport.png" height="150" width="350" >
 </p>
<br>

<h2>Requirements :hammer_and_wrench:	</h2>
If you are thinking of using this project, you should use this commands. <br>

```  
  git clone  https://github.com/SahinTiryaki/Classification-On-X-Ray-Diagnosis-Images..git
    
```

```  
  pip install -r requirements.txt
    
```
```  
  python3 app.py
    
```

