**Covid Detection Using X-Rays**

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
conda create -n covid_detection python=3.6.12
pip install -r requirements.txt
conda activate covid_detection 
```

* And finally run the project with
```python app.py```

* Open the localhost url provided after running app.py and now you can use the project locally in your web browser.

**DEMO**

* Home Page
![image](https://user-images.githubusercontent.com/88246010/221581347-f3e2051a-eda9-4913-a2ca-a013e4d1af5e.png)

**Note** : Sometime after clicking submit button page might throw some error just reload the page

* If Prediction is positive
![image](https://user-images.githubusercontent.com/88246010/221581798-a35abe13-3c5e-4ef1-ad71-4af61ea2cb5e.png)

*If Prediction is negative
![image](https://user-images.githubusercontent.com/88246010/221582065-39455d21-8805-4f2e-ae8f-c3c3be202dcd.png)

**Further Improvements**
1. The UI of this project is too simple more editing cane be done to make it look more attractive.
2. More data can be collected manually via web scrapping to make the system more accurate.

**Contact**

If you have any doubt or want to contribute feel free to email me or hit me up on [LinkedIn](https://www.linkedin.com/in/prabhanshu-gupta-71248118a/
)
