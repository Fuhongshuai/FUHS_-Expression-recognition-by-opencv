import tensorflow as tf
import cv2
import numpy as np
import os
import sys
sys.path.append("/users/fuhongshuai/PycharmProjects/face/")
import train

expression_dic = {'0':'angry','1':'disgust','2':'fear','3':'happy','4':'neutral','5':'sad','6':'surprise'}
#img1_path = '/users/fuhongshuai/PycharmProjects/face/manface/'
save_path = '/users/fuhongshuai/PycharmProjects/face_recognition/checkpoint_dir'


def init():
    x = tf.placeholder(tf.float32, [None, 2304])
    y = tf.placeholder(tf.float32, [None, 7])
    keep_prob = tf.placeholder(tf.float32)
    Face_data = np.zeros((1, 48 * 48))
    Face_label = np.zeros((1, 7), dtype=int)
    xavier_init = tf.contrib.layers.xavier_initializer()
    zero_init = tf.zeros_initializer()
    wc1 = tf.get_variable("wc1", [3, 3, 1, 8], initializer=xavier_init)
    wc2 = tf.get_variable("wc2", [3, 3, 8, 16], initializer=xavier_init)
    wc3 = tf.get_variable("wc3", [3, 3, 16, 32], initializer=xavier_init)
    # out_weights = tf.get_variable("out_weights",[n_classes],initializer = xavier_init)
    bc1 = tf.get_variable("bc1", [8], initializer=zero_init)
    bc2 = tf.get_variable("bc2", [16], initializer=zero_init)
    bc3 = tf.get_variable("bc3", [32], initializer=zero_init)
    bd1 = tf.get_variable("bd1", [200], initializer=zero_init)
    # out_biases = tf.get_variable("out_biases",[n_classes],initializer = zero_init)
    weights = dict(wc1=wc1, wc2=wc2, wc3=wc3)
    biases = dict(bc1=bc1, bc2=bc2, bc3=bc3, bd1=bd1)
    model = train.Model(x, y, keep_prob, Face_data, Face_label, weights, biases)
    return model

def test(img,model):
    # net_g_test = model.conv_net(x)
    saver = tf.train.Saver()
    # ckpt = tf.train.get_checkpoint_state(checkpoint_dir = save_path)
    with tf.Session() as sess:
        sess.run(tf.initialize_all_variables())
        # if ckpt and ckpt.model_checkpoint_path:
        # ckpt_name = os.path.basename(ckpt.model_checkpoint_path)
        saver.restore(sess, save_path + '/model_' + '4200' + '.cptk')
        # print(" [*] Success to read {}".format(ckpt_name))
        # else:
        # print(" [*] Failed to find a checkpoint")
        net_g_answer = sess.run(model.fc1, feed_dict={x: img})
        #print(net_g_answer)
        answer = sess.run(tf.argmax(net_g_answer, 1))
        print(expression_dic['answer'])













