import os
import cv2
import numpy as np
import tensorflow as tf
from object_detection import label_map_util
from object_detection import visualization_utils as vis_util

CWD_PATH = os.getcwd()
PATH_TO_CKPT = os.path.join(CWD_PATH,'object_detection','inference_graph','frozen_inference_graph.pb')
PATH_TO_LABELS = os.path.join(CWD_PATH,'object_detection','training','labelmap.pbtxt')
PATH_TO_IMAGE = os.path.join(CWD_PATH,'streetview.jpg')
NUM_CLASSES = 1

label_map = label_map_util.load_labelmap(PATH_TO_LABELS)
categories = label_map_util.convert_label_map_to_categories(label_map, max_num_classes=NUM_CLASSES, use_display_name=True)
category_index = label_map_util.create_category_index(categories)

detection_graph = tf.Graph()
with detection_graph.as_default():
	od_graph_def = tf.GraphDef()
	with tf.gfile.GFile(PATH_TO_CKPT, 'rb') as fid:
		serialized_graph = fid.read()
		od_graph_def.ParseFromString(serialized_graph)
		tf.import_graph_def(od_graph_def, name='')

	sess = tf.Session(graph=detection_graph)

# Define input and output tensors (i.e. data) for the object detection classifier
image_tensor = detection_graph.get_tensor_by_name('image_tensor:0')
detection_boxes = detection_graph.get_tensor_by_name('detection_boxes:0')
detection_scores = detection_graph.get_tensor_by_name('detection_scores:0')
detection_classes = detection_graph.get_tensor_by_name('detection_classes:0')
num_detections = detection_graph.get_tensor_by_name('num_detections:0')

# Load image using OpenCV
image = cv2.imread(PATH_TO_IMAGE)
image_expanded = np.expand_dims(image, axis=0)

# Perform the actual detection by running the model with the image as input
(boxes, scores, classes, num) = sess.run(
	[detection_boxes, detection_scores, detection_classes, num_detections],
	feed_dict={image_tensor: image_expanded})
		
# Draw the results of the detection (aka 'visulaize the results')
vis_util.visualize_boxes_and_labels_on_image_array(
	image,
	np.squeeze(boxes),
	np.squeeze(classes).astype(np.int32),
	np.squeeze(scores),
	category_index,
	use_normalized_coordinates=True,
	line_thickness=1,
	min_score_thresh=0.7)
		
PATH_TO_IMAGE2 = os.path.join(CWD_PATH,'image.jpg')		
cv2.imwrite(PATH_TO_IMAGE2,image)