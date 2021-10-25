# Q1
# In the module file called handin6.py, create a function called read_mnist_csv, which takes a
# single argument called filename. This function should read the file, and return a numpy array.
# Note that the first line in the .csv file is a header with column names, which you should exclude
# when reading in the data. Hint: you can use genfromtxt for this task.
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

def read_mnist_csv(filename):
    """Read in csv file to numpy array"""
    file = np.genfromtxt(filename, skip_header = 1, delimiter = ',', dtype=int)
    return file

print(read_mnist_csv('mnist_test_200.csv'))
out_q1 = read_mnist_csv('mnist_test_200.csv')
print(out_q1.shape)
# Verify that your function works by calling it from the handin6_test.py file, on the filename
# mnist_test_200.csv. Note how the data is organized: each image correponds to one row; the first
# columns specifies which digit this image contains (there are examples for all 10 digits), and the
# remaining columns specify the values for each of the 28x28 pixels in the image.

# Q2
# As mentioned, the first column in the dataset specifies which of the digits the row corresponds to.
# Write a function called group_by_label that takes a numpy array as argument, and returns a list of
# numpy arrays, grouped by these 10 digits. The output should thus be a list with 10 elements, where,
# for example, the first element is a numpy array corresponding to all rows (images) with the digit 0.
# Hint: The np.where function can give you all the indices where a numpy array has a particular value.
# So, for instance, the following will return all elements in an array x where the values are zero:

def group_by_label(file):
    """takes a file(numpy array in and returns a list of numpy arrays grouped by first value"""
    list_of_numpy_array = []
    for i in range(0,10):
        digit = file[np.where(file[:,0] == i)]
        list_of_numpy_array.append(digit)
    return list_of_numpy_array

out_q2 = group_by_label(out_q1)
print(out_q2)

# indices = np.where(x == 0)
# print(x[indices])
# Again, verify that it works by calling the group_by_label function from your handin6_test.py file,
# using the numpy array from the previous exercise as argument.

# Q3
# Now, let's convert the data in the rows to actual images. You will notice that we have 785 column -
# the first one is the digit label, and the remaining 784 are the 28x28 pixel values. In your handin6.py
# file, write a function called convert_to_images that takes a list of numpy arrays as input (the one
# created by the previous exercise), and returns a list with numpy arrays with shape (???, 28, 28), where
# ??? is the size of the group.
# Hint: you can use the reshape method in any numpy array to change the
# shape of an array (while keeping the total number of elements fixed).

def convert_to_images(list_of_numpy_arrays):
    """takes a list of numpy arrays as input, returns list with numpy arrays with shape"""
    input = list_of_numpy_arrays
    output_array = []
    for i in range(0,10):
        input_no_first_column = []      # restart list for each new digit
        for k in range(0,len(input[i])):
            input_no_first_column.append(input[i][k,1:])       # Make a list of the digit without first column
        output_array.append(np.reshape(input_no_first_column, (len(input_no_first_column), 28, 28)))
            # Append each digit one at a time to output while reshaping to correct shape
    return output_array

out_q3 = convert_to_images(out_q2)
print(out_q3)
print(len(out_q3))

print(len(out_q3[0]))

# Verify that your function works by calling it from handin6_test.py using the list of grouped numpy
# arrays from the previous exercise as input.

# Q4
# Now let's visualize a digit. In your handin6.py file, write a function called draw_image that takes a
# 28x28 pixel numpy array group as input, and shows it on screen. You can use matplotlib's imshow
# function for this purpose. Set the color map (cmap) to gray and remove the axis on the plot.

def draw_image(pixel_array):
    """Function that takes a 28x28 pixel numpy array group as input, and shows it on screen"""
    plt.figure()
    plt.imshow(pixel_array, cmap='gray')
    plt.axis('off')
    return pixel_array

# Again, check that it is working by calling the draw_image function from the handin6_test.py file,
# using the first image in the zero-digit group as an example. To visualize it, add a plt.show()
# to your handin6_test.py (don't put it in the main module, since it will disrupt the testing procedure).


# Q5
# Now let's create a visualization containing one of each digit. In your handin6.py file,
# write a function called draw_image_row, which takes a list of numpy arrays as its input (i.e.
# the groups from before). Within this function, you can use fig, axs = plt.subplots(rows, columns)
# function to create a grid of small plots. Since we only want a single row, you can set the first
# argument to 1, while the second argument of subplots should be the number of groups. The subplots
# call will create a number of miniplots, which you can access through the axs variable.
# For instance, to visualize something in the first miniplot, you would write axs[0].imshow(...).
# For simplicity, just choose the first image in each group to visualize.

def draw_image_row(list_of_numpy_arrays):
    """Draw 1 image row, with first 10 images, one of each digit"""
    plt.figure()
    fig, axs = plt.subplots(1, len(list_of_numpy_arrays))
    for i in range(0,len(list_of_numpy_arrays)):
        axs[i].imshow(list_of_numpy_arrays[i][0], cmap='gray')
    return list_of_numpy_arrays


# Call the draw_image_row from your handin6_test.py using the groups list from the exercises above.
# Verify that you indeed get a row of all 10 digits.

# Q6
# Finally, let's calculate the average image for each group. In your handin6.py file, write a
# function called calc_group_averages, that takes a list of numpy arrays as input, and returns a new
# list of numpy arrays, where each numpy array is now just a single image, which is an average of all
# the images in the group. Hint: you will need to use the axis option of np.average like we saw in class.
# Please make sure that your output images have the shape (1,28,28) rather than just (28,28) -
# which you can do using the reshape method. This ensures that you can reuse the draw_image_row function
# to visualize these averaged images.


def calc_group_averages(list_of_numpy_arrays):
    """Calculate the average number and prints it"""
    output2 = []
    for i in range(0,len(list_of_numpy_arrays)):
        output = []
        output.append(np.average(list_of_numpy_arrays[i], axis = (0)))
        output2.append(np.reshape(output, (len(output), 28, 28)))
    return output2



#     input = list_of_numpy_arrays
#     output_array = []
#     for i in range(0,10):
#         input_no_first_column = []
#         for k in range(0,len(input[i])):
#             input_no_first_column.append(input[i][k,1:])
#         output_array.append(np.reshape(input_no_first_column, (len(input_no_first_column), 28, 28)))
#     return output_array

# From your handin6_test.py file, call the calc_group_averages function using the group list from the
# previous exercises. Now take the resulting list, and use it to call draw_image_row again - this time
# to get a row of average images for each digit.

# q6 = calc_group_averages(out_q3)
