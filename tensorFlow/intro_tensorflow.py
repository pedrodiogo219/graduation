import tensorflow as tf

#inicializando as constantes
x1 = tf.constant([1,2,3,4])
x2 = tf.constant([5,6,7,8])

#multiplicando os Tensors
result = tf.multiply(x1, x2)

#inicializando secao
sess = tf.Session()

print(sess.run(result))

sess.close()
