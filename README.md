# cost-aware-inference-source-code
This repository hosts the source code used for the project "Cost aware inference with early exits".

Below, we provide a brief overview of directory that contains the source code used for the project.

### controller
The python scripts to sychronize the Android workload automation and running native app (see tflite_native_app directory) with tflite.

### modeling_pytorch
Contains the source code for branchyNet modelling and training, converting pytorch models to ONNX format, and ONNX model to tflite format.
Contains tools for estimating branch MACs.

### tflite_native_app
C++ source code (to be cross compiled for arch arm64) with tflite library binding. Executes a model with predefined number of times, spawns the load tracking thread and collect the experimentation results.

### prototype
Source code, both in python and C++ to experiment with load tracking, estimation. Source code to test the proposed algorithm.

### tflite_patch
Patch for tflite (from tensorflow version 2.1) to enable partial execution through braches.

### classification_app
Android application that does realtime image classification on the image frames directly genereted from camera. The source code is taken from android examples, where we modify to lof the frame drops.
