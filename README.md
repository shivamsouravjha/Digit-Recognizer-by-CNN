# Digit-Recognizer-by-CNN
this repo shows a code to recognize digits using CNN



# Handwritten digit recognition using convolutional neural network.
The objective of this project is to build a image-classifier using Convolutional Neural Networks to accurately categorize the handwritten digits. The data for this project can be found <a href="http://yann.lecun.com/exdb/mnist/">here</a> and the files are expected to be stored in the folder "/data/" relative to the repository.

# Convolutional Nerual Networks (CNNs)
Convolutional Neural Networks are a special type of neural networks which are very effective in image recognition and classification. They are powerful as they make use of spatial relationships among the features.
<br>
<br>
There are four main operations in a typical CNN.
<br>
<br>
1.Convolution
<br>
2.Non Linearity
<br>
3.Pooling / Sub Sampling / Down Sampling
<br>
4.Fully Connected Layer
<br>
<br>

# Network Architecture
We use three types of layers, in this model. They are the convolutional layer, pooling layer and fully connected layer.
For this problem, I have defined the following network architecture.
<br>
<br>
Note: The input is a sample set of 60,000 images, where each image is 28x28 pixels with 1 channel.
<br>
<br>
The first layer is a Convolutional layer with 20 filters each of size (6,6) followed by another Convolutional layer with 20 filters each of size (3,3). Then, we have a Max Pooling layer of size (4,4).
<br>
<br>
Similarly, I have defined same set of layers with Convolutional layer having only 10 filters this time.
All the Convolutional layers defined above have ReLU as activation function.
<br>
<br>
Then there are fully connected layers with 30 units in the first and 10 (no. of o/p units) in the second.
The first layer uses tanh as activation function and the second one uses softmax.
<br>
<br>
I also introduced dropouts in between the stacks of layers to avoid overfitting. The key idea behind dropout is to randomly drop units along with their connections to prevent units from co-adapting too much. Read more <a href="https://www.cs.toronto.edu/~hinton/absps/JMLRdropout.pdf">here</a>.

# MNIST Data
The data can be found and is described <a href="http://yann.lecun.com/exdb/mnist/">here</a>.

# Environment Setup
I recommend using Anaconda for running the script. Run the following command on conda shell to create a new environment with all the required packages.
<br>
<br>
<code>conda env create -f mnist-env.yml</code>
<br>
<br>
The mnist-env.yml file can be found in the repo, which contains details of all the required packages to run the script.

# Training
You can begin training the classifier by running the following command. Make sure you have activated the environment before you run the script.
<br>
<br>
<code>python mnist-classifier.py</code>
<br>
<br>
I was able to achieve 97.14% accuracy on training data and 97.86% on test data. I encourage you to play with the architecture and the parameters to see what you are able to achieve. Feel free to discuss the same.

# Classifying New Images
The images in MNIST dataset contains only greyscale images and almost all of them are clean. This is because of the purpose the creators had while creating the dataset. So, there is a need for some preprocessing.
<br>
<br>
First off, the images should be converted to greyscale. This is fairly obvious if you have gone through the training script, where we define the number of channels as 1 in the input format.
<br>
<br>
Secondly, all the images should be resized to (28,28) for the same reason mentioned above.
<br>
<br>
Now, you're ready to make predictions on custom images!
