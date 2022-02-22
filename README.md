# keras-xml-model-builder 
A Keras model builder which takes in an xml file and then builds a Keras model.

## Description
This is designed to allow the user to write an XML file and build a keras model from it. There are two different methods that the suer can choose from. The first method is the user can sepcify a file path to the XML file and an output file path and the script will generate a python file that will build the keras model. The second method is that the user can sepcify just teh XML path and the script will output a keras model instance. This is done with a two-pass traversal of the XML data. First we learn all the data that the user has input and then we update/create each layer accoringly. This way the user can specify any combination of parameters for each layer and whatever the pareser finds it will update and everything else will be left to default settings. This project will also include functionality to send a current model to an XML file. Unfortunately this will only save the architecture and not the weights of a trained model.

## XML Rules 
The XML file must start with ```<model>``` and end with ```</model>```. This is the root of the XML tree. From there the user MUST specify the model type. In keras this is most likely ```Sequential```. After that, the user can define at will the amount of layers and the children of each layer. An example XML file is included in this repository and a list of usable XML tags is included at the bottom of this README. The goal of this project is to make the XML parser as robust as possible. The first stage will be to get existing keras model functionality built and then add in functionality for custom layers, activation functions etc. 

## Contact Information 
Brian Egolf - egolfbr@miamioh.edu 

### XML tags 
It is assumed the user knows that each tag has a similar end tag of the format ```</tag_name>```.
Ex.
```<model>``` and ```</model>```
#### Full List
- ```<model>```
- ```<layer>```
- ```<layer_type>```
- ```<activation>```
- ```<units>```
- ```<filters>```
- ```<filter_dimension>```
- ```<input_shape>```
- ```<optimizer>```
- ```<loss>```
- ```<rate>```
- ```<input_dim>```

Future updates will include more layer types and parameters. 
