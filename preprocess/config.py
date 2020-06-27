import tensorflow as tf

FLAGS = tf.app.flags.FLAGS
BINARY_FILES_DIR = './data'
# flags = {'width':256, 'height':256, 'depth':3}

tf.app.flags.DEFINE_integer('width',  256, '')
tf.app.flags.DEFINE_integer('height', 256, '')
tf.app.flags.DEFINE_integer('depth', 3, '')

