import tensorflow as tf
import os
os.environ['TF_CPP_MIN_LOG_LEVEL']='3'

def run():
    output = None
    #logit_data = [2.0, 1.0, 0.1] #[ 0.65900117  0.24243298  0.09856589]
    logit_data = [0.02, 0.01, 0.001]  # [ 0.33656105  0.3332122   0.33022675]
    # [20, 10, 1] will close to 0.0 or 1.0
    logits = tf.placeholder(tf.float32)
    print(logits)

    softmax = tf.nn.softmax(logits)
    print(softmax)

    with tf.Session() as sess:
        output = sess.run(softmax, feed_dict={logits: logit_data})

    print(output)
    return output

run()
