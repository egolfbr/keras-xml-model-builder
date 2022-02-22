import os
os.environ["KERAS_BACKEND"] = "tensorflow"
import keras 
from keras.engine.base_layer import Layer
from keras import layers
from keras.layers import Dense, Flatten, Conv2D, Conv3D, MaxPooling2D, MaxPooling3D, InputLayer
from keras.models import Sequential
from keras import Model
import sys 
import xml.etree.ElementTree as ET


def from_xml(filePath):
    tree = ET.parse(filePath)
    root = tree.getroot()
    #loop through each layer
    print("Parsing XML file... ...")
    for model_type in root.findall('model_type'):
        if model_type.text == "Sequential":
            myModel = keras.models.Sequential()
        else:
            sys.exit("Keras-XML: Invalid or no model type specified")

    for layer in root.findall('layer'):
        # Determine the type of each layer 
        layer_type = layer.find('layer_type')
        layer_type = layer_type.text
        if layer_type == "Dense":
            units = (layer.find('units'))
            units = units.text
            act_func = (layer.find('activation'))
            act_func = act_func.text
            if root.findall('layer').index(layer) == 0:
                inp = layer.find('input_dim')
                inp = inp.text
                myModel.add(keras.layers.Dense(int(units),activation=act_func, input_dim=int(inp)))
            else:
                myModel.add(keras.layers.Dense(int(units),activation=act_func))
        elif layer_type == "Conv2D" or layer_type == "Conv3D" or layer_type == "Conv1D":
            filts = (layer.find('filters'))
            filts = filts.text
            filt_dim = (layer.find('filter_dimension'))
            filt_dim = filt_dim.text
            filt_dim = tuple(map(int, filt_dim.split(',')))
            act_func  = (layer.find('activation'))
            if layer_type == "Conv2D":
                myModel.add(keras.layers.Conv2D(int(filts),filt_dim,activation=act_func))
            elif layer_type == "Conv3D":
                myModel.add(keras.layers.Conv3D(int(filts),filt_dim,activation=act_func))
            else:
                myModel.add(keras.layers.Conv1D(int(filts),filt_dim,activation=act_func))
        elif layer_type == "Flatten" or layer_type == "GlobalMaxPooling2D" or layer_type == "GlobalAveragePooling2D" or layer_type == "GlobalAveragePooling3D" or layer_type == "GlobalMaxPooling3D":
            if layer_type == "Flatten":
                myModel.add(keras.layers.Flatten())
            elif layer_type == "GlobalMaxPooling2D":
                myModel.add(keras.layers.GlobalMaxPooling2D())
            elif layer_type == "GlobalAveragePooling2D":
                myModel.add(keras.layers.GlobalAveragePooling2D())
            elif layer_type == "GlobalMaxPooling3D":
                myModel.add(keras.layers.GlobalMaxPooling3D())
            elif layer_type == "GlobalAveragePooling3D":
                myModel.add(keras.layers.GlobalAveragePooling3D())
        elif layer_type == "Dropout":
            rates = (layer.find('rate'))
            rates = rates.text
            myModel.add(keras.layers.Dropout(float(rates)))
        elif layer_type == "Activation":
            act_func = (layer.find('activation'))
            act_func = act_func.text
            myModel.add(keras.layers.Activation(act_func))
        elif layer_type == "compile":
            loss_func = layer.find('loss')
            loss_func = loss_func.text
            opt = layer.find('optimizer')
            opt = opt.text
            mets = layer.find('metrics')
            mets = mets.text
            myModel.compile(optimizer=opt,loss=loss_func)
        elif layer_type == "Input":
            shape = layer.find('input_shape')
            shape = shape.text
            shape = tuple(map(int, shape.split(',')))
            myModel.add(keras.layers.InputLayer(input_shape=shape))
    print("Model Created! Ready to train!")
    return myModel

  
        


new_model = from_xml("example2.xml")
print(new_model.summary())




