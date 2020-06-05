import os
import tensorflow as tf
import numpy as np
import config

FLAGS = tf.app.flags.FLAGS

hansik_labels = [0, 2, 3, 5, 7, 12, 21, 26, 28, 36, 44, 57, 74, 84, 86, 97, 105, 112, 113, 114]
indexs = [0 for i in hansik_labels]

def list_binary_files(folder):
    return [folder + '/' + d for d in os.listdir(folder)
            if os.path.isfile(os.path.join(folder, d))]


def read_raw_images(data_set):
    dirs = './data/' + data_set + '/'
    filename = list_binary_files(dirs)

    filename_queue = tf.train.string_input_producer(filename)

    if data_set is 'train':
        image_bytes = FLAGS.height * FLAGS.width * FLAGS.depth
        record_bytes = image_bytes + 1
        reader = tf.FixedLengthRecordReader(record_bytes=record_bytes)
        key, value = reader.read(filename_queue)
        record_bytes = tf.decode_raw(value, tf.uint8)
        label = tf.cast(tf.slice(record_bytes, [0], [1]), tf.int32)
        uint8image = tf.reshape(tf.slice(record_bytes, [1], [image_bytes]), [
                                 FLAGS.height,  FLAGS.width, FLAGS.depth])
        return label, uint8image

    elif data_set is 'test':
        image_bytes = FLAGS.height * FLAGS.width * FLAGS.depth
        record_bytes = image_bytes + 1
        reader = tf.FixedLengthRecordReader(record_bytes=record_bytes)
        key, value = reader.read(filename_queue)
        record_bytes = tf.decode_raw(value, tf.uint8)
        uint8image = tf.reshape(tf.slice(record_bytes, [0], [image_bytes]),
                                 [FLAGS.height,  FLAGS.width, FLAGS.depth])
        return uint8image
    elif data_set is 'validation':
        image_bytes = FLAGS.height * FLAGS.width * FLAGS.depth
        record_bytes = image_bytes + 1
        reader = tf.FixedLengthRecordReader(record_bytes=record_bytes)
        key, value = reader.read(filename_queue)
        record_bytes = tf.decode_raw(value, tf.uint8)
        label = tf.cast(tf.slice(record_bytes, [0], [1]), tf.int32)
        uint8image = tf.reshape(tf.slice(record_bytes, [1], [image_bytes]), [
                                 FLAGS.height, FLAGS.width, FLAGS.depth])
        return label, uint8image


def main(argv=None):
    data_set = 'validation' 
    # data_set = 'test'
    # data_set = 'train'

    file_cnts = len(list_binary_files('./data/' + data_set + '/'))-1

    label_and_data = read_raw_images(data_set)
    sess = tf.Session()
    init = tf.initialize_all_variables()
    sess.run(init)
    tf.train.start_queue_runners(sess=sess)
    for i in range(0, 100*file_cnts): ## TODO: set proper number of iterations.
        if (i%20==0):
            print("pic : %d" %(i))
        point, img =  sess.run(label_and_data)
        img = tf.image.encode_jpeg(img)
        img = img.eval(session=sess)
        if (point in hansik_labels):
            idx = hansik_labels.index(point)
            filepath = os.path.join(os.path.join('./data', data_set), "%d_%d.jpg" %(point, indexs[idx]))
            indexs[idx] += 1
            with open(filepath, "w+") as fd: 
                fd.write(img)
                fd.close()

if __name__ == '__main__':
    tf.app.run()