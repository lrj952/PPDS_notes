
import matplotlib.pyplot as plt
from handin6 import read_mnist_csv
from handin6 import group_by_label
from handin6 import convert_to_images
from handin6 import draw_image
from handin6 import draw_image_row
from handin6 import calc_group_averages

# Q1
mnist_test = read_mnist_csv('mnist_test_200.csv')
type(mnist_test)

# Q2

out_q2 = group_by_label(mnist_test)
print(out_q2)
print(len(out_q2))

# Q3

out_q3 = convert_to_images(out_q2)
print(out_q3)
print(len(out_q3))


# Q4
draw = draw_image(out_q3[0][0])
plt.show()

# Q5
draw_row = draw_image_row(out_q3)
plt.show()

# Q6
q6 = calc_group_averages(out_q3)
draw_image_row(q6)