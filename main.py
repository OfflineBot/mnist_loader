from keras.datasets import mnist
import json

import shutil
import os
import numpy as np

def reset():
    if os.path.exists("storage"):
        shutil.rmtree("storage")
    
    os.mkdir("storage")

    with open(f'storage/mnist_data.json', 'w+') as file:
        file.flush()
        mnist_text = {
            "input": {
                "0": [],
                "1": [],
                "2": [],
                "3": [],
                "4": [],
                "5": [],
                "6": [],
                "7": [],
                "8": [],
                "9": []
            },
            "output": {
                "0": [],
                "1": [],
                "2": [],
                "3": [],
                "4": [],
                "5": [],
                "6": [],
                "7": [],
                "8": [],
                "9": []
            }
        } 
        json.dump(mnist_text, file, indent=2)


reset()
single_image_min_count = 10
num_count = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

with open('storage/mnist_data.json', 'r') as mnist_data:

    existing_data = json.load(mnist_data)    
    (train_x, train_y), (test_x, test_y) = mnist.load_data()
    i = 0
    while (min(num_count) < single_image_min_count):
        output_list = ['0', '0', '0', '0', '0', '0', '0', '0', '0']

        # input 
        input_image = np.array(train_x[i]).reshape(28*28).tolist()
        input_data = input_image
        output_image = np.array(train_y[i])

        # managing counter
        num_count[output_image - 1] += 1

        # output
        output_list[output_image - 1] = '1'
        output_data = output_list

        # saving to json
        existing_data['input'][str(output_image)].append(input_data)
        existing_data['output'][str(output_image)].append(output_data)

        # for loop
        i += 1

        

with open('storage/mnist_data.json', 'w+') as file:
    json.dump(existing_data, file, indent=2)

print(num_count)