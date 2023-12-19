from flask import Flask, request, send_file, render_template
from moviepy.editor import VideoFileClip
from werkzeug.utils import secure_filename
import os

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generate_video', methods=['POST'])
def generate_video():
    input_video = request.files['input_video']
    output_path = process_video(input_video)
    return send_file(output_path, as_attachment=True)

def process_video(input_video):
    # Set the path for the processed video
    output_path = 'output_video.mp4'

    # Generate a secure filename to avoid any potential security issues
    input_filename = secure_filename(input_video.filename)

    # Save the input video file temporarily
    input_video.save(input_filename)

    # Open the video file
    video_clip = VideoFileClip(input_filename)

    # Example: Rotate the video by 90 degrees
    rotated_clip = video_clip.rotate(90)

    # Write the processed video to the output path
    rotated_clip.write_videofile(output_path, codec="libx264")

    # Close the video clip
    rotated_clip.close()

    # Remove the temporary input file
    os.remove(input_filename)

    return output_path

if __name__ == '__main__':
    app.run(debug=True)
