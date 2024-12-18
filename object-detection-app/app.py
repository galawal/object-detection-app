import gradio as gr
    import cv2
    import numpy as np
    from pathlib import Path
    import random

    # ... (Your yolo_detection and draw_bounding_boxes functions) ...

    def inference(image):
        image, bounding_boxes, confidences, class_numbers, results = yolo_detection(image)
        image_with_boxes = draw_bounding_boxes(image, bounding_boxes, confidences, class_numbers, results)
        return image_with_boxes

    iface = gr.Interface(
        fn=inference,
        inputs=gr.Image(type="filepath"),
        outputs="image",
        title="YOLOv3 Object Detection",
        description="Upload an image to detect objects.",
    )
    iface.launch()
