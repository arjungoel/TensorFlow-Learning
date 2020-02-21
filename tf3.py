# To print the value of 'a'.
import os
os.environ['TF_CPP_MIN_LOG_LEVEL']='2'
import tensorflow.compat.v1 as tf
tf.compat.v1.disable_eager_execution() # for tensorflow v.2.x

x = 4
y = 3
op1 = tf.add(x,y)
op2 = tf.multiply(x,y)

#concept of lazy evaluation
useless = tf.multiply(x,op1)
op3 = tf.pow(op1,op2)

# Instantiate the session and run the computation inside the session..
# with clause takes care of sess.close()
with tf.compat.v1.Session() as sess:
    op3 = print(sess.run(op3))
