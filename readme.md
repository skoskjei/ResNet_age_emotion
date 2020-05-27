ResNet for classifying age and emotion
This is a project in the course ICT Seminar 2 at University of Agder. Pre-trained ResNets from Keras are used to classify age and emotion using a single model and a single dataset which combines the two features.

Datalabels:
The images in the dataset is labeled as follows;
The label is the first two groups of digits of the filename. The groups are separated by an underscore (‘_’). The last group of digits is the original filename.
The first group, which consists of two integers, represents the age group, and the second group, consisting of only one integer, represents the emotion.
11_x = belong to age group 11 (17-18 years old)
xx_0 = unhappy (0=unhappy and 1=happy)

For instance, an image with filename 24_1_2948.png is of a happy person that is between 65 and 71 years old.

See age groups and corresponding ages in the table below;
[insert table]

Licence:
MIT License

Copyright (c) 2020 Øyvor Ystad Skjei & Emilija Jasinskaite

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.