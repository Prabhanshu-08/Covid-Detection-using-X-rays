**Covid Detection Using X-Rays**



![CD2](https://user-images.githubusercontent.com/88246010/222777237-6df3537d-1116-4233-a2ba-a81d415a261f.gif)



It is a simple DL project to detect covid through X-ray images of chest. The model has been trained on images of chest x-rays and dataset can be found in kaggle.

**Data Source**

[KAGGLE](https://www.kaggle.com/datasets/fusicfenta/chest-xray-for-covid19-detection)

**Motivation**

The COVID-19 pandemic has had a profound impact on the world, affecting millions of people and leading to significant changes in our daily lives. One of the key challenges in managing this crisis has been the rapid and accurate detection of COVID-19 cases. X-ray imaging is a widely available and non-invasive diagnostic tool that has shown promise in detecting COVID-19 in patients and help them before its too late.

**Built with**

Matplotlib,
Pandas,
Numpy,
Seaborn,
Tensorflow,
Keras,
CV2

**Usage**

* Before the following steps make sure you have [git](https://git-scm.com/download), [Anaconda](https://www.anaconda.com/) or [miniconda](https://docs.conda.io/en/latest/miniconda.html) installed on your system

* Clone the complete project with git clone https://github.com/Prabhanshu-08/Covid-Detection-using-X-rays.git or you can just download the code and unzip it

* Once the project is cloned, open anaconda prompt in the directory where the project was cloned and paste the following block

```
conda create -n covid_detection python=3.8.8
pip install -r requirements.txt
conda activate covid_detection 
```

* After creating an environment go to this [drive](https://drive.google.com/drive/u/0/folders/10auHKxY02juCEINIbetSp1smG-oQtWgR) link and download 'vgg_model' file and place it in same 'covid_detection' folder. This was done to copy the model which will do the predictions. Since this model was large in size it could not be hosted in github.

* And finally run the project with
```python app.py```

* Open the localhost url provided after running app.py and now you can use the project locally in your web browser.

**DEMO**

* Home Page
![image](https://user-images.githubusercontent.com/88246010/221746732-ba4dc51d-44e7-401c-a01f-4a7c1913f9aa.png)

**Note** : Sometime after clicking submit button page might throw some error just reload the page

* If Prediction is positive
![image](https://user-images.githubusercontent.com/88246010/221746882-83ee3d79-a390-4a96-8a87-1d77b870b22c.png)

* If Prediction is negative
![image](https://user-images.githubusercontent.com/88246010/221746996-61fcd9a4-5b28-425a-9136-f18e1da864aa.png)

**Further Improvements**
1. The UI of this project is too simple more editing cane be done to make it look more attractive.
2. More data can be collected manually via web scrapping to make the system more accurate.

**Contact**

If you have any doubt or want to contribute feel free to email me or hit me up on [LinkedIn](https://www.linkedin.com/in/prabhanshu-gupta-71248118a/
)
