# To print the value of 'a'.

import os
os.environ['TF_CPP_MIN_LOG_LEVEL']='2'
import tensorflow.compat.v1 as tf
tf.compat.v1.disable_eager_execution()
#tf.disable_v2_behavior()

a = tf.add(3,5)
# Instantiate the session and run the computation inside the session..
sess = tf.compat.v1.Session()
print(sess.run(a))

#close the session..
sess.close()