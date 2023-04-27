from flask import Flask, request
import torch
import io
import numpy as np

app = Flask(__name__)

model = torch.hub.load("ultralytics/yolov5", "custom","best.pt")

@app.route('/', methods=['POST'])
def test():
    data = request.json
    arr = np.array(data['image'])
    results = model(arr)
    results = results.xyxy[0].numpy()
    bbox = results[:,:-2]
    classes = results[:,-1]
    return {"bbox":bbox.tolist(),"class":classes.tolist()}


if __name__ == '__main__':

    app.run(debug=True)
