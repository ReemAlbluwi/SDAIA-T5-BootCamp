
---

# Real-Time Vehicle Detection, Counting, and Classification

This project demonstrates real-time vehicle detection, counting, and classification using a YOLOv8 model. The video processing involves detecting vehicles in real-time, counting them in the right and left lanes, and distinguishing between cars and trucks.

## Features

- **Real-Time Vehicle Detection**: Identifies vehicles in a video feed using a pre-trained YOLOv8 model.
- **Vehicle Counting**: Counts the number of vehicles in both the right and left lanes.
- **Vehicle Classification**: Classifies detected vehicles into cars and trucks.
- **Visualization**: Displays the processed video with real-time annotations, including the total vehicle count and classification results.

## Requirements

To run the code, you will need the following:

- Python 3.x
- OpenCV
- Numpy
- Ultralytics YOLOv8

You can install the required Python packages using pip:

```bash
pip install opencv-python numpy ultralytics
```

## Usage

1. **Clone the repository**:

    ```bash
    git clone https://github.com/yourusername/your-repository-name.git
    cd your-repository-name
    ```

2. **Download the YOLOv8 model**:  
   Ensure that you have a trained YOLOv8 model file (`YOLO_Model.pt`). Place it in the same directory as the script or adjust the path in the code.

3. **Run the script**:  
   Make sure your video file (`sample_video.mp4`) is in the same directory or update the path in the script. Then run the script using:

    ```bash
    python your_script_name.py
    ```

4. **View the output**:  
   The processed video will be saved as `processed_sample_video.avi`. You can open this video using any media player to see the real-time detection, counting, and classification.

## Code Explanation

- **YOLOv8 Model Loading**: The script loads a pre-trained YOLOv8 model for vehicle detection.
- **Video Processing**: The video is read frame-by-frame, and vehicles are detected, counted, and classified in real-time.
- **Drawing and Annotation**: The script draws polygons for lane boundaries, counts vehicles in each lane, and adds real-time annotations to the video frames.
- **Saving the Output**: The processed video is saved to disk for later viewing.

## Output

The output video will display:
- **Title**: "Vehicle Classification: Cars vs. Trucks"
- **Real-Time Counts**: Displays the count of vehicles in each lane as well as the total count.
- **Annotations**: Highlights detected vehicles and classifies them as cars or trucks.

## Contributing

If you would like to contribute to this project, please fork the repository and submit a pull request with your improvements.

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.

## Contact

For any questions or suggestions, feel free to open an issue or contact me at [ireemalbluwi@gmail.com](mailto:ireemalbluwi@gmail.com).

