The app.py is the flask server. Before running this we have to first install yolov5 by running the following commands.

1. git clone https://github.com/ultralytics/yolov5
2. cd yolov5
3. pip install -r requirements.txt  # install

After that we need to install the dependencies listed in the requirements.txt of this repo. We also need to download the model weights from https://drive.google.com/file/d/1IHtINbOzGtB--vfpe_euEXXmMJFdWeEy/view?usp=sharing. 
To run the server we just neeed to run the app.py file. To test the server we can run the test.py file.

For training the model I used the scripts given in the yolov5 repository. I only changed the data.yaml since there are only 2 classes and specified the dataset directory.

Details about the training experiments can be found in the pdf file.

The dataset can be downloaded from https://drive.google.com/file/d/1vQOfVQxFn9JDWHHMCNPVToS8EPZp-gSt/view?usp=sharing
