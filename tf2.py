# To print the value of 'a'.

import os
os.environ['TF_CPP_MIN_LOG_LEVEL']='2'
import tensorflow.compat.v1 as tf
tf.compat.v1.disable_eager_execution() # for tensorflow v.2.x

a = tf.add(3,5)
# Instantiate the session and run the computation inside the session..
# with clause takes care of sess.close()
with tf.compat.v1.Session() as sess:
    print(sess.run(a))
